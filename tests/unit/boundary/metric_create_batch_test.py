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

import os
import json
from boundary import MetricCreateBatch
from boundary import MetricDelete
from metric_test import MetricTest
from boundary import MetricExport
from cli_test import CLITest
from cli_runner import CLIRunner


class MetricCreateBatchTest(TestCase):
    def setUp(self):
        self.cli = MetricCreateBatch()
        self.filename = os.path.join(os.path.dirname(__file__), 'metric_import_data.json')

    def test_get_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_metric_batch(self):
        filename = os.path.join(os.path.dirname(__file__), 'metric_import_data.json')
        print(filename)

        runner_create = CLIRunner(MetricCreateBatch())
        create = runner_create.get_output(['-f', filename])

        runner_export = CLIRunner(MetricExport())
        export = runner_export.get_output(['-p', 'TEST_METRIC_IMPORT'])
        metrics = json.loads(export)

        MetricTest.metric_assert(self,
                      metrics['TEST_METRIC_IMPORT_A'],
                      'My Number of Files',
                      'My Files',
                      'My Number Of Files',
                      'number',
                      'SUM',
                      2000,
                      False)

# runner_delete = CLIRunner(MetricDelete())
#        delete = runner_delete.get_output(['-n', metric_name])
