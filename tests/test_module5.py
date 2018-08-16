import pytest
import sys

from jobs import app

@pytest.mark.app_job_template
def test_app_job_template():
    pass

@pytest.mark.app_job_route
def test_app_job_route():
    pass

@pytest.mark.app_job_route_decorator
def test_app_job_route_decorator():
    pass

@pytest.mark.app_job_route_parameter
def test_app_job_route_parameter():
    pass

@pytest.mark.app_job_route_data
def test_app_job_route_data():
    pass

@pytest.mark.app_job_route_pass_data
def test_app_job_route_pass_data():
    pass
