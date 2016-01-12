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

from cli_test import CLITest
from cli_runner import CLIRunner
from boundary import AlarmCreate
from boundary import AlarmDelete
from boundary import AlarmSearch


class AlarmSearchTest(TestCase):

    def setUp(self):
        self.cli = AlarmSearch()

    def test_get_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_curl(self):
        runner = CLIRunner(self.cli)

        curl = runner.get_output(['-n', 'foo',
                                  '-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_search_alarm(self):
        alarm_name = 'alarm_test' + CLITest.random_string(6)
        metric_name = 'CPU'
        aggregate = 'max'
        op = 'gt'
        value = 0.50
        interval = '5 minutes'
        note = CLITest.random_string(20)
        enabled = True
        runner_create = CLIRunner(AlarmCreate())

        create = runner_create.get_output(['-n', alarm_name,
                                           '-m', metric_name,
                                           '-g', aggregate,
                                           '-o', op,
                                           '-v', str(value),
                                           '-r', interval,
                                           '-d', note,
                                           '-x', str(enabled).lower()])

        runner_search = CLIRunner(AlarmSearch())
        search = runner_search.get_output(['-n', alarm_name])
        result_search = json.loads(search)
        alarm = result_search['result'][0]
        self.assertEqual(int(300), alarm['interval'])
        self.assertItemsEqual([], alarm['actions'])
        self.assertEqual(1, int(alarm['familyId']))
        self.assertFalse(False, alarm['isDisabled'])
        self.assertEqual(metric_name, alarm['metricName'])
        self.assertEqual(alarm_name, alarm['name'])
        self.assertTrue(alarm['perHostNotify'])
        self.assertEqual(aggregate, alarm['triggerPredicate']['agg'])
        self.assertEqual(op, alarm['triggerPredicate']['op'])
        self.assertEqual(value, alarm['triggerPredicate']['val'])
        self.assertEqual(3, int(alarm['typeId']))

        runner_delete = CLIRunner(AlarmDelete())
        delete = runner_delete.get_output(['-i', str(alarm['id'])])
