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
import json
from boundary import API
from boundary import AlarmCreate
from boundary import AlarmDelete
from cli_test import CLITest
from cli_runner import CLIRunner


class AlarmDeleteTest(TestCase):

    def setUp(self):
        self.cli = AlarmDelete()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_curl(self):
        runner = CLIRunner(self.cli)

        alarm_id = 1024

        curl = runner.get_output(['-i', str(alarm_id),
                                  '-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_api_call(self):
        api = API()
        name = 'ALARM_DELETE_API_TEST' + CLITest.random_string(6)
        metric_name = 'CPU'
        interval = '1 minute'
        aggregate = 'sum'
        operation = 'gt'
        threshold = '0.80'
        note = CLITest.random_string(20)
        alarm = api.alarm_create(name=name,
                                 metric_name=metric_name,
                                 interval=interval,
                                 aggregate=aggregate,
                                 operation=operation,
                                 threshold=threshold,
                                 note=note)

        self.api.alarm_delete(id=alarm.id)

    def test_delete_alarm(self):
        name = 'ALARM_DELETE_TEST' + CLITest.random_string(6)
        metric_name = 'CPU'
        interval = '1 minute'
        aggregate = 'sum'
        operation = 'gt'
        threshold = '0.80'
        note = CLITest.random_string(20)

        runner_create = CLIRunner(AlarmCreate())
        create = runner_create.get_output(['-n', name,
                                           '-m', metric_name,
                                           '-g', aggregate,
                                           '-o', operation,
                                           '-v', str(threshold),
                                           '-r', interval,
                                           '-d', note])
        result_create = json.loads(create)
        alarm = result_create['result']

        runner_delete = CLIRunner(AlarmDelete())
        delete = runner_delete.get_output(['-i', str(alarm['id'])])


