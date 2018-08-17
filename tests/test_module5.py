import pytest
import sys

from jobs import app

@pytest.mark.app_job_template
def test_app_job_template_module5():
    pass

@pytest.mark.app_job_route
def test_app_job_route_module5():
    pass

@pytest.mark.app_job_route_decorator
def test_app_job_route_decorator_module5():
    pass

@pytest.mark.app_job_route_parameter
def test_app_job_route_parameter_module5():
    pass

@pytest.mark.app_job_route_data
def test_app_job_route_data_module5():
    pass

@pytest.mark.app_job_route_pass_data
def test_app_job_route_pass_data_module5():
    pass
