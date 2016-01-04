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
from string import split
from unittest import TestCase

from boundary import HostgroupCreate
from boundary import HostgroupDelete
from cli_runner import CLIRunner
from cli_test import CLITest


class HostgroupCreateTest(TestCase):

    def setUp(self):
        self.cli = HostgroupCreate()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_filter(self):
        runner_create = CLIRunner(HostgroupCreate())
        filter_name = 'Filter' + CLITest.random_string(6)
        sources = 'foo,bar,red,green'

        create = runner_create.get_output(['-n', filter_name,
                                           '-s', sources])
        filter_create = json.loads(create)
        filter = filter_create['result']

        self.assertEqual(filter_name, filter['name'])
        self.assertItemsEqual(split(sources, ','), filter['hostnames'])

        filter_id = filter['id']

        runner_delete = CLIRunner(HostgroupDelete())
        delete = runner_delete.get_output(['-i', str(filter_id)])
        delete_result = json.loads(delete)
        self.assertTrue(delete_result['result']['success'])

