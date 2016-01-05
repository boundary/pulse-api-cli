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

from boundary import AlarmGet
from boundary import AlarmCreate
from boundary import AlarmDelete
from boundary import API
from cli_test import CLITest
from cli_runner import CLIRunner
import json


class AlarmGetTest(TestCase):
    def setUp(self):
        self.cli = AlarmGet()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_api_call(self):
        self.api = API()
        name = 'ALARM_GET_TEST'
        metric_name = 'CPU'
        interval = '1 minute'
        aggregate = 'sum'
        operation = 'gt'
        threshold = '0.80'
        alarm_create = self.api.alarm_create(name=name,
                                             metric_name=metric_name,
                                             interval=interval,
                                             aggregate=aggregate,
                                             operation=operation,
                                             threshold=threshold)

        alarm_get = self.api.alarm_get(id=alarm_create.id)

        self.assertEqual(alarm_create.id, alarm_get.id)
        self.assertEqual(alarm_create.name, alarm_get.name)
        self.assertEqual(alarm_create.metric_name, alarm_get.metric_name)
        self.assertEqual(alarm_create.interval, alarm_get.interval)
        self.assertEqual(alarm_create.aggregate, alarm_get.aggregate)
        self.assertEqual(alarm_create.operation, alarm_get.operation)
        self.assertEqual(alarm_create.threshold, alarm_get.threshold)

    def test_get_alarm(self):
        runner_create = CLIRunner(AlarmCreate())

        create = runner_create.get_output(['-n', 'my-alarm', '-m', 'CPU', '-g', 'max', '-o', 'gt',
                                    '-v', '0.50', '-r', '5 minutes'])
        result_create = json.loads(create)
        alarm_create = result_create['result']

        runner_get = CLIRunner(AlarmGet())
        get = runner_get.get_output(['-i', str(alarm_create['id'])])
        result_get = json.loads(get)
        alarm_get = result_get['result']

        self.assertEqual(int(alarm_create['interval']), alarm_get['interval'])
        self.assertEqual(alarm_create['actions'], alarm_get['actions'])
        self.assertEqual(int(alarm_create['familyId']), int(alarm_get['familyId']))
        self.assertFalse(alarm_create['isDisabled'], alarm_get['isDisabled'])
        self.assertEqual(alarm_create['metricName'], alarm_get['metricName'])
        self.assertEqual(alarm_create['name'], alarm_get['name'])
        self.assertTrue(alarm_get['perHostNotify'])
        self.assertEqual(alarm_create['triggerPredicate']['agg'], alarm_get['triggerPredicate']['agg'])
        self.assertEqual(alarm_create['triggerPredicate']['op'], alarm_get['triggerPredicate']['op'])
        self.assertEqual(alarm_create['triggerPredicate']['val'], alarm_get['triggerPredicate']['val'])
        self.assertEqual(int(alarm_create['typeId']), int(alarm_get['typeId']))

        runner_delete = CLIRunner(AlarmDelete())
        delete = runner_delete.get_output(['-i', str(alarm_get['id'])])

