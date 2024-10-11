# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VaGv_info_indus_tutorial'
copyright = '2024, aRTHUR vARLET, vALENTIN GIRARDET'
author = 'aRTHUR vARLET, vALENTIN GIRARDET'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.graphviz",

    "sphinx.ext.ifconfig",

    "sphinx.ext.intersphinx",

    "sphinx_copybutton",

    "sphinx_tabs.tabs",

    "sphinx_rtd_theme",

    "myst_parser",
    ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for

# a list of builtin themes.

#

html_theme = 'sphinx_rtd_theme'


# -- Options for copybutton extension ----------------------------------------

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "

copybutton_prompt_is_regexp = True


# Add any paths that contain custom static files (such as style sheets) here,

# relative to this directory. They are copied after the builtin static files,

# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']


html_css_files = [

    "css/custom.css",

]

