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

from boundary import HostgroupCreate
from boundary import HostgroupDelete
from boundary import HostgroupGet
from cli_runner import CLIRunner
from cli_test import CLITest


class HostgroupGetTest(TestCase):

    def setUp(self):
        self.cli = HostgroupGet()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_hostgroup(self):
        runner_create = CLIRunner(HostgroupCreate())

        hostgroup_name = 'SAMPLE' + CLITest.random_string(6)

        create = runner_create.get_output(['-n', hostgroup_name,
                                           '-s', 'FOO,BAR'])
        hostgroup_create = json.loads(create)
        hostgroup = hostgroup_create['result']

        self.assertEqual(hostgroup_name, hostgroup['name'])
        self.assertFalse(hostgroup['system'])
        self.assertTrue(CLITest.is_int(hostgroup['id']))
        hostgroup_id = int(hostgroup['id'])

        runner_get = CLIRunner(HostgroupGet())
        get = runner_get.get_output(['-i', str(hostgroup_id)])
        hostgroup_get = json.loads(get)
        hostgroup = hostgroup_get['result']

        self.assertEqual(hostgroup_name, hostgroup['name'])
        self.assertFalse(hostgroup['system'])
        self.assertTrue(CLITest.is_int(hostgroup['id']))

        runner_delete = CLIRunner(HostgroupDelete())
        delete = runner_delete.get_output(['-i', str(hostgroup_id)])
        hostgroup_get = json.loads(delete)
        hostgroup = hostgroup_get['result']
        self.assertTrue(hostgroup['success'])
