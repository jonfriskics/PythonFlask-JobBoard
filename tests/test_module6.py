import pytest
import sys

from jobs import app

@pytest.mark.employer_template
def test_employer_template():
    pass

@pytest.mark.employer_template_details
def test_employer_template_details():
    pass

@pytest.mark.employer_template_all_jobs
def test_employer_template_all_jobs():
    pass

@pytest.mark.employer_template_reviews
def test_employer_template_reviews():
    pass

@pytest.mark.employer_template_review_stars
def test_employer_template_review_stars():
    pass

@pytest.mark.employer_template_review_details
def test_employer_template_review_details():
    pass

@pytest.mark.app_employer_route
def test_app_employer_route():
    pass

@pytest.mark.app_employer_route_employers
def test_app_employer_route_employers():
    pass

@pytest.mark.app_employer_route_jobs
def test_app_employer_route_jobs():
    pass

@pytest.mark.app_employer_route_reviews
def test_app_employer_route_reviews():
    pass
