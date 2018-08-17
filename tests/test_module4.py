import pytest
import sys

from jobs import app

@pytest.mark.template_macros
def test_template_macros_module4():
    pass

@pytest.mark.show_job_macro_definition
def test_show_job_macro_definition_module4():
    pass

@pytest.mark.show_job_macro_html
def test_show_job_macro_html_module4():
    pass

@pytest.mark.show_job_macro_header
def test_show_job_macro_header_module4():
    pass

@pytest.mark.show_job_macro_body
def test_show_job_macro_body_module4():
    pass

@pytest.mark.show_jobs_macro_definition
def test_show_jobs_macro_definition_module4():
    pass

@pytest.mark.show_jobs_macro_for_loop
def test_show_jobs_macro_for_loop_module4():
    pass

@pytest.mark.show_jobs_macro_for_loop_body
def test_show_jobs_macro_for_loop_body_module4():
    pass

@pytest.mark.import_macros
def test_import_macros_module4():
    pass

@pytest.mark.index_template
def test_index_template_module4():
    pass

@pytest.mark.display_all_jobs
def test_display_all_jobs_module4():
    pass

@pytest.mark.app_jobs_route_jobs
def test_app_jobs_route_jobs_module4():
    pass
