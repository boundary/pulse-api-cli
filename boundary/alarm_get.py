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


class AlarmGet(ApiCli):
    def __init__(self):
        """
        """
        ApiCli.__init__(self)
        self._alarm_id = None

    def add_arguments(self):
        """
        """
        ApiCli.add_arguments(self)

        self.parser.add_argument('-i', '--alarm-id', dest='alarm_id', action='store', required=True,
                                 metavar='alarm-id', help='Alarm identifier')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)
        self._alarm_id = self.args.alarm_id if self.args.alarm_id is not None else None

    def handle_key_word_args(self):
        self._alarm_id = self._kwargs['id'] if 'id' in self._kwargs else None

    def get_api_parameters(self):
        self.method = "GET"
        self.path = "v2/alarms/{0}".format(self._alarm_id)

    def get_description(self):
        """
        """
        return "Retrieves an alarm definition from a {0} account".format(self.product_name)

    def _handle_api_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            alarm_result = json.loads(self._api_result.text)
            return result_to_alarm(alarm_result['result'])
        else:
            return None




