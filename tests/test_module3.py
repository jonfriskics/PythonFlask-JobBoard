import pytest
import inspect

from jobs import app
from .utils import *

@pytest.mark.app_import_sqlite
def test_app_import_sqlite_module3():
    assert 'sqlite3' in dir(app), 'Have you imported `sqlite`?'

@pytest.mark.app_import_g
def test_app_import_g_module3():
    assert 'g' in dir(app), 'Have you imported the `g` class from `flask`?'

@pytest.mark.app_db_path
def test_app_db_path_module3():
    assert 'DATABASE' in dir(app), 'Have you created a constant called `DATABASE`.'
    assert app.DATABASE == 'db/jobs.sqlite', 'Have you created a constant called `DATABASE`?'

@pytest.mark.app_get_db_get_attribute
def test_app_get_db_get_attribute_module3():
    assert 'get_db' in dir(app), 'Have you defined a function named `get_db`.'
    assert 'getattr:g:_database:None' in get_functions(app.get_db), 'Have you used the `getattr` function to get the global `_database`?'

@pytest.mark.app_get_db_connection
def test_app_get_db_connection_module3():
    assert 'g' in dir(app), 'Have you imported the `g` class from `flask`?'
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert 'get_db' in dir(app), 'Have you defined a function named `get_db`.'
    with app.app.app_context():
        app.get_db()
        assert hasattr(app.g, '_database'), 'Did you assign the `_database` attribute to `g`?'
        _, _, db_name = app.g._database.execute('PRAGMA database_list').fetchone()
        assert os.path.join(os.getcwd(), 'db', 'jobs.sqlite') == db_name, 'Did you pass the `connect` function the `DATABASE` constant?'

@pytest.mark.app_get_db_row_factory
def test_app_get_db_row_factory_module3():
    assert 'g' in dir(app), 'Have you imported the `g` class from `flask`?'
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert 'get_db' in dir(app), 'Have you defined a function named `get_db`.'
    with app.app.app_context():
        db = app.get_db()
        assert isinstance(db, app.sqlite3.Connection), 'Are you returning the database connection?'
        assert id(db.row_factory) == id(app.sqlite3.Row), 'Have you set the database `row_factory` to the sqlite3.Row class?'

@pytest.mark.app_query_db
def test_app_query_db_module3():
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert 'query_db' in dir(app), 'Have you defined a function named `query_db`.'
    assert 'get_db' in get_functions(app.query_db), 'Have you called the `get_db` function in `query_db`?'

@pytest.mark.app_query_db_parameters
def test_app_query_db_parameters_module3():
    assert 'query_db' in dir(app), 'Have you defined a function named `query_db`.'
    parameters = inspect.getfullargspec(app.query_db)
    assert parameters.args[0] == 'query' and parameters.args[1] == 'args' and parameters.args[2] == 'one', 'Have you added the correct parameters to the `query_db` function parameters list?'
    assert parameters.defaults[0] == () and parameters.defaults[1] == False, 'Do the `args` and `one` parameters have the correct defaults in the `query_db` function parameters list?'

@pytest.mark.app_query_db_execute
def test_app_query_db_execute_module3():
    assert 'query_db' in dir(app), 'Have you defined a function named `query_db`.'
    assert 'execute:query:args' in get_functions(app.query_db), 'Have you called the `execute` function in `query_db`?'

@pytest.mark.app_query_db_fetchall
def test_app_query_db_fetchall_module3():
    assert 'query_db' in dir(app), 'Have you defined a function named `query_db`.'
    assert 'fetchall' in get_functions(app.query_db), 'Have you called the `fetchall` function in `query_db`?'
    assert 'close' in get_functions(app.query_db), 'Have you called the `close` function in `query_db`?'

@pytest.mark.app_query_db_one
def test_app_query_db_one_module3():
    assert 'query_db' in dir(app), 'Have you defined a function named `query_db`.'
    with app.app.app_context():
        results = app.query_db('SELECT * FROM job', one=True)
        assert type(results) != list, 'Have you create an if statement to only return one result in `one` is true?'

@pytest.mark.app_close_connection
def test_app_close_connection_module3():
    assert 'close_connection' in dir(app), 'Have you defined a function named `close_connection`.'
    assert 'getattr:g:_database:None' in get_functions(app.get_db), 'Have you used the `getattr` function to get the global `_database`?'
    assert 'close' in get_functions(app.query_db), 'Have you called the `close` function in `query_db`?'

@pytest.mark.app_close_connection_decorator
def test_app_close_connection_decorator_module3():
    assert 'close_connection' in dir(app), 'Have you defined a function named `close_connection`.'
    decorator = get_decorators(app.close_connection)['close_connection'][0][0]
    assert decorator == 'teardown_appcontext', 'Does `close_connection` have a `teardown_appcontext` decorator?'