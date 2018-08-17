import pytest
import sys

from jobs import app
from .utils import *


@pytest.mark.app_import_sqlite
def test_app_import_sqlite_module3():
    assert 'sqlite3' in dir(app), 'Have you imported `sqlite`'

@pytest.mark.app_import_g
def test_app_import_g_module3():
    assert 'g' in dir(app), 'Have you imported the `g` class from `flask`'

@pytest.mark.app_db_path
def test_app_db_path_module3():
    assert 'DATABASE' in dir(app), 'Have you created a constant called `DATABASE`.'
    assert app.DATABASE == 'db/jobs.sqlite', 'Have you created a constant called `DATABASE`.'

@pytest.mark.app_get_db_get_attribute
def test_app_get_db_get_attribute_module3():
    assert 'get_db' in dir(app), 'Have you defined a function named `get_db`.'
    assert 'getattr:g:_database:None' in get_functions(app.get_db)

@pytest.mark.app_get_db_connection
def test_app_get_db_connection_module3():
    get_statements(app.get_db)
    assert False

@pytest.mark.app_get_db_row_factory
def test_app_get_db_row_factory_module3():
    pass

@pytest.mark.app_query_db
def test_app_query_db_module3():
    pass

@pytest.mark.app_query_db_parameters
def test_app_query_db_parameters_module3():
    pass

@pytest.mark.app_query_db_execute
def test_app_query_db_execute_module3():
    pass

@pytest.mark.app_query_db_fetchall
def test_app_query_db_fetchall_module3():
    pass

@pytest.mark.app_query_db_one
def test_app_query_db_one_module3():
    pass

@pytest.mark.app_close_connection
def test_app_close_connection_module3():
    pass

@pytest.mark.app_close_connection_decorator
def test_app_close_connection_decorator_module3():
    pass
