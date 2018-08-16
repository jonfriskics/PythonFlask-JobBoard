import pytest
import sys
import pprint

from jobs import app

@pytest.mark.app_import_flask
def test_app_import_flask():
    pass

@pytest.mark.app_create_flask_app
def test_app_create_flask_app():
    pass

@pytest.mark.templates_folder
def test_templates_folder():
    pass

@pytest.mark.index_template
def test_index_template():
    pass

@pytest.mark.app_index_route_function
def test_app_index_route_function():
    pass

@pytest.mark.app_route_decoractors
def test_app_route_decoractors():
    pass

