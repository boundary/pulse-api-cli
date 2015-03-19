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

class AlarmCreate (ApiCli):
     
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "POST"
        
        self.alarmName = None
        self.metricName = None
        self.aggregate = None
        self.operation = None
        self.resolution = None
        self.isDisabled = False
        
        self.intervals = {"1 second": 1,
                          "15 seconds": 15,
                          "1 minute": 60,
                          "5 minutes": 900,
                          "1 hour": 3600}
        
        
    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--alarm-name', dest='alarmName',action='store',required=True,
                                 metavar='alarm_name',help='Name of the alarm')
        self.parser.add_argument('-m', '--metric', dest='metricName',action='store',
                                 metavar='display_name',help='Name of the metric to alarm')
        self.parser.add_argument('-g', '--trigger-aggregate', dest='aggregate',action='store',choices=['sum','avg','max','min'],
                                 metavar='aggregate',help='Metric aggregate to alarm upon')
        self.parser.add_argument('-o', '--trigger-operation', dest='operation',action='store',choices=['eq','gt','lt'],
                                 metavar='operation',help='Trigger threshold comparison')
        self.parser.add_argument('-v', '--trigger-threshold', dest='triggerThreshold',action='store',metavar='value',help='Trigger threshold value')
        self.parser.add_argument('-r', '--trigger-interval', dest='triggerInterval',action='store',required=True,
                                 choices=['1 second', '15 seconds', '1 minute', '5 minutes','1 hour'],
                                 metavar='interval',help='Interval to alarm on, can be one of: "1 second","15 seconds","1 minute","5 minutes","1 hour"')
        self.parser.add_argument('-i','--host-group-id',dest='hostGroupId',action='store',metavar='hostgroup_id',
                                 help='Host group the alarm applies to')
        self.parser.add_argument('-d','--note',dest='note',action='store',metavar='note',
                                 help='A description or resolution of the alarm')
        self.parser.add_argument('-p', '--per-host-notify', dest='pertHostNotify',action='store_true',
                                 help='An alarm by default will run the associated actions when any server in the host group violates the threshold, and then at the end when all servers are back within the threshold. If perHostNotify is set to true, the actions will run when ANY server in the group violates and falls back within the threshold.')
        self.parser.add_argument('-x', '--is-disabled',dest='isDisabled',action='store_true',help='Enable or disable the alarm')
        
    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        ApiCli.getArguments(self)
        if self.args.metricName != None:
            self.metricName = self.args.metricName
            
        if self.args.displayName != None:
            self.displayName = self.args.displayName
        else:
            self.displayName = self.metricName
                        
        if self.args.displayNameShort != None:
            self.displayNameShort = self.args.displayNameShort
        else:
            self.displayNameShort = self.metricName
            
        if self.args.description != None:
            self.description = self.args.description
        else:
            self.description = self.metricName
                    
        if self.args.aggregate != None:
            self.aggregate = self.args.aggregate
        else:
            self.aggregate = "ave"
            
        if self.args.unit != None:
            self.unit = self.args.unit
        else:
            self.unit = "number"
            
        if self.args.resolution != None:
            self.resolution = self.args.resolution
        else:
            self.resolution = 1000
            
        if self.args.isDisabled != None:
            self.isDisabled = self.args.isDisabled
            
       
        self.data = {'name': self.metricName,
                    'displayName': self.displayName,
                    'displayNameShort': self.displayNameShort,
                    'description': self.description,
                    'defaultAggregate': self.aggregate,
                    'unit': self.unit,
                    'defaultResolutionMS': self.resolution,
                    'isDisabled': self.isDisabled}
        self.path = "v1/metrics/{0}".format(self.metricName)
    
    def validateArguments(self):
        return ApiCli.validateArguments(self)
         
    def getDescription(self):
        return "Creates a new metric definition in an Boundary account"
    