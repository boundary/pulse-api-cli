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
from boundary import API
from cli_test import CLITest


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

