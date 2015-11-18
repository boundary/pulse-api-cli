#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest import TestCase
from cli_test_parameters import CLITestParameters
import os.path


class CliTestParametersTest(TestCase):

    def setUp(self):
        self.test_parameters = CLITestParameters('test_parameter_test_data.json')

    def test_load(self):
        self.test_parameters.load()

    def test_lookup_foo(self):
        self.test_parameters.load()
        p = self.test_parameters.get('Foo')
        self.assertEqual(1, p['red'], 'check p.red')
        self.assertEqual("bar", p['green'])
        self.assertEqual(1, p['blue']['cyan'])
        self.assertEqual("foo", p['blue']['magenta'])
        self.assertEqual(100, p['blue']['yellow']['a'])

    def test_lookup_bar(self):
        self.test_parameters.load()
        p = self.test_parameters.get('Bar')
        self.assertEqual(2, p['red'], 'check p.red')
        self.assertEqual("FOO", p['green'])
        self.assertEqual(100, p['blue']['cyan'])
        self.assertEqual("BAR", p['blue']['magenta'])
        self.assertEqual(1000, p['blue']['yellow']['b'])

    def test_get_file_contents(self):
        contents = self.test_parameters.get_cli_help('UserGet')
        print(contents)


