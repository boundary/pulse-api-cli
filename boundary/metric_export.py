# 
#  Copyright 2015 BMC Software, Inc.
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
import re

"""
Exports metrics from a Boundary account with the ability to filter on metric name
"""


class MetricExport(MetricCommon):

    def __init__(self):
        """
        Initialize the instance
        """
        MetricCommon.__init__(self)
        self.method = "GET"
        self.path = "v1/metrics"
        self.metrics = None
        self.patterns = None
        self.filter_expression = None

    def get_description(self):
        """
        """
        return 'Export the metric definitions from a {0} account'.format(self.product_name)

    def add_arguments(self):
        """
        """
        MetricCommon.add_arguments(self)
        self.parser.add_argument('-p', '--pattern', metavar='pattern', dest='patterns', action='store',
                                 help='regular expression pattern to use search the name of the metric')
        
    def get_arguments(self):
        """
        """
        MetricCommon.get_arguments(self)
        
        if self.args.patterns:
            self.filter_expression = re.compile(self.args.patterns)

    def extract_dictionary(self, metrics):
        """
        Extract required fields from an array
        """
        new_metrics = {}
        for m in metrics:
            metric = self.extract_fields(m)
            new_metrics[m['name']] = metric
        return new_metrics

    def filter(self):
        """
        Apply the criteria to filter out on the metrics required
        """
        if self.filter_expression is not None:
            new_metrics = []
            metrics = self.metrics['result']
            for m in metrics:
                if self.filter_expression.search(m['name']):
                    new_metrics.append(m)
        else:
            new_metrics = self.metrics['result']

        self.metrics = self.extract_dictionary(new_metrics)

    def _handle_results(self):
        """
        Call back function to be implemented by the CLI.
        """
        
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            self.metrics = json.loads(self._api_result.text)
            self.filter()
            out = json.dumps(self.metrics, sort_keys=True, indent=4, separators=(',', ': '))
            print(self.colorize_json(out))
