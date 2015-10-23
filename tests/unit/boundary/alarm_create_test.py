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

from unittest import TestCase
from boundary import AlarmCreate
from boundary import API
from cli_test import CLITest


class AlarmCreateTest(TestCase):

    def setUp(self):
        self.cli = AlarmCreate()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_api_call(self):
        name = 'ALARM_TEST'
        metric_name = 'CPU'
        interval = '1 minute'
        aggregate = 'sum'
        operation = 'gt'
        threshold = '0.80'
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


