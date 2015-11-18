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
import unittest
from boundary.api_cli import ApiCli


class TestApiCli(unittest.TestCase):

    def setUp(self):
        self.a = ApiCli()

    def test_cli_description_set(self):
        with self.assertRaises(AttributeError):
            self.a.method = 'Mary Had a Little Lamb'

    def test_method_put(self):
        a = ApiCli()
        a.method = 'PUT'
        self.assertEquals(a.method, 'PUT', 'Check assignment of PUT to property method')

    def test_method_foo(self):
        with self.assertRaises(AttributeError, msg='Assign a value that is not in http method list'):
            self.a.method = 'FOO'

    def test_path_set(self):
        self.a.path = "v1/foobar"
        self.assertEqual(self.a.path, 'v1/foobar', 'Check assignment of path property')

if __name__ == '__main__':
    unittest.main()
