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
from host_group_modify import HostGroupModify

class HostGroupUpdate (HostGroupModify):
     
    def __init__(self):
        HostGroupModify.__init__(self,True)
        self.method = "PUT"
        
        self.hostGroupId = ""
        
    def addArguments(self):
        HostGroupModify.addArguments(self)
        self.parser.add_argument('-i', '--host-group-id', dest='hostGroupId',action='store',required=True,metavar='host_group_id',help='Host group id to update')
        
    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        HostGroupModify.getArguments(self)
        
        if self.args.hostGroupId != None:
            self.hostGroupId = self.args.hostGroupId
                
        self.path="v1/hostgroup/" + str(self.hostGroupId)
         
    def getDescription(self):
        return "Updates host group definition in a Boundary account"
    