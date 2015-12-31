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
import requests
import json
from boundary import MetricCommon


class MetricGet(MetricCommon):
    def __init__(self):
        MetricCommon.__init__(self)
        self._metrics = None
        self._metric_name = None

    def add_arguments(self):
        MetricCommon.add_arguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metric_name', action='store', required=True,
                                 metavar='metric_name', help='Metric identifier')

    def get_description(self):
        return 'Get a metric definition from a {0} account'.format(self.product_name)

    def get_arguments(self):
        MetricCommon.get_arguments(self)
        self._metric_name = self.args.metric_name if self.args.metric_name is not None else None
        self.get_api_parameters()

    def get_api_parameters(self):
        self.path = "v1/metrics"
        self.method = "GET"

    def _handle_api_results(self):
        pass

    def _handle_results(self):
        metric = None
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            self._metrics = json.loads(self._api_result.text)

            # Handle old style metrics
            if 'result' in self._metrics:
                for m in self._metrics['result']:
                    if m['name'] == self._metric_name:
                        metric = m
            # Handle new style metrics
            else:
                for key in self._metrics:
                    if key == self._metric_name:
                        metric = self._metrics[key]
            # pretty print the JSON output
            if metric is not None:
                out = json.dumps(self.extract_fields(metric), sort_keys=True, indent=4, separators=(',', ': '))
                print(self.colorize_json(out))
