# -*- coding: utf-8 -*-

import sys, os

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, '../../../src'))

import django_reservation
version = django_reservation.VERSION
release = django_reservation.RELEASE
project = django_reservation.PROJECT
copyright = django_reservation.COPYRIGHT
author = django_reservation.AUTHOR


# Source
master_doc = 'index'
templates_path = ['_templates']
source_suffix = '.rst'
exclude_trees = []
pygments_style = 'sphinx'

# html build settings
html_theme = 'default'
html_static_path = ['_static']

# htmlhelp settings
htmlhelp_basename = '%sdoc' %project

# latex build settings
latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project,
    author, 'manual'),
]
