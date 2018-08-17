import os
import ast
import inspect
from pprint import pprint

from bs4 import BeautifulSoup

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
        functions.append(name + ':' + ':'.join([a.s for a in node.args]))

    node_iter = ast.NodeVisitor()
    node_iter.visit_Call = visit_Call
    node_iter.visit(ast.parse(inspect.getsource(source)))

    return functions

def list_routes(app):
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        if rule.endpoint is not 'static':
            rules.append(rule.endpoint+':'+ methods +':'+ str(rule))
    return rules

def template_exists(name):
    return os.path.isfile('jobs/templates/' + name + '.html')

def template_contains(name, tag):
    doc = BeautifulSoup(open(os.getcwd() + '/jobs/templates/' + name + '.html'), 'html.parser')
    return doc.find(tag)

def tag_contains(name, tag, text):
    return template_contains(name, tag).text if template_contains(name, tag) else False
