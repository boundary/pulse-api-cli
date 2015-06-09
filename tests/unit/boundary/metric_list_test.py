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
import unittest
from mock import Mock, patch
import sys
from boundary.metric_list import MetricList
from io import TextIOWrapper, BytesIO
import json
import StringIO


class TestMetricList(unittest.TestCase):

    def setUp(self):
        self.metric_list = MetricList()
        self.text = '''
        {
        "result": [
                    {
                     "name": "BOUNDARY_MOCK_METRIC",
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

        # setup the environment
        self.old_stdout = sys.stdout
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
        sys.stdout = StringIO.StringIO()

    def tearDown(self):
        # restore stdout
        sys.stdout.close()
        sys.stdout = self.old_stdout

    def test_cli_description(self):
        self.assertEqual(self.metric_list.cli_description, 'Lists the defined metrics in a Boundary account')

    def test_mock_arguments(self):
        pass
        # sys.argv = ['metric-list', '-l', 'debug']
        # self.metric_list.execute();

    @patch('boundary.api_cli.requests')
    def test_execute(self, mock_requests):
        sys.argv = ['metric-list']
        self.maxDiff = None

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = self.text

        mock_requests.get.return_value = mock_response
        self.metric_list.execute()

        # get output
        sys.stdout.seek(0)      # jump to the start
        self.out = sys.stdout.read() # read output
        json1 = json.load(self.out)
        json2 = json.load(self.text)
        self.assertDictEqual(json1, json2)
