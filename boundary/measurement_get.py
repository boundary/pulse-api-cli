###
### Copyright 2014-2015 Boundary, Inc.
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###     http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
###
from api_cli import ApiCli

class MeasurementGet (ApiCli):
     
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        self.metricName = None
        self.source = None
        self.aggregate = None
        self.start = None
        self.end = None
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--name', dest='metricName',action='store',required=True,metavar="metric_name",help='Metric identifier')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate',action='store',choices=['sum','avg','max','min'],required=True,metavar='aggregate',help='Metric default aggregate')
        self.parser.add_argument('-s', '--source', dest='source',action='store',metavar="source",help='Source of measurement')
        self.parser.add_argument('-b', '--start', dest='start',action='store',required=True,metavar="start",help='Start of time range')
        self.parser.add_argument('-d', '--end', dest='end',action='store',required=True,metavar="end",help='End of time range')

    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.metricName != None:
            self.metricName = self.args.metricName
        if self.args.source != None:
            self.source = self.args.source
        if self.args.aggregate != None:
            self.aggregate = self.args.aggregate
        if self.args.start != None:
            self.start = self.args.start
        if self.args.end != None:
            self.end = self.args.end
            
        self.path = "v1/measurements/{0}".format(self.metricName)
        self.url_parameters = {"source": self.source, "start": self.start,"end": self.end, "agg": self.aggregate }
         
    def getDescription(self):
        return "Retrieves measurement values from a metric in a Boundary account"
    