#
# Copyright 2014-2015 Boundary, Inc.
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
        self._id = kwargs['id'] if 'id' in kwargs else None
        self._interval = kwargs['interval'] if 'interval' in kwargs else None
        self._metric_name = kwargs['metric_name'] if 'metric_name' in kwargs else None
        self._name = kwargs['name'] if 'name' in kwargs else None
        self._note = kwargs['note'] if 'note' in kwargs else None
        self._operation = kwargs['operation'] if 'operation' in kwargs else None
        self._per_host_notify = kwargs['per_host_notify'] if 'per_host_notify' in kwargs else None
        self._threshold = kwargs['threshold'] if 'threshold' in kwargs else None

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


class Alarms:
    def __init__(self, alarms):
        self._alarms = alarms

    def __getitem__(self, item):
        alarm_values = self._metrics["result"][item]
        alarm = None
        if alarm_values is not None:
            alarm = Alarm(id=alarm_values["id"])

        return alarm


def result_to_alarm(result):
    try:
        # We call these inside a try block since they are suppose to exist
        alarm_id = result['id']
        name = result['name']
        aggregate = result['triggerPredicate']['agg']
        operation = result['triggerPredicate']['op']
        threshold = result['triggerPredicate']['val']
        metric_name = result['metricName']

        # These are optional so explicity check to see if the exist
        interval = result['interval'] if 'interval' in result else None
        note = result['note'] if 'note' in result else None
        per_host_notify = result['perHostNotify'] if 'perHostNotify' in result else None
        actions = result['interval'] if 'interval' in result else None
        return Alarm(id=alarm_id,
                     name=name,
                     aggregate=aggregate,
                     operation=operation,
                     threshold=threshold,
                     metric_name=metric_name,
                     interval=interval,
                     note=note,
                     per_host_notify=per_host_notify,
                     actions=actions)

    except NameError:
        return None
