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
import json
from unittest import TestCase

from boundary import PluginGet
from cli_runner import CLIRunner
from cli_test import CLITest


class PluginGetTest(TestCase):

    def setUp(self):
        self.cli = PluginGet()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_get_plugin(self):
        runner = CLIRunner(PluginGet())

        plugin_name = 'httpcheck'

        get = runner.get_output(['-n', plugin_name])
        plugin_get = json.loads(get)
        plugin = plugin_get['result']

        self.assertTrue('download' in plugin)
        self.assertTrue('repoUrl' in plugin)
        self.assertEqual(plugin_name, plugin['name'])
        self.assertTrue('description' in plugin)
        self.assertTrue('paramSchema' in plugin)
        self.assertTrue('paramArray' in plugin)
        self.assertTrue('postExtract' in plugin)
        self.assertTrue('command' in plugin)
        self.assertTrue('ignore' in plugin)
        self.assertTrue('icon' in plugin)
        self.assertTrue('dashboards' in plugin)
        self.assertTrue('version' in plugin)
        self.assertTrue('metrics' in plugin)
        self.assertTrue('metricDefinitions' in plugin)

