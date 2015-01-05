#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

#
# Copyright 2014 Tuenti Technologies S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys, os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import pyflapjackevents

from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)



setup(name='pyflapjackevents',
      version=pyflapjackevents.__version__,
      description="Send status events to flapjack from python.",
      long_description=file('README.rst').read(),
      classifiers=[],
      keywords='',
      author='Jose Plana',
      author_email='jplana@tuenti.com',
      url='http://github.com/tuenti/pyflapjackevents',
      license='Apache License, Version 2.0',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # requirements
      ],
      test_requires=[
          'pytest',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      cmdclass = {'test': PyTest},
      )
