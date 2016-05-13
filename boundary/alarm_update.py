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

from boundary import AlarmModify


class AlarmUpdate(AlarmModify):
    def __init__(self):
        AlarmModify.__init__(self, True)
        self._alarm_id = None

    def add_arguments(self):

        self.parser.add_argument('-i', '--alarm-id', dest='alarm_id', action='store', required=True, type=int,
                                 metavar='alarm_id', help='Id of the alarm to update')
        self.parser.add_argument('-n', '--alarm-name', dest='alarm_name', action='store',
                                 metavar='alarm_name', help='Name of the alarm')

        AlarmModify.add_arguments(self)

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """

        AlarmModify.get_arguments(self)
        self._alarm_id = self.args.alarm_id if self.args.alarm_id is not None else None
        self.get_api_parameters()

    def handle_key_word_args(self):
        AlarmModify.handle_key_word_args(self)
        self._alarm_id = self._kwargs['id'] if 'id' in self._kwargs else None

    def get_api_parameters(self):
        AlarmModify.get_api_parameters(self)
        self.method = "PUT"
        if self._alarm_id is not None:
            self._payload['id'] = int(self._alarm_id)
        self.data = json.dumps(self._payload, sort_keys=True)
        self.path = "v2/alarms/{0}".format(self._alarm_id)

    def get_description(self):
        return 'Updates an alarm definition in an {0} account'.format(self.product_name)


