#
# Copyright 2014-2015 Boundary, Inc.
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

from boundary import MetricCommon
import json
import requests


class MetricList(MetricCommon):
    def __init__(self):
        MetricCommon.__init__(self)

        self._enabled = None
        self._custom = None

    def addArguments(self):
        MetricCommon.addArguments(self)
        self.parser.add_argument('-b', '--enabled', dest="enabled", action='store_true', required=False, default=False,
                                 help='Filter the list of metrics to only return enabled metrics')
        self.parser.add_argument('-c', '--custom', dest="custom", action='store_true', required=False, default=False,
                                 help='Filter the list of metrics to only return custom metrics')

    def getArguments(self):
        self._enabled = self.args.enabled if self.args.enabled is not None else None
        self._custom = self.args.custom if self.args.custom is not None else None

        self.get_api_parameters()

    def get_api_parameters(self):
        self.path = "v1/metrics"
        self.method = "GET"
        self.url_parameters = {'enabled': self._enabled, 'custom': self._custom}

    def getDescription(self):
        """
        Text describing this command
        """
        return "Lists the defined metrics in a {0} account".format(self.product_name)

    def _handle_results(self):
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            metrics = json.loads(self._api_result.text)
            m = []
            for metric in metrics['result']:
                new_metric = self.extractFields(metric)
                m.append(new_metric)

            metrics['result'] = m
            # pretty print the JSON output
            out = json.dumps(metrics, sort_keys=True, indent=4, separators=(',', ': '))
            print(self.colorize_json(out))

