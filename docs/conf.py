# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'PyQtQuick_Project_Template'
copyright = '2025, Vo Linh Truc'
author = 'Bico'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.plantuml',
]

# Path to plantuml.jar
plantuml = 'java -jar {}'.format(os.path.join(os.path.dirname(__file__), 'plantuml/plantuml.jar'))
plantuml_output_format = 'svg'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
