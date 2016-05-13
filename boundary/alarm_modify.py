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
import json

import requests
from boundary import ApiCli
from boundary.alarm_common import result_to_alarm


class AlarmModify(ApiCli):
    def __init__(self, update):
        ApiCli.__init__(self)
        self._update = update

        # Mapping of alarm types to corresponding codes
        self._alarm_types = {"threshold": 3, "host": 4, "api": 5}

        self._aggregate = None
        self._actions = None
        self._alarm_name = None
        self._alarm_id = None
        self._host_group_id = None
        self._interval = None
        self._is_disabled = None
        self._metric = None
        self._note = None
        self._operation = None
        self._per_host_notify = None
        self._threshold = None
        self._type_id = None
        self._notify_clear = None
        self._notify_set = None
        self._payload = {}
        self._trigger_interval = None
        self._timeout_interval = None

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-m', '--metric', dest='metric', action='store',
                                 required=True,
                                 metavar='metric_name', help='Name of the metric to alarm')

        self.parser.add_argument('-g', '--trigger-aggregate', dest='aggregate', action='store',
                                 required=(False if self._update else True),
                                 choices=['sum', 'avg', 'max', 'min'], help='Metric aggregate to alarm upon')

        self.parser.add_argument('-o', '--trigger-operation', dest='operation', action='store',
                                 required=(False if self._update else True),
                                 choices=['eq', 'gt', 'lt'], help='Trigger threshold comparison')

        self.parser.add_argument('-v', '--trigger-threshold', dest='threshold', action='store',
                                 required=(False if self._update else True),
                                 metavar='value', help='Trigger threshold value')

        self.parser.add_argument('-r', '--trigger-interval', dest='trigger_interval', action='store',
                                 metavar='trigger_interval', required=False, type=int,
                                 help='Interval of time in ms that the alarm state should be in fault ' +
                                      'before triggering')

        self.parser.add_argument('-j', '--timeout-interval', dest='timeout_interval', action='store',
                                 metavar = 'timeout_interval', required=False, type=int,
                                 help='The interval after which an individual host state should resolve by timeout. ' +
                                      'Default: 259200000 milli-seconds (3 days)')

        self.parser.add_argument('-u', '--host-group-id', dest='host_group_id', action='store', metavar='host_group_id',
                                 type=int, help='Host group the alarm applies to')

        self.parser.add_argument('-d', '--note', dest='note', action='store', metavar='note',
                                 help='A description or resolution of the alarm')

        self.parser.add_argument('-k', '--action', dest='actions', action='append', metavar='action-id', type=int,
                                 help='An action to be performed when an alarm is triggered')

        self.parser.add_argument('-c', '--notify-clear', dest='notify_clear', action='store', default=None,
                                 choices=['true', 'false'],
                                 help='Perform actions when all hosts')

        self.parser.add_argument('-s', '--notify-set', dest='notify_set', action='store', default=None,
                                 choices=['true', 'false'],
                                 help='Perform actions when an alarm threshold and interval is breached.')

        self.parser.add_argument('-p', '--per-host-notify', dest='per_host_notify', action='store',
                                 default=None, choices=['true', 'false'],
                                 help='An alarm by default will run the associated actions when \
                                 any server in the host group violates the threshold, and then at the end when \
                                 all servers are back within the threshold. If perHostNotify is set to true, \
                                 the actions will run when ANY server in the group violates \
                                 and falls back within the threshold.')

        self.parser.add_argument('-x', '--is-disabled', dest='is_disabled', action='store', default=None,
                                 choices=['true', 'false'], help='Enable or disable the alarm definition')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)

        self._actions = self.args.actions if self.args.actions is not None else None
        self._alarm_name = self.args.alarm_name if self.args.alarm_name is not None else None

        self._metric = self.args.metric if self.args.metric is not None else None
        self._aggregate = self.args.aggregate if self.args.aggregate is not None else None
        self._operation = self.args.operation if self.args.operation is not None else None
        self._threshold = self.args.threshold if self.args.threshold is not None else None
        self._trigger_interval = self.args.trigger_interval if self.args.trigger_interval is not None else None
        self._host_group_id = self.args.host_group_id if self.args.host_group_id is not None else None
        self._note = self.args.note if self.args.note is not None else None
        self._per_host_notify = self.args.per_host_notify if self.args.per_host_notify is not None else None
        self._is_disabled = self.args.is_disabled if self.args.is_disabled is not None else None
        self._notify_clear = self.args.notify_clear if self.args.notify_clear is not None else None
        self._notify_set = self.args.notify_set if self.args.notify_set is not None else None
        self._timeout_interval = self.args.timeout_interval if self.args.timeout_interval is not None else None

    def get_api_parameters(self):

        # Create trigger predicate dictionary
        predicate = {}

        if self._aggregate is not None:
            predicate['agg'] = self._aggregate
        if self._operation is not None:
            predicate['op'] = self._operation
        if self._threshold is not None:
            predicate['val'] = float(self._threshold)

        if 'agg' in predicate or 'op' in predicate or 'val' in predicate:
            self._payload['triggerPredicate'] = predicate

        # Create payload dictionary
        if self._alarm_name:
            self._payload['name'] = self._alarm_name

        if self._host_group_id is not None:
            self._payload['hostgroupId'] = self._host_group_id

        if self._interval is not None:
            self._payload['triggerInterval'] = self._interval

        if self._is_disabled is not None:
            self._payload['isDisabled'] = self._is_disabled

        if self._metric is not None:
            self._payload['metric'] = self._metric

        if self._note is not None:
            self._payload['note'] = self._note

        if self._actions is not None:
            self._payload['actions'] = self._actions

        if self._per_host_notify is not None:
            self._payload['perHostNotify'] = True if self._per_host_notify == 'yes' else False

        if self._is_disabled is not None:
            self._payload['isDisabled'] = True if self._is_disabled == 'yes' else False

        if self._notify_clear is not None:
            self._payload['notifyClear'] = self._notify_clear

        if self._notify_set is not None:
            self._payload['notifySet'] = self._notify_set

        if self._timeout_interval is not None:
            self._payload['timeoutInterval'] = self._timeout_interval

        if self._trigger_interval is not None:
            self._payload['triggerInterval'] = self._trigger_interval

        self.data = json.dumps(self._payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json'}
        self.path = 'v2/alarms'

    def handle_key_word_args(self):

        self._actions = self._kwargs['actions'] if 'actions' in self._kwargs else None
        self._aggregate = self._kwargs['aggregate'] if 'aggregate' in self._kwargs else None
        self._alarm_name = self._kwargs['name'] if 'name' in self._kwargs else None
        self._alarm_id = self._kwargs['id'] if 'id' in self._kwargs else None
        self._operation = self._kwargs['operation'] if 'operation' in self._kwargs else None
        self._threshold = self._kwargs['threshold'] if 'threshold' in self._kwargs else None
        self._host_group_id = self._kwargs['host_group_id'] if 'host_group_id' in self._kwargs else None
        self._trigger_interval = self._kwargs['trigger_interval'] if 'trigger_interval' in self._kwargs else None
        self._metric = self._kwargs['metric'] if 'metric' in self._kwargs else None
        self._note = self._kwargs['note'] if 'note' in self._kwargs else None
        self._actions = self._kwargs['actions'] if 'actions' in self._kwargs else None
        self._timeout_interval = self._kwargs['timeout_interval'] if 'timeout_interval' in self._kwargs else None
        self._notify_clear = self._kwargs['notifyClear'] if 'notifyClear' in self._kwargs else None
        self._notify_set = self._kwargs['notifySet'] if 'notifySet' in self._kwargs else None

        self.data = json.dumps(self._payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json'}
        self.path = 'v2/alarms'

    def _handle_api_results(self):
        # Only process if we get HTTP result of 201
        if self._api_result.status_code == requests.codes.created:
            alarm_result = json.loads(self._api_result.text)
            return result_to_alarm(alarm_result)
        else:
            return None

