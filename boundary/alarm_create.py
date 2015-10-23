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
from boundary import AlarmModify
import requests
import json
from boundary import Alarm


class AlarmCreate(AlarmModify):
    def __init__(self, **kwargs):
        AlarmModify.__init__(self, False)
        self._kwargs = kwargs
        self.method = "POST"
        self._alarm_result = None

        self.cli_description = "Creates a new alarm definition in an Boundary account"

    def addArguments(self):

        self.parser.add_argument('-n', '--alarm-name', dest='alarm_name', action='store', required=True,
                                 metavar='alarm_name', help='Name of the alarm')

        AlarmModify.addArguments(self)

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        AlarmModify.getArguments(self)

        self.get_api_parameters()

    def getDescription(self):
        return 'Creates an alarm definition in an {0} account'.format(self.product_name)

    def get_api_parameters(self):
        AlarmModify.get_api_parameters(self)
        self.path = 'v1/alarms'

    # {
    #     "result": {
    #         "id": 50877,
    #         "name": "bar2",
    #         "triggerPredicate": {
    #             "agg": "AVG",
    #             "op": "gt",
    #             "val": "0.80"
    #         },
    #         "metricName": "CPU",
    #         "interval": 60,
    #         "note": "a note",
    #         "perHostNotify": false,
    #         "actions": [
    #             8428
    #         ]
    #     }
    # }
    def dict_to_alarm(self):
        try:
            alarm_id = self._alarm_result['id']
            name = self._alarm_result['name']
            aggregate = self._alarm_result['triggerPredicate']['agg']
            operation = self._alarm_result['triggerPredicate']['op']
            threshold = self._alarm_result['triggerPredicate']['val']
            metric_name = self._alarm_result['metricName']

            # These are optional
            interval = self._alarm_result['interval'] if 'interval' in self._alarm_result else None
            note = self._alarm_result['note'] if 'note' in self._alarm_result else None
            per_host_notify = self._alarm_result['perHostNotify'] if 'perHostNotify' in self._alarm_result else None
            actions = self._alarm_result['interval'] if 'interval' in self._alarm_result else None
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
            pass

    def _handle_api_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            alarm_result = json.loads(self._api_result.text)
            self._alarm_result = alarm_result['result']
        return self.dict_to_alarm()
