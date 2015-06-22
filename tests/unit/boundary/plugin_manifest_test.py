#!/usr/bin/env python
#
# Copyright 2014-2015 Boundary, Inc.
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

from boundary import PluginManifest

class TestPluginManifest(unittest.TestCase):

    def setUp(self):
        self.pm = PluginManifest('../../../plugin.json')
        self.pm.load()

    def test_load(self):
        pm = PluginManifest('../../../plugin.json')
        pm.load()

    def test_check_data_members(self):
        self.assertEqual('Boundary README Test', self.pm.name,
                         'Check for name')
        self.assertEqual('Example plugin.json for testing README.md generation', self.pm.description, 'Check for description')
        self.assertEqual('2.0', self.pm.version)
        self.assertEqual('meter', self.pm.tags)
        self.assertEqual('icon.png', self.pm.icon)
        self.assertEqual('node index.js', self.pm.command)
        self.assertEqual('boundary-meter init.lua', self.pm.command_lua)
        self.assertEqual('npm install', self.pm.post_extract)
        self.assertEqual('', self.pm.post_extract_lua)
        self.assertEqual('node_modules', self.pm.ignore)
        self.assertEqual(['BOUNDARY_README_METRIC'], self.pm.metrics)

    def test_check_for_param_array(self):

        a = self.pm.param_array

        self.assertTrue(a is not None)

    def test_check_param_array(self):
        pass

  # "paramArray": {
  #   "itemTitle": [
  #     "parameter_a",
  #     "parameter_b",
  #     "parameter_c"
  #   ],
  #   "schemaTitle": "Configuration"
  # },