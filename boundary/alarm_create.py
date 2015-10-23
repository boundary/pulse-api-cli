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
from boundary.alarm_common import result_to_alarm


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

    def _handle_api_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            alarm_result = json.loads(self._api_result.text)
            return result_to_alarm(alarm_result['result'])
        else:
            return None

