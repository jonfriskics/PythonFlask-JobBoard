import pytest
import sys

from jobs import app

@pytest.mark.app_review_route
def test_app_review_route():
    pass

@pytest.mark.app_review_post_request_check
def test_app_review_post_request_check():
    pass

@pytest.mark.app_review_insert_review
def test_app_review_insert_review():
    pass

@pytest.mark.review_form_cancel
def test_review_form_cancel():
    pass
