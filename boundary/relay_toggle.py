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


class RelayToggle(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self._path = None
        self._name = None
        self._disable = False
        self._remove = False
        self._sources = None

    def add_arguments(self):
        ApiCli.add_arguments(self)

        self.parser.add_argument('-d', '--disable', dest='disabled', action='store', default=None,
                                 choices=['yes', 'no'], help='Enable or disable the meter')
        self.parser.add_argument('-n', '--name', metavar='name', dest='name', action='store', required=True,
                                 help='Name of the meter to toggle')
        self.parser.add_argument('-r', '--remove', dest='remove', action='store', default=None,
                                 choices=['yes', 'no'], help='Remove the meter')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)

        # Get the list of sources separated by commas
        if self.args.sources is not None:
            self._sources = self.args.sources

        payload = {}
        if self._sources is not None:
            source_list = str.split(self._sources, ',')
            for s in source_list:
                payload['names'].append(s)

        self.data = json.dumps(payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}

    def get_description(self):
        return 'Set a relay to be disabled or enabled'.format(self.product_name)
