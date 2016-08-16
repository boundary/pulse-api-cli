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

from boundary import API
from boundary import AlarmCreate
from boundary import AlarmDelete
from cli_runner import CLIRunner
from cli_test import CLITest
from cli_test_parameters import CLITestParameters


class AlarmCreateTest(TestCase):
    def setUp(self):
        self.cli = AlarmCreate()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_curl(self):
        runner = CLIRunner(self.cli)

        alarm_name = 'my-curl'
        metric = 'CPU'
        aggregate = 'min'
        operation = 'lt'
        value = 0.5
        trigger_interval = 300000
        enabled = False

        curl = runner.get_output(['-n', alarm_name,
                                  '-m', metric,
                                  '-g', aggregate,
                                  '-o', operation,
                                  '-v', str(value),
                                  '-r', str(trigger_interval),
                                  '-x', str(enabled).lower(),
                                  '-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_api_call(self):
        name = 'ALARM_CREATE_TEST' + CLITest.random_string(6)
        metric = 'CPU'
        trigger_interval = 60000
        aggregate = 'sum'
        operation = 'gt'
        threshold = 0.80
        alarm = self.api.alarm_create(name=name,
                                      metric=metric,
                                      trigger_interval=trigger_interval,
                                      aggregate=aggregate,
                                      operation=operation,
                                      threshold=threshold)

        self.assertEqual(name, alarm.name)
        self.assertEqual(metric, alarm.metric)
        self.assertEqual(trigger_interval, alarm.trigger_interval)
        self.assertEqual(aggregate, alarm.aggregate)
        self.assertEqual(operation, alarm.operation)
        self.assertEqual(threshold, alarm.threshold)

        self.api.alarm_delete(id=alarm.id)

    def test_credentials(self):
        parameters = CLITestParameters(filename='credentials.json')
        api_host = parameters.get_value('api-host', 'value')
        email = parameters.get_value('email', 'value')
        api_token = parameters.get_value('api-token', 'value')

        api = API(api_host=api_host, email=email, api_token=api_token)

        name = 'ALARM_CREDS_TEST' + CLITest.random_string(6)
        metric = 'CPU'
        trigger_interval = 900000
        aggregate = 'sum'
        operation = 'gt'
        threshold = 0.80
        alarm = api.alarm_create(name=name,
                                 metric=metric,
                                 trigger_interval=trigger_interval,
                                 aggregate=aggregate,
                                 operation=operation,
                                 threshold=threshold)

        self.assertEqual(name, alarm.name)
        self.assertEqual(metric, alarm.metric)
        self.assertEqual(trigger_interval, alarm.trigger_interval)
        self.assertEqual(aggregate, alarm.aggregate)
        self.assertEqual(operation, alarm.operation)
        self.assertEqual(threshold, alarm.threshold)

        api.alarm_delete(id=alarm.id)

    def test_create_alarm(self):
        runner_create = CLIRunner(AlarmCreate())

        alarm_name = 'my-alarm' + CLITest.random_string(6)
        trigger_interval = 300000

        create = runner_create.get_output(['-n', alarm_name,
                                           '-m', 'CPU',
                                           '-g', 'max',
                                           '-o', 'gt',
                                           '-v', '0.50',
                                           '-r', str(trigger_interval)])
        alarm = json.loads(create)
        self.assertEqual(trigger_interval, int(alarm['triggerInterval']))
        self.assertEqual([], alarm['actions'])
        self.assertEqual(1, int(alarm['familyId']))
        self.assertFalse(alarm['isDisabled'])
        self.assertEqual('CPU', alarm['metric'])
        self.assertEqual(alarm_name, alarm['name'])
        self.assertTrue(alarm['perHostNotify'])
        self.assertTrue(alarm['notifyClear'])
        self.assertTrue(alarm['notifySet'])
        self.assertEqual('max', alarm['triggerPredicate']['agg'])
        self.assertEqual('gt', alarm['triggerPredicate']['op'])
        self.assertEqual(0.5, alarm['triggerPredicate']['val'])
        self.assertEqual(3, int(alarm['typeId']))

        self.api.alarm_delete(id=alarm['id'])


