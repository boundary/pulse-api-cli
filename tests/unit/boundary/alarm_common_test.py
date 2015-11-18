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
from boundary import Alarm


class AlarmCreateTest(TestCase):
    def setUp(self):
        self.alarm = Alarm()

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)


    def test_alarm_defaults(self):
        self.assertIsNone(self.alarm.actions)
        self.assertIsNone(self.alarm.aggregate)
        self.assertIsNone(self.alarm.host_group_id)
        self.assertIsNone(self.alarm.id)
        self.assertIsNone(self.alarm.interval)
        self.assertIsNone(self.alarm.is_disabled)
        self.assertIsNone(self.alarm.metric_name)
        self.assertIsNone(self.alarm.name)
        self.assertIsNone(self.alarm.note)
        self.assertIsNone(self.alarm.operation)
        self.assertIsNone(self.alarm.per_host_notify)
        self.assertIsNone(self.alarm.threshold)

    def test_alarm_init(self):
        actions = [1, 2]
        aggregate = 'avg'
        host_group_id = 1000
        alarm_id = 123456789
        interval = '1 hour'
        is_disabled = True
        metric_name = "TEST_METRIC"
        name = 'My Alarm'
        note = 'just a note'
        operation = 'eq'
        per_host_notify = True
        threshold = 1000

        alarm = Alarm(
            actions=actions,
            aggregate=aggregate,
            host_group_id=host_group_id,
            id=alarm_id,
            interval=interval,
            is_disabled=is_disabled,
            metric_name=metric_name,
            name=name,
            note=note,
            operation=operation,
            per_host_notify=per_host_notify,
            threshold=threshold
        )

        self.assertEqual(actions, alarm.actions)
        self.assertEqual(aggregate, alarm.aggregate)
        self.assertEqual(host_group_id, alarm.host_group_id)
        self.assertEqual(alarm_id, alarm.id)
        self.assertEqual(interval, alarm.interval)
        self.assertEqual(is_disabled, alarm.is_disabled)
        self.assertEqual(metric_name, alarm.metric_name)
        self.assertEqual(name, alarm.name)
        self.assertEqual(note, alarm.note)
        self.assertEqual(operation, alarm.operation)
        self.assertEqual(per_host_notify, alarm.per_host_notify)
        self.assertEqual(threshold, alarm.threshold)

    def test_set_actions(self):
        self.alarm.actions = [1, 2, 3, 4]
        self.assertEqual([1, 2, 3, 4], self.alarm.actions)

    def test_set_aggregate(self):
        self.alarm.aggregate = 'sum'
        self.assertEqual('sum', self.alarm.aggregate)

    def test_set_id(self):
        self.alarm.id = 1076
        self.assertEqual(1076, self.alarm.id)

    def test_set_interval(self):
        self.alarm.interval = 60
        self.assertEqual(60, self.alarm.interval)

    def test_set_is_disabled(self):
        self.alarm.is_disabled = True
        self.assertEqual(True, self.alarm.is_disabled)

    def test_set_metric_name(self):
        self.alarm.metric_name = 'toad'
        self.assertEqual('toad', self.alarm.metric_name)

    def test_set_name(self):
        self.alarm.name = 'blue'
        self.assertEqual('blue', self.alarm.name)

    def test_set_note(self):
        self.alarm.note = 'This is a note'
        self.assertEqual('This is a note', self.alarm.note)

    def test_set_operation(self):
        self.alarm.operation = 'gt'
        self.assertEqual('gt', self.alarm.operation)

    def test_set_per_host_notify(self):
        self.alarm.per_host_notify = True
        self.assertEqual(True, self.alarm.per_host_notify)

    def test_set_threshold(self):
        self.alarm.threshold = 2000
        self.assertEqual(2000, self.alarm.threshold)

    def test_set_bad_aggregate(self):
        with self.assertRaises(AttributeError, msg='Check bad aggregate'):
            alarm = Alarm()
            alarm.aggregate = 'foo'

    def test_repr(self):
        alarm = Alarm(
            actions=[1, 2],
            aggregate='avg',
            host_group_id=1000,
            alarm_id=123456789,
            interval=900,
            is_disabled=True,
            metric_name='TEST_METRIC',
            name='My Alarm',
            note='just a note',
            operation='eq',
            per_host_notify=True,
            threshold=1000
        )

        self.assertEqual('Alarm(aggregate="avg", actions=[1, 2], host_group_id=1000, id=None, interval=900, '
                         'is_disabled=True, metric_name="TEST_METRIC", name="My Alarm", '
                         'note="just a note", operation="eq", per_host_notify=True, threshold=1000',
                         alarm.__repr__())
