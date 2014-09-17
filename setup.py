# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

from version import get_version

setup(name='gs.content.js.autocomplete',
      version=get_version(),
      description="Autocomplete in GroupServer",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='form type-ahead autocomplete javascript groupserver',
      author='Michael JasonSmith',
      author_email='mpj17@onlinegroups.net',
      url='http://source.iopen.net/groupserver/gs.content.js.autocomplete/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gs', 'gs.content', 'gs.content.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.browserresource',
          'gs.content.css',
          'gs.content.js.jquery.base',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
