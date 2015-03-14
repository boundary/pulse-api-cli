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
import socket
import time

'''
Implements command line utility to add a measurement value to a Boundary account
Uses the following Boundary API:

http://premium-documentation.boundary.com/v1/post/measurements

'''
class MeasurementAdd (ApiCli):
     
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "POST"
        self.path="v1/measurements"
        
        self.metricName = None
        self.measurement = None
        self.source = None
        self.timestamp = None
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metricName',action='store',required=True,metavar='metric_name',help='Metric identifier')
        self.parser.add_argument('-m', '--measurement', dest='measurement',action='store',required=True,metavar="measurement",help='Measurement value')
        self.parser.add_argument('-s', '--source', dest='source',action='store',metavar="source",help='Source of measurement')
        self.parser.add_argument('-d', '--timestamp', dest='timestamp',action='store',metavar="timestamp",help='Time of occurence of the measurement in either epoch seconds or epoch milliseconds')

    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.metricName != None:
            self.metricName = self.args.metricName
            
        if self.args.measurement != None:
            self.measurement = self.args.measurement
            
        if self.args.source != None:
            self.source = self.args.source
        else:
            self.source = socket.gethostname()
            
        if self.args.timestamp != None:
            self.timestamp = self.args.timestamp
        else:
            self.timestamp = int(time.time())
            
        self.data = {"metric": self.metricName,"measure": self.measurement,"source": self.source,"timestamp": self.timestamp}
                     
    def getDescription(self):
        return "Adds a measurement value to a Boundary account"
    
