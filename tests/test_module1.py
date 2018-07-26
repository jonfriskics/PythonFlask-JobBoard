import pytest
import sys
import pprint

from jobs import app

@pytest.mark.testing_import
def test_import():
    imports = ['os','Flask', 'sqlite3']
    types = [v + ':' + str(eval('type(app.' + v + ')')) for v in dir(app) if not v.startswith("__") and v not in imports]