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

import requests
import json
from boundary import MetricCommon


class MetricGet(MetricCommon):
    def __init__(self):
        MetricCommon.__init__(self)
        self.metrics = None

        self._metric_name = None
        self._enabled = None
        self._custom = None

    def addArguments(self):
        MetricCommon.addArguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metric_name', action='store', required=True,
                                 metavar='metric_name', help='Metric identifier')
        self.parser.add_argument('-b', '--enabled', dest="enabled", action='store_true', required=False, default=False,
                                 help='Filter the list of metrics to only return enabled metrics')
        self.parser.add_argument('-c', '--custom', dest="custom", action='store_true', required=False, default=False,
                                 help='Filter the list of metrics to only return custom metrics')

    def getDescription(self):
        return 'Lists the defined metrics in a {0} account'.format(self.product_name)

    def getArguments(self):
        MetricCommon.getArguments(self)

        self._metric_name = self.args.metric_name if self.args.metric_name is not None else None
        self._enabled = self.args.enabled if self.args.enabled is not None else None
        self._custom = self.args.custom if self.args.custom is not None else None

    def get_api_parameters(self):
        self.path = "v1/metrics"
        self.method = "GET"
        self.url_parameters = {'enabled': self._enabled, 'custom': self._custom}

    def _handle_api_results(self):
        pass

    def _handle_results(self, result):
        metric = None
        # Only process if we get HTTP result of 200
        if result.status_code == requests.codes.ok:
            self.metrics = json.loads(result.text)

            # Handle old style metrics
            if 'result' in self.metrics:
                for m in self.metrics['result']:
                    if m['name'] == self.metricName:
                        metric = m
            # Handle new style metrics
            else:
                for key in self.metrics:
                    if key == self.metricName:
                        metric = self.metrics[key]
            # pretty print the JSON output
            if metric is not None:
                out = json.dumps(self.extractFields(metric), sort_keys=True, indent=4, separators=(',', ': '))
                print(self.colorize_json(out))
