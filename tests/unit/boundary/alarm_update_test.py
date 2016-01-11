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
from boundary import AlarmCreate
from boundary import AlarmDelete
from boundary import AlarmGet
from boundary import AlarmUpdate
from cli_runner import CLIRunner
from cli_test import CLITest


class AlarmUpdateTest(TestCase):
    def setUp(self):
        self.cli = AlarmUpdate()
        self.api = API()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_api_call(self):
        aggregate = 'sum'
        interval = '1 minute'
        is_disabled = True
        metric_name = 'CPU'
        note = 'This is a note'
        alarm_name = 'ALARM_CREATE_TEST' + CLITest.random_string(4)
        operation = 'gt'
        per_host_modify = True
        threshold = '0.80'
        alarm_create = self.api.alarm_create(aggregate=aggregate,
                                             interval=interval,
                                             is_disabled=is_disabled,
                                             metric_name=metric_name,
                                             name=alarm_name,
                                             note=note,
                                             operation=operation,
                                             per_host_modify=per_host_modify,
                                             threshold=threshold)

        aggregate = 'avg'
        interval = '1 hour'
        is_disabled = False
        metric_name = 'CPU'
        note = 'This is a updated note'
        operation = 'lt'
        per_host_modify = True
        threshold = '0.50'

        alarm_update = self.api.alarm_update(id=alarm_create.id,
                                             aggregate=aggregate,
                                             interval=interval,
                                             is_disabled=is_disabled,
                                             metric_name=metric_name,
                                             name=alarm_name,
                                             note=note,
                                             operation=operation,
                                             per_host_modify=per_host_modify,
                                             threshold=threshold)

        self.assertEqual(aggregate, alarm_update.aggregate)
        self.assertEqual(3600, alarm_update.interval)
        self.assertEqual(is_disabled, alarm_update.is_disabled)
        self.assertEqual(metric_name, alarm_update.metric_name)
        self.assertEqual(alarm_name, alarm_update.name)
        self.assertEqual(note, alarm_update.note)
        self.assertEqual(operation, alarm_update.operation)
        self.assertEqual(per_host_modify, alarm_update.per_host_modify)
        self.assertEqual(threshold, alarm_update.threshold)

        self.api.alarm_delete(id=alarm_create.id)

    def test_update_alarm(self):
        alarm_name = 'my-alarm-' + CLITest.random_string(6)
        metric_name = 'CPU'
        note = CLITest.random_string(50)
        aggregate = 'max'
        op = 'gt'
        value = 0.75
        interval = '5 minutes'
        is_disabled = True
        runner_create = CLIRunner(AlarmCreate())
        create = runner_create.get_output(['-n', alarm_name,
                                           '-m', metric_name,
                                           '-d', note,
                                           '-g', aggregate,
                                           '-o', op,
                                           '-v', str(value),
                                           '-r', str(interval),
                                           '-x', str(is_disabled).lower()])
        result_create = json.loads(create)
        alarm_create = result_create['result']

        note = CLITest.random_string(50)
        aggregate = 'max'
        op = 'gt'
        value = 0.75
        interval = '5 minutes'
        is_disabled = False

        runner_update = CLIRunner(AlarmUpdate())
        update = runner_update.get_output(['-i', str(alarm_create['id']),
                                           '-n', alarm_name,
                                           '-m', metric_name,
                                           '-d', note,
                                           '-g', aggregate,
                                           '-o', op,
                                           '-v', str(value),
                                           '-r', str(interval),
                                           '-x', str(is_disabled).lower()])
        result_update = json.loads(update)
        alarm = result_update['result']

        self.assertEqual(300000, alarm['triggerInterval'])
        self.assertEqual(1, alarm['familyId'])
        self.assertFalse(is_disabled, alarm['isDisabled'])
        self.assertEqual(metric_name, alarm['metric'])
        self.assertEqual(alarm_name, alarm['name'])
        self.assertEqual(aggregate, alarm['triggerPredicate']['agg'])
        self.assertEqual(op, alarm['triggerPredicate']['op'])
        self.assertEqual(value, alarm['triggerPredicate']['val'])
        self.assertEqual(3, int(alarm['typeId']))
        self.assertEqual(note, alarm['note'])

        runner_delete = CLIRunner(AlarmDelete())
        delete = runner_delete.get_output(['-i', str(alarm['id'])])
