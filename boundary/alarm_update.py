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


class AlarmUpdate(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "POST"

        self.alarmName = None
        self.metricName = None
        self.aggregate = None
        self.operation = None
        self.threshold = None
        self.interval = None
        self.hostGroupId = None
        self.note = None
        self.perHostNotify = None
        self.actions = None
        self.isDisabled = False

        self.intervals = {'1 second': 1,
                          '5 seconds': 15,
                          '1 minute': 60,
                          '5 minutes': 900,
                          '1 hour': 3600,
                          '1.5 hours': 5400,
                          '3 hours': 10800,
                          '6 hours': 21600,
                          '12 hours': 43200
                          }

        self.cli_description = "Creates a new metric definition in an Boundary account"

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--alarm-name', dest='alarmName', action='store', required=True,
                                 metavar='alarm_name', help='Name of the alarm')
        self.parser.add_argument('-m', '--metric', dest='metricName', action='store', required=True,
                                 metavar='metric_name', help='Name of the metric to alarm')
        self.parser.add_argument('-g', '--trigger-aggregate', dest='aggregate', action='store', required=True,
                                 choices=['sum', 'avg', 'max', 'min'], help='Metric aggregate to alarm upon')
        self.parser.add_argument('-o', '--trigger-operation', dest='operation', action='store', required=True,
                                 choices=['eq', 'gt', 'lt'], help='Trigger threshold comparison')
        self.parser.add_argument('-v', '--trigger-threshold', dest='threshold', action='store', required=True,
                                 metavar='value', help='Trigger threshold value')
        self.parser.add_argument('-r', '--trigger-interval', dest='interval', action='store', required=True,
                                 choices=['1 second', '15 seconds', '1 minute', '5 minutes', '1 hour', '1.5 hours',
                                          '3 hours', '6 hours', '12 hours'],
                                 help='Interval to alarm upon')
        self.parser.add_argument('-i', '--host-group-id', dest='hostGroupId', action='store', metavar='hostgroup_id',
                                 type=int, help='Host group the alarm applies to')
        self.parser.add_argument('-d', '--note', dest='note', action='store', metavar='note',
                                 help='A description or resolution of the alarm')
        self.parser.add_argument('-c', '--action', dest='actions', action='append', metavar='action-id', type=int,
                                 help='An action to be performed when an alarm is triggered')
        self.parser.add_argument('-p', '--per-host-notify', dest='perHostNotify', action='store_true', default=None,
                                 help='An alarm by default will run the associated actions when \
                                 any server in the host group violates the threshold, and then at the end when \
                                 all servers are back within the threshold. If perHostNotify is set to true, \
                                 the actions will run when ANY server in the group violates \
                                 and falls back within the threshold.')
        self.parser.add_argument('-x', '--is-disabled', dest='isDisabled', action='store_true', default=None,
                                 help='Enable or disable the alarm')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)
        if self.args.alarmName is not None:
            self.alarmName = self.args.alarmName

        if self.args.metricName is not None:
            self.metricName = self.args.metricName

        if self.args.aggregate is not None:
            self.aggregate = self.args.aggregate

        if self.args.operation is not None:
            self.operation = self.args.operation

        if self.args.threshold is not None:
            self.threshold = self.args.threshold

        if self.args.interval is not None:
            self.interval = self.args.interval

        if self.args.hostGroupId is not None:
            self.hostGroupId = self.args.hostGroupId

        if self.args.actions is not None:
            self.actions = self.args.actions

        if self.args.note is not None:
            self.note = self.args.note

        if self.args.perHostNotify is not None:
            self.perHostNotify = self.args.perHostNotify

        if self.args.isDisabled is not None:
            self.isDisabled = self.args.isDisabled

        p = {
            'name': self.alarmName,
            'triggerPredicate': {"agg": self.aggregate, "op": self.operation, "val": self.threshold},
            'metricName': self.metricName,
            'interval': self.intervals[self.interval]
        }

        if self.hostGroupId is not None:
            p['hostgroupId'] = self.hostGroupId
        if self.note is not None:
            p['note'] = self.note
        if self.actions is not None:
            p['actions'] = self.actions
        if self.perHostNotify is not None:
            p['perHostNotify'] = self.perHostNotify
        if self.isDisabled is not None:
            p['isDisabled'] = self.isDisabled

        self.data = json.dumps(p, sort_keys=True)
        self.path = 'v1/alarms'
        self.headers = {'Content-Type': 'application/json'}

    def getDescription(self):
        return "Creates a new metric definition in an Boundary account"
