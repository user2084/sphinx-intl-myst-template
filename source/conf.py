# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Another Sphinx Template'
copyright = '2023, AuthorName'
author = 'AuthorName'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []

source_suffix = ['.rst', '.md']
master_doc = 'index'

extensions = [
    "myst_parser",
    "rst2pdf.pdfbuilder"
]

# -- MyST --------------------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "dollarmath",
#    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
#    "smartquotes",
#    "replacements",
#    "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]

# to make attrs_inline work without warning (example: image in intro.md)
suppress_warnings = ["myst.directive_parse"]

# myst_url_schemes = {
#     "http": None,
#     "https": None,
#     "mailto": None,
#     "ftp": None,
#     "wiki": "https://en.wikipedia.org/wiki/{{path}}#{{fragment}}",
#     "doi": "https://doi.org/{{path}}"
# }
# myst_number_code_blocks = ["typescript"]
# myst_heading_anchors = 2
# myst_footnote_transition = True
# myst_dmath_double_inline = True

myst_enable_checkboxes = True

# myst_substitutions = {
#     "role": "[role](#syntax/roles)",
#     "directive": "[directive](#syntax/directives)",
# }

# -- sphinx-intl configuration -----------------------------------------------

locale_dirs = ['./locale']
gettext_compact = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# html_logo = "_static/logo-wide.svg"
# html_favicon = "_static/logo-square.svg"
html_title = ""
html_theme_options = {
#    "home_page_in_toc": True,
#    "github_url": "https://github.com/executablebooks/MyST-Parser",
#    "repository_url": "https://github.com/executablebooks/MyST-Parser",
#    "repository_branch": "master",
#    "path_to_docs": "docs",
#    "use_repository_button": True,
#    "use_edit_page_button": True,
#    "use_issues_button": True,
#    "announcement": "<b>WIP:</b> This site is still work in progress",
}
html_last_updated_fmt = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_css_files = ["local.css"]


# -- Options for LATEXPDF output --------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#latex-options

# latex_documents = [
#  ('index', 'yourdoc.tex', u'DocName', u'YourName', 'manual'),
# ]

# pdf_documents = [('index', u'documentation', 'My Docs', u'Me'), ]

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
        \renewcommand{\baselinestretch}{0.75}
        \pagestyle{plain}
        \thispagestyle{plain}
    ''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# DocClass for LaTeX builder
# latex_docclass = {
#     'manual': 'jsbook',
#     'howto': 'jsarticle'
# }
