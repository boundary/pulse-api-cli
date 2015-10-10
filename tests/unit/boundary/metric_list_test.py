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
from mock import Mock, patch
import sys
from boundary.metric_list import MetricList
from io import TextIOWrapper, BytesIO
import json
import StringIO
from cli_test import CLITest


class MetricListTest(TestCase):

    def setUp(self):
        self.cli = MetricList()
        self.text = '''
        {
        "result": [ { "name": "BOUNDARY_MOCK_METRIC",
                     "defaultAggregate": "AVG",
                     "defaultResolutionMS": 1000,
                     "description": "BOUNDARY_MOCK_METRIC",
                     "displayName": "BOUNDARY_MOCK_METRIC",
                     "displayNameShort": "BOUNDARY_MOCK_METRIC",
                     "unit": "number",
                     "isDisabled": false,
                     "isBuiltin": false
                    }
                  ]
        }
        '''

        self.out = None
        self.json1 = None
        self.json2 = None
        # setup the environment
        self.old_stdout = sys.stdout
        sys.stdout = TextIOWrapper(BytesIO(), 'utf-8')
        sys.stdout = StringIO.StringIO()

    def tearDown(self):
        # restore stdout
        sys.stdout.close()
        sys.stdout = self.old_stdout
#        print("self.out: " + str(self.out))
#        print("self.json1: " + str(self.json1))
#        print("self.text: " + str(self.text))
#        print("self.json2: " + str(self.json2))

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_mock_arguments(self):
        pass
        # sys.argv = ['metric-list', '-l', 'debug']
        # self.metric_list.execute();

#   @patch('boundary.api_cli.requests')
#   def test_execute(self, mock_requests):
#       sys.argv = ['metric-list']
#       self.maxDiff = None

#       mock_response = Mock()
#       mock_response.status_code = 200
#       mock_response.text = self.text

#       mock_requests.get.return_value = mock_response
#       self.cli.execute()

#       # get output
#       sys.stdout.seek(0)      # jump to the start
#       self.out = sys.stdout.read()  # read output
#       self.json1 = json.loads(self.out)
#       self.json2 = json.loads(self.text)
#       self.assertDictEqual(self.json1, self.json2)
