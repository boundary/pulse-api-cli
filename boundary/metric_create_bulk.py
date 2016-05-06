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
from boundary import MetricCommon
import requests

"""
Class definition for import metric definitions
Sets creates or updates a metric from a JSON file
"""


class MetricCreateBulk(MetricCommon):

    def __init__(self):
        """
        """
        MetricCommon.__init__(self)
        self.method = 'PUT'
        self.metrics = None
        self.file_path = None
        self.v2Metrics = None

    def add_arguments(self):
        """
        Configure handling of command line arguments.
        """
        # Call our parent to add the default arguments
        MetricCommon.add_arguments(self)

        self.parser.add_argument('-f', '--file', dest='file_path', metavar='path', action='store', required=True,
                                 help='Path to JSON file')

    def get_arguments(self):
        """
        """
        MetricCommon.get_arguments(self)
        if self.args.file_path is not None:
            self.file_path = self.args.file_path
        
    def load_and_parse(self):
        """
        Load the metrics file from the given path
        """
        f = open(self.file_path, "r")
        metrics_json = f.read()
        self.metrics = json.loads(metrics_json)

    def import_metrics(self):
        """
        1) Get command line arguments
        2) Read the JSON file
        3) Parse into a dictionary
        4) Create or update definitions using API call
        """

        self.v2Metrics = self.metricDefinitionV2(self.metrics)
        if self.v2Metrics:
            metrics = self.metrics

        else:
            metrics = self.metrics['result']

        # Loop through the metrics and call the API
        # to create/update
        for m in metrics:
            if self.v2Metrics:
                metric = metrics[m]
                metric['name'] = m
            else:
                metric = m
            self.create_update(metric)
      
    def _call_api(self):
        """
        """
        self.load_and_parse()
        self.import_metrics()

    def create_update(self, metric):
        self.path = "v1/metrics/{0}".format(metric['name'])
        self.headers = {'content-type': 'application/json'}
        self.data = json.dumps(metric)
        MetricCommon._call_api(self)

    def _handle_api_results(self):
        pass

    def _handle_results(self):
        """
        Default is to just print the results to standard out
        """
        if self._api_result.status_code != requests.codes.ok:
            print(self.colorize_json(self._api_result.text))

