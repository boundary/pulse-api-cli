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
from boundary import HostgroupList
from cli_test import CLITest
from cli_runner import CLIRunner


class HostgroupListTest(TestCase):

    def setUp(self):
        self.cli = HostgroupList()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_list_hostgroup(self):
        runner_list = CLIRunner(HostgroupList())
        list = runner_list.get_output([])
        hostgroup_list = json.loads(list)

        self.assertGreaterEqual(1, len(hostgroup_list))

