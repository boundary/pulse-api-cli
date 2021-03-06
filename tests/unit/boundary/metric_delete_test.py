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

from boundary import MetricCreate
from boundary import MetricDelete
from cli_runner import CLIRunner
from cli_test import CLITest


class MetricDeleteTest(TestCase):
    def setUp(self):
        self.cli = MetricDelete()

    def test_get_description(self):
        CLITest.check_description(self, self.cli)

    def test_get_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_curl(self):
        runner = CLIRunner(self.cli)

        metric = 'FOO'
        curl = runner.get_output(['-n', metric,
                                  '-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_delete_metric(self):
        runner_create = CLIRunner(MetricCreate())
        metric_name = 'METRIC' + CLITest.random_string(6)
        display_name = 'Display Name ' + CLITest.random_string(20)
        display_name_short = 'Short Display Name' + CLITest.random_string(5)
        description = CLITest.random_string(30)
        aggregate = 'avg'
        unit = 'number'
        resolution = 60000
        disabled = False

        create = runner_create.get_output(['-n', metric_name,
                                           '-d', display_name,
                                           '-s', display_name_short,
                                           '-i', description,
                                           '-g', aggregate,
                                           '-r', str(resolution),
                                           '-u', unit,
                                           '-x', str(disabled).lower()])
        metric_create = json.loads(create)
        metric = metric_create['result']

        runner_delete = CLIRunner(MetricDelete())
        delete = runner_delete.get_output(['-n', metric_name])
