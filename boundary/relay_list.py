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
from boundary import ApiCli


class RelayList(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.path = "v1/relays"
        self._control = None
        self._metrics = None
        self._plugins = None
        self._plugin_summary = None
        self._relays = None

    def add_arguments(self):
        ApiCli.add_arguments(self)

        self.parser.add_argument('--no-control', dest="control", action='store_true', required=False,
                                 help='Remove control field from the output')
        self.parser.add_argument('--no-metrics', dest="metrics", action='store_true', required=False,
                                 help='Remove metric field from the output')
        self.parser.add_argument('--no-plugins', dest="plugins", action='store_true', required=False,
                                 help='Remove plugins field from the output')
        # self.parser.add_argument('--plugin-summary', dest="plugin_summary", action='store_true', required=False,
        #                          help='Displays only a summary of the plugin output')

    def get_arguments(self):
        ApiCli.get_arguments(self)

        if self.args.control is not None:
            self._control = self.args.control
        if self.args.metrics is not None:
            self._metrics = self.args.metrics
        if self.args.plugins is not None:
            self._plugins = self.args.plugins
        # if self.args.plugin_summary is not None:
        #    self._plugin_summary = self.args.plugin_summary

    def get_description(self):
        return 'Lists the relays in a {0} account'.format(self.product_name)

    def _filter(self):
        """
        Apply the criteria to filter out on the output required
        """
        if self._metrics or self._control or self._plugins:
            relays = self._relays['result']['relays']
            for relay in relays:
                if self._metrics:
                    del relays[relay]['metrics']
                if self._control:
                    del relays[relay]['control']
                if self._plugins:
                    if 'plugins' in relays[relay]:
                        del relays[relay]['plugins']

    def _dump_json(self):
        out = json.dumps(self._relays, sort_keys=True, indent=4, separators=(',', ': '))
        print(self.colorize_json(out))

    def _handle_results(self):
        """
        Call back function to be implemented by the CLI.
        """

        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            self._relays = json.loads(self._api_result.text)
            self._filter()
            self._dump_json()
