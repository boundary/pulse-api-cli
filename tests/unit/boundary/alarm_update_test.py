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
from boundary import AlarmUpdate
from boundary import API
from cli_test import CLITest


class AlarmUpdateTest(TestCase):
    def setUp(self):
        self.cli = AlarmUpdate()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_api_call(self):
        actions = [1693]
        aggregate = 'sum'
        host_group_id = 1000
        interval = '1 minute'
        is_disabled = True
        metric_name = 'CPU'
        note = 'This is a note'
        name = 'ALARM_CREATE_TEST'
        operation = 'gt'
        per_host_modify = True
        threshold = '0.80'
        alarm = self.api.alarm_create(actions=actions, aggregate=aggregate, interval=interval,
                                      is_disabled=is_disabled, host_group_id=host_group_id, metric_name=metric_name,
                                      name=name, note=note, operation=operation, per_host_modify=per_host_modify,
                                      threshold=threshold)

        actions = [2000]
        aggregate = 'avg'
        host_group_id = 2000
        interval = '1 hour'
        is_disabled = False
        metric_name = 'SYSTEM.CPU.IOWAIT'
        metric_name = 'CPU'
        note = 'This is a updated note'
        name = 'ALARM_UPDATE_TEST'
        operation = 'lt'
        per_host_modify = True
        threshold = '0.50'

        # alarm = self.api.alarm_update(id=alarm.id, actions=actions, aggregate=aggregate, interval=interval,
        #                               is_disabled=is_disabled, host_group_id=host_group_id, metric_name=metric_name,
        #                               name=name, note=note, operation=operation, per_host_modify=per_host_modify,
        #                               threshold=threshold)
        #
        # self.assertListEqual(actions, alarm.actions)
        # self.assertEqual(aggregate, alarm.aggregate)
        # self.assertEqual(3600, alarm.interval)
        # self.assertEqual(is_disabled, alarm.is_disabled)
        # self.assertEqual(host_group_id, alarm.host_group_id)
        # self.assertEqual(metric_name, alarm.metric_name)
        # self.assertEqual(name, alarm.name)
        # self.assertEqual(note, alarm.note)
        # self.assertEqual(operation, alarm.operation)
        # self.assertEqual(per_host_modify, alarm.per_host_modify)
        # self.assertEqual(threshold, alarm.threshold)
