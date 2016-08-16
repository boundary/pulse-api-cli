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
from boundary import MetricCommon
import json
import requests


class MetricList(MetricCommon):
    def __init__(self):
        MetricCommon.__init__(self)
        self._enabled = None
        self._custom = None

    def add_arguments(self):
        MetricCommon.add_arguments(self)
        self.parser.add_argument('-b', '--enabled', dest="enabled", action='store', required=False,
                                 default=None, choices=['true', 'false'],
                                 help='Filter the list of metrics to only return enabled metrics')
        self.parser.add_argument('-c', '--custom', dest="custom", action='store', required=False,
                                 default=None, choices=['true', 'false'],
                                 help='Filter the list of metrics to only return custom metrics')

    def get_arguments(self):
        MetricCommon.get_arguments(self)
        self._enabled = self.args.enabled if self.args.enabled is not None else None
        self._custom = self.args.custom if self.args.custom is not None else None

        self.get_api_parameters()

    def get_api_parameters(self):
        self.path = "v1/metrics"
        self.method = "GET"
        if self._enabled is not None or self._custom is not None:
            self.url_parameters = {}
            if self._enabled is not None:
                self.url_parameters['enabled'] = self._enabled
            if self._custom is not None:
                self.url_parameters['custom'] = self._custom

    def get_description(self):
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
                new_metric = self.extract_fields(metric)
                m.append(new_metric)

            metrics['result'] = m
            # pretty print the JSON output
            out = json.dumps(metrics, sort_keys=True, indent=4, separators=(',', ': '))
            print(self.colorize_json(out))

