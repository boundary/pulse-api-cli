#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class Alarm(object):
    def __init__(self, **kwargs):
        self._operations = ('eq', 'lt', 'gt')
        self._aggregates = ('avg', 'sum', 'max', 'min')

        self._actions = kwargs['actions'] if 'actions' in kwargs else None
        self._aggregate = kwargs['aggregate'] if 'aggregate' in kwargs else None
        self._host_group_id = kwargs['host_group_id'] if 'host_group_id' in kwargs else None
        self._id = kwargs['id'] if 'id' in kwargs else None
        self._interval = kwargs['interval'] if 'interval' in kwargs else None
        self._is_disabled = kwargs['is_disabled'] if 'is_disabled' in kwargs else None
        self._metric_name = kwargs['metric_name'] if 'metric_name' in kwargs else None
        self._name = kwargs['name'] if 'name' in kwargs else None
        self._note = kwargs['note'] if 'note' in kwargs else None
        self._operation = kwargs['operation'] if 'operation' in kwargs else None
        self._per_host_notify = kwargs['per_host_notify'] if 'per_host_notify' in kwargs else None
        self._threshold = kwargs['threshold'] if 'threshold' in kwargs else None

    def __repr__(self):
        return 'Alarm(aggregate={0}, actions={1}, host_group_id={2}, id={3}, ' \
               'interval={4}, is_disabled={5}, metric_name={6}, name={7}, note={8}, operation={9}, ' \
               'per_host_notify={10}, ' \
               'threshold={11}'.format('"{0}"'.format(self._aggregate) if self._aggregate is not None else None,
                                       self._actions, self._host_group_id,self._id, self._interval, self._is_disabled,
                                       '"{0}"'.format(self._metric_name) if self._metric_name is not None else None,
                                       '"{0}"'.format(self._name) if self._name is not None else None,
                                       '"{0}"'.format(self._note) if self._note is not None else None,
                                       '"{0}"'.format(self._operation) if self._operation is not None else None,
                                       self._per_host_notify, self._threshold)

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, actions):
        self._actions = actions

    @property
    def aggregate(self):
        return self._aggregate

    @aggregate.setter
    def aggregate(self, value):
        if value not in self._aggregates:
            raise AttributeError("Method value not in " + str(self._aggregates));
        self._aggregate = value

    @property
    def host_group_id(self):
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        self._host_group_id = host_group_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, interval):
        self._interval = interval

    @property
    def is_disabled(self):
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        self._is_disabled = is_disabled

    @property
    def metric_name(self):
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        self._metric_name = metric_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        self._note = note

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, operation):
        self._operation = operation

    @property
    def per_host_notify(self):
        return self._per_host_notify

    @per_host_notify.setter
    def per_host_notify(self, per_host_notify):
        self._per_host_notify = per_host_notify

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        self._threshold = threshold


def result_to_alarm(result):
    try:
        # We call these inside a try block since they are suppose to exist
        alarm_id = result['id']
        name = result['name']
        if result['triggerPredicate'] is not None:
            aggregate = result['triggerPredicate']['agg']
            operation = result['triggerPredicate']['op']
            threshold = result['triggerPredicate']['val']
        metric_name = result['metricName']

        # These are optional so explicitly check to see if the exist
        hostgroup_id = result['hostgroupId'] if 'hostgroupId' in result else None
        interval = result['interval'] if 'interval' in result else None
        is_disabled = result['isDisabled'] if 'isDisabled' in result else None
        note = result['note'] if 'note' in result else None
        per_host_notify = result['perHostNotify'] if 'perHostNotify' in result else None
        actions = result['actions'] if 'actions' in result else None
        return Alarm(
            actions=actions,
            aggregate=aggregate,
            host_group_id=hostgroup_id,
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

    except NameError:
        return None
