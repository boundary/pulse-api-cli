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
from boundary import AlarmList
from cli_runner import CLIRunner
from cli_test import CLITest


class AlarmListTest(TestCase):

    def setUp(self):
        self.cli = AlarmList()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_api_call(self):
        alarm_list = self.api.alarm_list()

        self.assertGreaterEqual(len(alarm_list), 1)
        for alarm in alarm_list:
            print(alarm)

    def test_list_alarm(self):
        runner_list = CLIRunner(AlarmList())

        create = runner_list.get_output([])
        result_list = json.loads(create)
        alarm_list = result_list['result']

        self.assertGreaterEqual(len(alarm_list), 1)

