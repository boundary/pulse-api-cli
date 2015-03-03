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

class MetricGet (ApiCli):
     
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        
        self.name = ""
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-m', '--name', dest='name',action='store',required=True,help='Metric identifier')
        self.parser.add_argument('-b', '--begin', dest='begin',action='store',help='Start time')
        self.parser.add_argument('-n', '--end', dest='end',action='store',help='Start time')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate',action='store',help='End time')

        
    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.name != None:
            self.name = self.args.name
            
        self.path = "v1/metrics/{0}".format(self.name)
         
    def getDescription(self):
        return "Creates a new metric definition in an Boundary account"
    