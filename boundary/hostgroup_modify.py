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
import json


class HostgroupModify(ApiCli):
    def __init__(self, update):
        ApiCli.__init__(self)
        self.update = update
        if self.update:
            self.method = "PUT"
        else:
            self.method = "POST"
        self.path = "v1/hostgroups"
        self.sources = None
        self.host_group_name = None

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)

        # Get the host group name
        if self.args.host_group_name is not None:
            self.host_group_name = self.args.host_group_name

        # Get the list of sources separated by commas
        if self.args.sources is not None:
            self.sources = self.args.sources

        payload = {}
        if self.host_group_name is not None:
            payload['name'] = self.host_group_name

        if self.sources is not None:
            source_list = str.split(self.sources, ',')
            if 'hostnames' not in payload:
                payload['hostnames'] = []

            for s in source_list:
                payload['hostnames'].append(s)
        self.data = json.dumps(payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}
