#!/usr/bin/python
##
## Copyright 2014-2015 Boundary, Inc.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##

'''
Exports metrics from a Boundary account with the ability to filter on metric name
'''
from api_cli import ApiCli
import json
import logging
import re
import sys

class MetricExport(ApiCli):

    def __init__(self):
        '''
        Initialize the instance
        '''
        ApiCli.__init__(self)
        self.path = "v1/metrics"
        self.metrics = None
        self.patterns = None
        self.filter_expression = None

    def getDescription(self):
        return 'Export the metric definitions from a Boundary account'

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-p','--pattern',metavar='pattern',dest='patterns',action='store',
                                 help='regular expression pattern to use search the name of the metric')
        
    def getArguments(self):
        ApiCli.getArguments(self)
        
        if self.args.patterns:
            self.filter_expression = re.compile(self.args.patterns)

    def extractFields(self, metric):
        '''
        Extract only the required fields for the create/update API call
        '''
        m = {}
        try:
            m['name'] = metric['name']
            m['description'] = metric['description']
            m['displayName'] = metric['displayName']
            m['displayNameShort'] = metric['displayNameShort']
            m['unit'] = metric['unit']
            m['defaultAggregate'] = metric['defaultAggregate']
            m['defaultResolutionMS'] = metric['defaultResolutionMS']
            m['isDisabled'] = metric['isDisabled']
        except KeyError as e:
            logging.error("Missing field \"" + e.message + "\" in result")
            sys.exit(1)

        return m

    def extract(self, metrics):
        '''
         Extract required fields
        '''
        new_metrics = []
        for m in metrics:
            new_metrics.append(self.extractFields(m))
        return new_metrics

    def filter(self):
        '''
         Apply the criteria to filter out on the metrics required
        '''
        new_metrics = []
        if self.filter_expression != None:
            metrics = self.metrics['result']
            for m in metrics:
                if self.filter_expression.search(m['name']):
                    new_metrics.append(m)
        else:
            new_metrics = self.metrics['result']

        self.metrics['result'] = self.extract(new_metrics)

    def handleResults(self,result):
        '''
        Call back function to be implemented by the CLI.
        '''
        self.metrics = json.loads(result.text)
        self.filter()
        out = json.dumps(self.metrics, sort_keys=True, indent=4,separators=(',', ': '))
        print out






            
