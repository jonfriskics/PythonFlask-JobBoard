import ast
import inspect
import json
import os
import collections

from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader, exceptions, meta, nodes
from jmespath import search

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

env = Environment(loader=PackageLoader('jobs', 'templates'))

def get_decorators(source):
    decorators = {}
    def visit_FunctionDef(node):
        decorators[node.name] = []
        for n in node.decorator_list:
            name = ''
            if isinstance(n, ast.Call):
                name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
            else:
                name = n.attr if isinstance(n, ast.Attribute) else n.id

            args = [a.s for a in n.args] if hasattr(n, 'args') else []
            decorators[node.name].append((name, args))

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return decorators

def get_functions(source):
    functions = []
    def visit_Call(node):
        name = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id
        if name == 'getattr':
            functions.append(name + ':' + node.args[0].id + ':' + node.args[1].s + ':' + str(node.args[2].value))
        else:
            if name is not 'connect':
                functions.append(name + ':' + ':'.join([a.s for a in node.args]))


    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return functions

def get_assignments(source):
    assignments = []
    def visit_Assign(node):
        assignments.append(build_dict(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Assign = visit_Assign
    node_iter.visit(ast.parse(inspect.getsource(source)))
    return assignments

def pair_exists(d, key, value):
    return key in d and value == d[key]

def build_dict(node):
    result = {}
    if node.__class__.__name__ == 'Is' or node.__class__.__name__ == 'Eq':
        result['node_type'] = node.__class__.__name__
    for attr in dir(node):
        if not attr.startswith("_") and attr != 'ctx' and attr != 'lineno' and attr != 'col_offset':
            value = getattr(node, attr)
            if isinstance(value, ast.AST):
                value = build_dict(value)
            elif isinstance(value, list):
                final = [build_dict(n) for n in value]
                value = final[0] if len(final) == 1 else final
            if value != []:
                result[attr] = value
    return flatten(result, sep='/')

def source_dict(source):
    return build_dict(ast.parse(inspect.getsource(source)))

def source_search(source, node_type, expr):
    expr = "body[0].body[?node_type == `{}`]{}".format(node_type, expr)
    return search(expr, source_dict(source))

def list_routes(app):
    rules = []

    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        if rule.endpoint is not 'static':
            rules.append(rule.endpoint + ':' + methods + ':' + str(rule))

    return rules

def template_values(name, function):
    values = []

    for node in parsed_content(name).find_all(nodes.Call):
        if node.node.name == function:
            values.append(node.args[0].value + ':' + node.kwargs[0].key + ':' +  node.kwargs[0].value.value)

    return values

def template_exists(name):
    return os.path.isfile('jobs/templates/' + name + '.html')

def template_source(name):
    try:
        return env.loader.get_source(env, name + '.html')[0]
    except exceptions.TemplateNotFound:
        return None

def template_doc(name):
    return BeautifulSoup(template_source(name), 'html.parser')

def template_find(name, tag, limit=None):
    return BeautifulSoup(template_source(name), 'html.parser').find_all(tag, limit=limit)

def parsed_content(name):
    return env.parse(template_source(name))

def template_extends(name):
    return list(meta.find_referenced_templates(parsed_content(name)))
