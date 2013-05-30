# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

from version import get_version

setup(name='gs.content.js.autocomplete',
      version=get_version(),
      description="Autocomplete in GroupServer",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='form type-ahead autocomplete javascript groupserver',
      author='Michael JasonSmith',
      author_email='mpj17@onlinegroups.net',
      url='http://www.groupserver.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gs'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'gs.content.css',
          'gs.content.form',
          'gs.content.js.jquery.base',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
