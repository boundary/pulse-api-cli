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

class MetricRef (ApiCli):
     
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "POST"
        self.path = "v1/metrics/ref"
        self.metricName = None
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metricName',action='store',required=True,metavar='metric_name',help='Metric identifier')
        
    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.metricName != None:
            self.metricName = self.args.metricName            
       
        self.data = {'metric': self.metricName}
        self.headers = {'Content-Type': 'application/json'}
    
    def validateArguments(self):
        '''
        If the metric name is not set then there is no use in proceeding
        with the REST call
        '''
        if self.metricName == None:
            self.setErrorMessage("Metric name not specified")
            return False;
        return ApiCli.validateArguments(self)
         
    def getDescription(self):
        return "Adds a reference to a metric definition in another Boundary account to a Boundary account"
    