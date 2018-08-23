import pytest

from jobs import app
from .utils import *

values = template_values('layout', 'url_for')

@pytest.mark.layout_template
def test_layout_template_module2():
    assert template_exists('layout'), 'The `layout.html` template does not exist in the `templates` folder.'

@pytest.mark.add_bulma_css_framework
def test_add_bulma_css_framework_module2():
    assert template_exists('layout'), 'The `layout.html` template does not exist in the `templates` folder.'
    assert 'static:filename:css/bulma.min.css' in values, 'Looks like `bulma.min.css` is not linked in `layout.html`.'

@pytest.mark.add_custom_css
def test_add_custom_css_module2():
    assert template_exists('layout'), 'The `layout.html` template does not exist in the `templates` folder.'
    assert 'static:filename:css/app.css' in values, 'Looks like `app.css` is not linked in `layout.html`.'

@pytest.mark.add_fontawesome
def test_add_fontawesome_module2():
    assert template_exists('layout'), 'The `layout.html` template does not exist in the `templates` folder.'
    attr = {
        'href': 'https://use.fontawesome.com/releases/v5.2.0/css/all.css',
        'rel': 'stylesheet'
    }
    assert template_doc('layout').find('link', attr), 'Looks like FontAwesome is not linked in `layout.html`.'

@pytest.mark.extend_base_template
def test_extend_base_template_module2():
    assert template_exists('index'), 'The `index.html` template does not exist in the `templates` folder.'
    assert template_exists('layout'), 'The `layout.html` template does not exist in the `templates` folder.'
    assert 'layout.html' in template_extends('index'), 'The `index.html` template does not extend `layout.html`.'
