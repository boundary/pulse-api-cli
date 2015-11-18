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

from boundary import ApiCli


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

        self.hostGroupName = ""

    def add_arguments(self):
        ApiCli.add_arguments(self)

        self.parser.add_argument('-n', '--host-group-name', dest='hostGroupName', action='store', required=True,
                                 metavar="host_group_name", help='Host group name')
        self.parser.add_argument('-s', '--sources', dest='sources', action='store', required=True, metavar='sources',
                                 help='Comma separated sources to add to the host group. If empty adds all hosts.')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)

        # Get the host group name
        if self.args.hostGroupName is not None:
            self.hostGroupName = self.args.hostGroupName

        # Get the list of sources separated by commas
        if self.args.sources is not None:
            self.sources = self.args.sources

        payload = {"name": self.hostGroupName, "hostnames": []}
        if self.sources is not None:
            source_list = str.split(self.sources, ',')
            for s in source_list:
                payload['hostnames'].append(s)
        self.data = json.dumps(payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}
