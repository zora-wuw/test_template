# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Name of the Tutorial'
copyright = '2024, National Computational Infrastructure'
author = 'Name of the author'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'

# furo logo
html_static_path = ["_static"]
html_theme_options = {
    "source_repository": "https://github.com/zora-wuw/test_template",
    "source_branch": "main",
    "source_directory": "docs/source",
    "top_of_page_buttons": ["view"],
    "light_logo": "logo-light.png",
    "dark_logo": "logo-dark.png",
    "light_css_variables": {
        "color-brand-primary": "#324159",
        "color-brand-content": "#57b0f2",
    },
    "dark_css_variables": {
        "color-brand-primary": "#b6c0d1",  
        "color-brand-content": "#57b0f2", 
    },
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
