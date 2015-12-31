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

from boundary import MetricGet
from cli_runner import CLIRunner
from cli_test import CLITest


class MetricGetTest(TestCase):

    def setUp(self):
        self.cli = MetricGet()

    def test_get_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_get_metric(self):
        runner_create = CLIRunner(MetricGet())

        get = runner_create.get_output(['-n', 'CPU'])
        metric_get = json.loads(get)

        self.assertEqual('CPU', metric_get['name'])
        self.assertEqual('CPU Utilization', metric_get['displayName'])
        self.assertTrue(True, metric_get['isBuiltin'])
