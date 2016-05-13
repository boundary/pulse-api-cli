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
from boundary import ApiCli
from boundary.alarm_common import result_to_alarm
import json
import requests


class AlarmList(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)

    def get_description(self):
        return "List alarm definitions associated with the {0} account".format(self.product_name)

    def get_api_parameters(self):
        self.path = "v2/alarms"
        self.method = "GET"

    def handle_key_word_args(self):
        pass

    def _handle_api_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            alarm_result = json.loads(self._api_result.text)
            alarms = []
            for alarm in alarm_result['result']:
                alarms.append(result_to_alarm(alarm))
            return alarms
        else:
            return None

