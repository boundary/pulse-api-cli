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
"""
Implements a command to get the information about an alarm
"""

from boundary import ApiCli
from boundary.alarm_common import result_to_alarm
import json
import requests

"""
Uses the following TrueSight Pulse API:

https://premium-api.boundary.com/v1/alarms/search?name=
"""


class AlarmSearch(ApiCli):
    def __init__(self):
        """
        """
        ApiCli.__init__(self)
        self._alarm_name = None

    def add_arguments(self):
        """
        """
        ApiCli.add_arguments(self)

        self.parser.add_argument('-n', '--alarm-name', dest='alarm_name', action='store', required=True,
                                 metavar='alarm-name', help='Alarm name')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)
        self._alarm_name = self.args.alarm_name if self.args.alarm_name is not None else None

    def handle_key_word_args(self):
        self._alarm_name = self._kwargs['name'] if 'name' in self._kwargs else None

    def get_api_parameters(self):
        self.method = "GET"
        self.path = "v2/alarms/search"
        self.url_parameters = {'name': self._alarm_name}

    def get_description(self):
        """
        """
        return "Searches for an alarm definition by name from a {0} account".format(self.product_name)

    def _handle_api_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            alarm_result = json.loads(self._api_result.text)
            return result_to_alarm(alarm_result['result'])
        else:
            return None
