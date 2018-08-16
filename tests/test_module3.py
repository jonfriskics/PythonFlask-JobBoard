import pytest
import sys

from jobs import app

@pytest.mark.app_import_sqlite
def test_app_import_sqlite():
    pass

@pytest.mark.app_import_g
def test_app_import_g():
    pass

@pytest.mark.app_db_path
def test_app_db_path():
    pass

@pytest.mark.app_get_db_get_attribute
def test_app_get_db_get_attribute():
    pass

@pytest.mark.app_get_db_connection
def test_app_get_db_connection():
    pass

@pytest.mark.app_get_db_row_factory
def test_app_get_db_row_factory():
    pass

@pytest.mark.app_query_db
def test_app_query_db():
    pass

@pytest.mark.app_query_db_parameters
def test_app_query_db_parameters():
    pass

@pytest.mark.app_query_db_execute
def test_app_query_db_execute():
    pass

@pytest.mark.app_query_db_fetchall
def test_app_query_db_fetchall():
    pass

@pytest.mark.app_query_db_one
def test_app_query_db_one():
    pass

@pytest.mark.app_close_connection
def test_app_close_connection():
    pass

@pytest.mark.app_close_connection_decorator
def test_app_close_connection_decorator():
    pass
