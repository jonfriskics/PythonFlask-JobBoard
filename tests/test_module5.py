import pytest
import sys

from jobs import app
from .utils import *

@pytest.mark.app_job_template
def test_app_job_template_module5():
    assert template_exists('job'), 'The `job.html` template does not exist in the `templates` folder.'
    assert 'layout.html' in template_extends('job'), 'The `job.html` template does not extend `layout.html`.'
    assert 'content' in template_block('job'), 'Have you added a template `block` called `content`?'
    assert 'show_job:job' in template_functions('job', 'show_job'), 'Have you call the `show_job` macro in the `job.html` file?'

@pytest.mark.app_job_route
def test_app_job_route_module5():
    assert 'job' in dir(app), 'Have you created the `job` function?'
    result = [item for item in get_functions(app.job) if item.startswith('render_template:job.html')]
    assert len(result) == 1, 'Have you called the `render_template` function.'

@pytest.mark.app_job_route_decorator
def test_app_job_route_decorator_module5():
    assert 'job' in dir(app), 'Have you created the `job` function?'
    assert 'route:/job/<job_id>' in get_functions(app.job)

@pytest.mark.app_job_route_parameter
def test_app_job_route_parameter_module5():
    assert 'job' in dir(app), 'Have you created the `job` function?'
    assert 'job_id' in inspect.getfullargspec(app.job).args, 'Have you added the correct parameters to the `job` function parameters list?'

@pytest.mark.app_job_route_data
def test_app_job_route_data_module5():
    assert 'job' in dir(app), 'Have you created the `job` function?'
    query_db = 'query_db:SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id WHERE job.id = ?:job_id:True'
    assert query_db in get_functions(app.job), '`query_db` has not been called or has the wrong parameters.'

@pytest.mark.app_job_route_pass_data
def test_app_job_route_pass_data_module5():
    assert 'job' in dir(app), 'Have you created the `job` function?'
    assert 'render_template:job.html:job:job' in get_functions(app.job), 'Have you added `job` to the `render_template` call.'
