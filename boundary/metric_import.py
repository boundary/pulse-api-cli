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

from api_cli import ApiCli
import json

"""
Class definition for import metric definitions
Sets creates or updates a metric from a JSON file
"""
class MetricImport(ApiCli):

    def __init__(self):
        ApiCli.__init__(self)
        self.metrics = None
        self.path = None
       
    def addArguments(self):
        """
        Configure handling of command line arguments.
        """
        # Call our parent to add the default arguments
        ApiCli.addArguments(self)

        self.parser.add_argument('-f', '--file', dest='path', metavar='path', action='store', required=True, help='Path to JSON file')

    def getArguments(self):
        ApiCli.getArguments(self)
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
        
        if 'result' in self.metrics:
            metrics = self.metrics['result']
        else:
            metrics = self.metrics
            
        for m in metrics:
            self.createUpdate(m)
      
    def callAPI(self):
        self.loadAndParse()
        self.importMetrics()

    def createUpdate(self, metric):
        """
        """
        m = {}
        m['name'] = metric['name']
        if metric['description'] != None:
            m['description'] = metric['description']
      
        if metric['displayName'] != None:
            m['displayName'] = metric['displayName']
      
        if metric['displayNameShort'] != None:
            m['displayNameShort'] = metric['displayNameShort']
          
        if metric['unit'] != None:
            m['unit'] = metric['unit']
    
        if metric['defaultAggregate'] != None:
            m['defaultAggregate'] = metric['defaultAggregate']
          
        if metric['defaultResolutionMS'] != None:
            m['defaultResolutionMS'] = metric['defaultResolutionMS']

        if metric['isDisabled'] != None:
            m['isDisabled'] = metric['isDisabled']
          
        self.path = "v1/metrics/{0}".format(metric['name'])
        self.headers = {'content-type': 'application/json'}
        self.data = json.dumps(m)
