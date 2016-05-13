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
import requests
import json
import time


class RelayGetOutput(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self._meter = None
        self._since = None
        self._raw = None
        self._relay_output = None

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-n', '--name', metavar='meter_name', dest='meter', action='store', required=True,
                                 help='Name of the meter to get output information')

        self.parser.add_argument('-s', '--since', metavar='since', dest='since', action='store', required=False,
                                 default=1, help='Pull since items from end of log')

        self.parser.add_argument('-r', '--raw', dest='raw', action='store_true', required=False,
                                 help='Send output in raw JSON format')

    def get_arguments(self):
        ApiCli.get_arguments(self)

        self._meter = self.args.meter if self.args.meter is not None else None
        self._since = self.args.since if self.args.since is not None else None
        self._raw = self.args.raw if self.args.raw is not None else None

        self.method = 'GET'
        self.path = 'v1/relays/{0}/output/{1}'.format(self._meter, self._since)

    def get_description(self):
        return 'Queries for relay output messages in a {0} account'.format(self.product_name)

    def _dump_text(self):
        """
        Send output in textual format
        """
        results = self._relay_output['result'];

        for l in results:
            dt = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(int(l[1]['ts'])))
            print("{0} {1} {2} {3}".format(l[0], dt, l[1]['type'], l[1]['msg']))

    def _dump_json(self):
        """
        Send raw JSON output
        """
        out = json.dumps(self._relay_output, sort_keys=True, indent=4, separators=(',', ': '))
        print(self.colorize_json(out))

    def _handle_results(self):
        """
        Call back function to be implemented by the CLI.
        """
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            self._relay_output = json.loads(self._api_result.text)
            if self._raw:
                self._dump_json()
            else:
                self._dump_text()
