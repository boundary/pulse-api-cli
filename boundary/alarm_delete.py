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
Implements command to remove an alarm definition from a Boundary account.
"""
from boundary import ApiCli
import requests

"""
Uses the following Boundary API:

https://premium-api.boundary.com/v1/alarm/:alarmId
"""


class AlarmDelete(ApiCli):
    def __init__(self,  **kwargs):
        """
        """
        ApiCli.__init__(self)
        self._kwargs = kwargs
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
        self.method = "DELETE"
        self.path = "v2/alarms/{0}".format(self._alarm_id)

    def get_description(self):
        return 'Deletes an alarm definition from a {0} account'.format(self.product_name)

    def _handle_results(self):
        """
        Handle the results of the API call
        """

        # Only process if we get HTTP return code other 200.
        if self._api_result.status_code != requests.codes.ok:
            print(self.colorize_json(self._api_result.text))

    def _handle_api_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code != requests.codes.ok:
            pass
        return None

    def good_response(self, status_code):
        """
        Determines what status codes represent a good response from an API call.
        """
        return status_code == requests.codes.no_content
