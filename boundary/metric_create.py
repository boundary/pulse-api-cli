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
class MetricCreate (ApiCli):
     
    def __init__(self):
        ApiCli.__init__(self)
        self.path = "v1/metrics"
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-m', '--name', dest='name',action='store',help='Metric identifier')
        self.parser.add_argument('-d', '--display-name', dest='display_name',action='store',help='Metric display name')
        self.parser.add_argument('-s', '--display-name-short', dest='display_name_short',action='store',help='Metric short display name')
        self.parser.add_argument('-i', '--description', dest='description',action='store',help='Metric description')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate',action='store',help='Metric default aggregate')
        self.parser.add_argument('-u', '--unit', dest='unit',action='store',help='Metric unit')
        self.parser.add_argument('-r', '--resolution', dest='resolution',action='store',help='Metric resolution')
        
    def getArguments(self):
        ApiCli.getArgs(self)
        if self.args.name != None:
            self.name = self.args.name

            
         
    def getDescription(self):
        return "Creates a new metric definition in an Boundary account"
    