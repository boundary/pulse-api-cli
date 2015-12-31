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
from boundary import AlarmCreate
from boundary import API
from cli_test import CLITest
from cli_test_parameters import CLITestParameters
from cli_runner import CLIRunner
import json


class AlarmCreateTest(TestCase):
    def setUp(self):
        self.cli = AlarmCreate()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_api_call(self):
        name = 'ALARM_CREATE_TEST'
        metric_name = 'CPU'
        interval = '1 minute'
        aggregate = 'sum'
        operation = 'gt'
        threshold = 0.80
        alarm = self.api.alarm_create(name=name,
                                      metric_name=metric_name,
                                      interval=interval,
                                      aggregate=aggregate,
                                      operation=operation,
                                      threshold=threshold)

        self.assertEqual(name, alarm.name)
        self.assertEqual(metric_name, alarm.metric_name)
        self.assertEqual(60, alarm.interval)
        self.assertEqual(aggregate, alarm.aggregate)
        self.assertEqual(operation, alarm.operation)
        self.assertEqual(threshold, alarm.threshold)

    def test_credentials(self):
        parameters = CLITestParameters(filename='credentials.json')
        api_host = parameters.get_value('api-host', 'value')
        email = parameters.get_value('email', 'value')
        api_token = parameters.get_value('api-token', 'value')

        api = API(api_host=api_host, email=email, api_token=api_token)

        name = 'ALARM_CREDS_TEST'
        metric_name = 'CPU'
        interval = '1 minute'
        aggregate = 'sum'
        operation = 'gt'
        threshold = 0.80
        alarm = api.alarm_create(name=name,
                                 metric_name=metric_name,
                                 interval=interval,
                                 aggregate=aggregate,
                                 operation=operation,
                                 threshold=threshold)

        self.assertEqual(name, alarm.name)
        self.assertEqual(metric_name, alarm.metric_name)
        self.assertEqual(60, alarm.interval)
        self.assertEqual(aggregate, alarm.aggregate)
        self.assertEqual(operation, alarm.operation)
        self.assertEqual(threshold, alarm.threshold)

        api.alarm_delete(id=alarm.id)

    def test_create_alarm(self):
        runner = CLIRunner(AlarmCreate())

        output = runner.get_output(['-n', 'my-alarm', '-m', 'CPU', '-g', 'max', '-o', 'gt',
                                    '-v', '0.50', '-r', '5 minutes'])
        result = json.loads(output)
        alarm = result['result']
        self.assertEqual('CPU', alarm['metricName'])
