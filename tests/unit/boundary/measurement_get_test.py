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

import unittest
import datetime
import json
from boundary import MeasurementGet
from cli_test import CLITest


class MeasurementGetTest(unittest.TestCase):

    def setUp(self):
        self.mg = MeasurementGet()
        self.now = datetime.datetime.now()
        self.now_epoch = self.now.strftime("%s")
        self.cli = MeasurementGet()

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    # def test_parse_datetime(self):
    #     out = self.mg.parse_time_date('2015-06-10')
    #     print(out)
    #     print(out.strftime("%s"))
    #     out = self.mg.parse_time_date(out.strftime("%s"))
    #     print(out)

    def test_datetime_to_json(self):
        j = {}

        j['start'] =self.now.strftime('%s')
        out = json.dumps(j)
        print(out)
        out = self.mg.parse_time_date(self.now.strftime("%s"))
        print(out.strftime("%s"))
        print(self.now_epoch)

