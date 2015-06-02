#!/usr/bin/env python
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

from metric_common import MetricCommon
import json
from six.moves import http_client

"""
Class definition for import metric definitions
Sets creates or updates a metric from a JSON file
"""


class MetricCreateBatch(MetricCommon):

    def __init__(self):
        """
        """
        MetricCommon.__init__(self)
        self.method = 'PUT'
        self.metrics = None
        self.path = None
        self.v2Metrics = None
       
    def addArguments(self):
        """
        Configure handling of command line arguments.
        """
        # Call our parent to add the default arguments
        MetricCommon.addArguments(self)

        self.parser.add_argument('-f', '--file', dest='path', metavar='path', action='store', required=True, help='Path to JSON file')

    def getArguments(self):
        """
        """
        MetricCommon.getArguments(self)
        if self.args.path is not None:
            self.path = self.args.path
        
    def loadAndParse(self):
        """
        Load the metrics file from the given path
        """
        f = open(self.path, "r")
        metrics_json = f.read()
        self.metrics = json.loads(metrics_json)

    def importMetrics(self):
        """
        1) Get command line arguments
        2) Read the JSON file
        3) Parse into a dictionary
        4) Create or update definitions using API call
        """

        self.v2Metrics = self.metricDefintionV2(self.metrics)
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
            self.createUpdate(metric)
      
    def callAPI(self):
        """
        """
        self.loadAndParse()
        self.importMetrics()

    def createUpdate(self, metric):
        """
        """
        self.path = "v1/metrics/{0}".format(metric['name'])
        self.headers = {'content-type': 'application/json'}
        self.data = json.dumps(metric)
        MetricCommon.callAPI(self)

    def handleResults(self, result):
        """
        Default is to just print the results to standard out
        """
        if result.status_code != http_client.OK:
            print(result.text)

