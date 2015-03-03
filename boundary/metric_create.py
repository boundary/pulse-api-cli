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
        self.method = "PUT"
        
        self.name = None
        self.displayName = None
        self.displayNameShort = None
        self.description = None
        self.aggregate = None
        self.unit = None
        self.resolution = None
        self.isDisabled = False
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-m', '--name', dest='name',action='store',required=True,help='Metric identifier')
        self.parser.add_argument('-d', '--display-name', dest='displayName',action='store',help='Metric display name')
        self.parser.add_argument('-s', '--display-name-short', dest='displayNameShort',action='store',help='Metric short display name')
        self.parser.add_argument('-i', '--description', dest='description',action='store',help='Metric description')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate',action='store',help='Metric default aggregate')
        self.parser.add_argument('-u', '--unit', dest='unit',action='store',choices=['sum','avg','max','min'],help='Metric unit')
        self.parser.add_argument('-r', '--resolution', dest='resolution',action='store',help='Metric default resolution')
        self.parser.add_argument('-x', '--is-disabled',dest='isDisabled', action='store_true', help='disable metric')
        
    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.name != None:
            self.name = self.args.name
            
        if self.args.displayName != None:
            self.displayName = self.args.displayName
            
        if self.args.displayNameShort != None:
            self.displayNameShort = self.args.displayNameShort
            
        if self.args.description != None:
            self.description = self.args.description
        
        if self.args.aggregate != None:
            self.aggregate = self.args.aggregate
            
        if self.args.unit != None:
            self.unit = self.args.unit
            
        if self.args.resolution != None:
            self.resolution = self.args.resolution
            
        if self.args.isDisabled != None:
            self.isDisabled = self.args.isDisabled
       
        self.data = {'name': self.name,
                    'displayName': self.displayName,
                    'displayNameShort': self.displayNameShort,
                    'description': self.description,
                    'defaultAggregate': self.aggregate,
                    'unit': self.unit,
                    'defaultResolutionMS': self.resolution,
                    'isDisabled': self.isDisabled}
        self.path = "v1/metrics/{0}".format(self.name)
    
    def validateArguments(self):
        return ApiCli.validateArguments(self)
         
    def getDescription(self):
        return "Creates a new metric definition in an Boundary account"
    