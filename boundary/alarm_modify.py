#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from boundary import ApiCli
import json


class AlarmModify(ApiCli):
    def __init__(self, update):
        ApiCli.__init__(self)
        self.update = update
        self.method = "POST"

        self.alarm_name = None
        self.metric_name = None
        self.aggregate = None
        self.operation = None
        self.threshold = None
        self.interval = None
        self.host_group_id = None
        self.note = None
        self.per_host_notify = None
        self.actions = None
        self.is_disabled = None

        self.intervals = {'1 second': 1,
                          '5 seconds': 15,
                          '1 minute': 60,
                          '5 minutes': 300,
                          '1 hour': 3600,
                          '1.5 hours': 5400,
                          '3 hours': 10800,
                          '6 hours': 21600,
                          '12 hours': 43200
                          }

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-m', '--metric', dest='metric_name', action='store',
                                 required=(False if self.update else True),
                                 metavar='metric_name', help='Name of the metric to alarm')

        self.parser.add_argument('-g', '--trigger-aggregate', dest='aggregate', action='store',
                                 required=(False if self.update else True),
                                 choices=['SUM', 'AVG', 'MAX', 'MIN'], help='Metric aggregate to alarm upon')

        self.parser.add_argument('-o', '--trigger-operation', dest='operation', action='store',
                                 required=(False if self.update else True),
                                 choices=['eq', 'gt', 'lt'], help='Trigger threshold comparison')

        self.parser.add_argument('-v', '--trigger-threshold', dest='threshold', action='store',
                                 required=(False if self.update else True),
                                 metavar='value', help='Trigger threshold value')

        self.parser.add_argument('-r', '--trigger-interval', dest='interval', action='store',
                                 required=(False if self.update else True),
                                 choices=['1 second', '15 seconds', '1 minute', '5 minutes', '1 hour', '1.5 hours',
                                          '3 hours', '6 hours', '12 hours'],
                                 help='Interval to alarm upon')

        self.parser.add_argument('-u', '--host-group-id', dest='host_group_id', action='store', metavar='host_group_id',
                                 type=int, help='Host group the alarm applies to')

        self.parser.add_argument('-d', '--note', dest='note', action='store', metavar='note',
                                 help='A description or resolution of the alarm')

        self.parser.add_argument('-c', '--action', dest='actions', action='append', metavar='action-id', type=int,
                                 help='An action to be performed when an alarm is triggered')

        self.parser.add_argument('-p', '--per-host-notify', dest='per_host_notify', action='store',
                                 default=None, choices=['yes', 'no'],
                                 help='An alarm by default will run the associated actions when \
                                 any server in the host group violates the threshold, and then at the end when \
                                 all servers are back within the threshold. If perHostNotify is set to true, \
                                 the actions will run when ANY server in the group violates \
                                 and falls back within the threshold.')

        self.parser.add_argument('-x', '--is-disabled', dest='is_disabled', action='store', default=None,
                                 choices=['yes', 'no'], help='Enable or disable the alarm definition')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)

        if self.args.alarm_name is not None:
            self.alarm_name = self.args.alarm_name

        if self.args.metric_name is not None:
            self.metric_name = self.args.metric_name

        if self.args.aggregate is not None:
            self.aggregate = self.args.aggregate

        if self.args.operation is not None:
            self.operation = self.args.operation

        if self.args.threshold is not None:
            self.threshold = self.args.threshold

        if self.args.interval is not None:
            self.interval = self.args.interval

        if self.args.host_group_id is not None:
            self.host_group_id = self.args.host_group_id

        if self.args.actions is not None:
            self.actions = self.args.actions

        if self.args.note is not None:
            self.note = self.args.note

        if self.args.per_host_notify is not None:
            self.per_host_notify = self.args.per_host_notify

        if self.args.is_disabled is not None:
            self.is_disabled = self.args.is_disabled

        self.get_api_parameters()

    def get_api_parameters(self):
        payload = {}

        # Create trigger predicate dictionary
        predicate = {}

        if self.aggregate is not None:
            predicate['agg'] = self.aggregate

        if self.operation is not None:
            predicate['op'] = self.operation

        if self.threshold is not None:
            predicate['val'] = self.threshold

        if 'agg' in predicate or 'op' in predicate or 'val' in predicate:
            payload['triggerPredicate'] = predicate

        # Create payload dictionary
        if self.alarm_name:
            payload['name'] = self.alarm_name

        if self.host_group_id is not None:
            payload['hostgroupId'] = self.host_group_id

        if self.interval is not None:
            payload['interval'] = self.intervals[self.interval]

        if self.metric_name is not None:
            payload['metricName'] = self.metric_name

        if self.note is not None:
            payload['note'] = self.note

        if self.actions is not None:
            payload['actions'] = self.actions

        if self.per_host_notify is not None:
            payload['perHostNotify'] = True if self.per_host_notify == 'yes' else False

        if self.is_disabled is not None:
            payload['isDisabled'] = True if self.is_disabled == 'yes' else False

        self.data = json.dumps(payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json'}

    def handle_key_word_args(self):

        if 'name' in self._kwargs:
            self.alarm_name = self._kwargs['name']

        if 'aggregate' in self._kwargs:
            self.aggregate = self._kwargs['aggregate']

        if 'operation' in self._kwargs:
            self.operation = self._kwargs['operation']

        if 'threshold' in self._kwargs:
            self.threshold = self._kwargs['threshold']

        if 'host_group_id' in self._kwargs:
            self.host_group_id = self._kwargs['host_group_id']

        if 'interval' in self._kwargs:
            self.interval = self._kwargs['interval']

        if 'metric_name' in self._kwargs:
            self.metric_name = self._kwargs['metric_name']

        if 'note' in self._kwargs:
            self.note = self._kwargs['note']

        if 'actions' in self._kwargs:
            self.actions = self._kwargs['actions']

        if 'per_host_notify' in self._kwargs:
            self.per_host_notify = self._kwargs['per_host_notify']

        if 'is_disabled' in self._kwargs:
            self.is_disabled = self._kwargs["is_disabled"]

