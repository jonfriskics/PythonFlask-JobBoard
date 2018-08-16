import pytest
import sys, os, inspect, re

from bs4 import BeautifulSoup

from jobs import app

def list_routes(app):
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        if rule.endpoint is not 'static':
            rules.append(rule.endpoint+':'+ methods +':'+ str(rule))
    return rules

@pytest.mark.app_import_flask
def test_app_import_flask():
    assert 'Flask' in dir(app), 'Have you imported the `Flask` class from `flask`'
    assert inspect.isclass(app.Flask), '`Flask` is not a class.'
    assert 'render_template' in dir(app), '`render_template` has not been imported.'
    assert callable(app.render_template), '`render_template` is not a function.'

@pytest.mark.app_create_flask_app
def test_app_create_flask_app():
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert isinstance(app.app, app.Flask), '`app` is not an instance of the `Flask` class.'

@pytest.mark.templates_folder
def test_templates_folder():
    assert os.path.isdir('jobs/templates'), 'The `templates` folder has not been created.'

@pytest.mark.index_template
def test_index_template():
    assert os.path.isfile('jobs/templates/index.html'), 'The `index.html` template does not exist in the `templates` folder.'
    index = BeautifulSoup(open(os.getcwd() + '/jobs/templates/index.html'), 'html.parser')
    assert index.find('h1'), 'The `index.html` template does not contain an `<h1>`.'
    assert index.find('h1').text == 'Jobs', "The `<h1>` in the `index.html` template does not contain the contents 'Jobs'."

@pytest.mark.app_index_route_function
def test_app_index_route_function():
    assert os.path.isfile('jobs/templates/index.html'), 'The `index.html` template does not exist in the `templates` folder.'
    assert 'jobs' in dir(app)
    with app.app.app_context():
        assert re.findall(r"return\s*render_template\s*\(\s*(?:'|\")index\.html(?:'|\")\s*\)", inspect.getsource(app.jobs))

@pytest.mark.app_route_decoractors
def test_app_route_decoractors():
    assert os.path.isfile('jobs/templates/index.html'), 'The `index.html` template does not exist in the `templates` folder.'
    assert 'jobs' in dir(app)

    rules = list_routes(app.app)

    assert 'jobs:GET,HEAD,OPTIONS:/jobs' in rules
    assert 'jobs:GET,HEAD,OPTIONS:/' in rules
