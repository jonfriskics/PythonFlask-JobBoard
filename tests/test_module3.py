import pytest
import sys

from jobs import app

@pytest.mark.app_import_sqlite
def test_app_import_sqlite_module3():
    pass

@pytest.mark.app_import_g
def test_app_import_g_module3():
    pass

@pytest.mark.app_db_path
def test_app_db_path_module3():
    pass

@pytest.mark.app_get_db_get_attribute
def test_app_get_db_get_attribute_module3():
    pass

@pytest.mark.app_get_db_connection
def test_app_get_db_connection_module3():
    pass

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
