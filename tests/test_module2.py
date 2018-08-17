import pytest
import sys

from jobs import app

@pytest.mark.layout_template
def test_layout_template_module2():
    pass

@pytest.mark.add_bulma_css_framework
def test_add_bulma_css_framework_module2():
    pass

@pytest.mark.add_custom_css
def test_add_custom_css_module2():
    pass

@pytest.mark.add_fontawesome
def test_add_fontawesome_module2():
    pass

@pytest.mark.extend_base_template
def test_extend_base_template_module2():
    pass