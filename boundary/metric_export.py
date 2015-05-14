#!/usr/bin/python
# 
#  Copyright 2014-2015 Boundary, Inc.
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

"""
Exports metrics from a Boundary account with the ability to filter on metric name
"""
from six.moves import http_client
from metric_common import MetricCommon
import json
import re


class MetricExport(MetricCommon):

    def __init__(self):
        """
        Initialize the instance
        """
        MetricCommon.__init__(self)
        self.path = "v1/metrics"
        self.metrics = None
        self.patterns = None
        self.filter_expression = None

    def getDescription(self):
        """
        """
        return 'Export the metric definitions from a Boundary account'

    def addArguments(self):
        """
        """
        MetricCommon.addArguments(self)
        self.parser.add_argument('-p', '--pattern', metavar='pattern', dest='patterns', action='store',
                                 help='regular expression pattern to use search the name of the metric')
        
    def getArguments(self):
        """
        """
        MetricCommon.getArguments(self)
        
        if self.args.patterns:
            self.filter_expression = re.compile(self.args.patterns)

    def extractFields(self, metric):
        """
        Extract only the required fields for the create/update API call
        """
        m = {}
        if 'name' in metric:
            m['name'] = metric['name']
        if 'description' in metric:
            m['description'] = metric['description']
        if 'displayName' in metric:
            m['displayName'] = metric['displayName']
        if 'displayNameShort' in metric:
            m['displayNameShort'] = metric['displayNameShort']
        if 'unit' in metric:
            m['unit'] = metric['unit']
        if 'defaultAggregate' in metric:
            m['defaultAggregate'] = metric['defaultAggregate']
        if 'defaultResolutionMS' in metric:
            m['defaultResolutionMS'] = metric['defaultResolutionMS']
        if 'isDisabled' in metric:
            m['isDisabled'] = metric['isDisabled']
        return m

    def extractArray(self, metrics):
        """
        Extract required fields from an array
        """
        new_metrics = []
        for m in metrics:
            new_metrics.append(self.extractFields(m))
        return new_metrics
    
    def extractDictionary(self, metrics):
        """
        Extract required fields from a dictionary
        """
        new_metrics = {}
        for key in metrics:
            new_metrics[key] = self.extractFields(metrics[key])
        return new_metrics
    
    def filterArray(self):
        """
        """
        if self.filter_expression != None:
            new_metrics = []
            metrics = self.metrics['result']
            for m in metrics:
                if self.filter_expression.search(m['name']):
                    new_metrics.append(m)
        else:
            new_metrics = self.metrics['result']

        self.metrics = self.extractArray(new_metrics)
        
    def filterDictionary(self):
        """
        """
        if self.filter_expression != None:
            new_metrics = {}
            print(type(self.metrics))
            for key in self.metrics:
                if self.filter_expression.search(key):
                    new_metrics[key] = self.metrics[key];
        else:
            new_metrics = self.metrics

        self.metrics = self.extractDictionary(new_metrics)

    def filter(self):
        """
        Apply the criteria to filter out on the metrics required
        """
        
        # Older format which uses an array to contain the metric definitions
        if 'result' in self.metrics:
            self.filterArray()
        else:
            # Handle new format which uses a hash to store a collection of definitions
            self.filterDictionary()

    def handleResults(self, result):
        """
        Call back function to be implemented by the CLI.
        """
        
        # Only process of we get HTTP result of 200
        if result.status_code == http_client.OK:
            self.metrics = json.loads(result.text)
            self.filter()
            out = json.dumps(self.metrics, sort_keys=True, indent=4, separators=(',', ': '))
            print(out)