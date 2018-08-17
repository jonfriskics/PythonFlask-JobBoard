import os
import ast
import inspect
from pprint import pprint

from jinja2 import nodes, Environment, PackageLoader, meta, exceptions
from bs4 import BeautifulSoup

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
            functions.append(name + ':' + ':'.join([a.s for a in node.args]))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))

    return functions


def get_statements(source):
    statment = []

    def visit_If(node):
        print(ast.dump(node))

    node_iter = ast.NodeVisitor()
    node_iter.visit_If = visit_If
    node_iter.visit(ast.parse(inspect.getsource(source)))

    return statment

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
