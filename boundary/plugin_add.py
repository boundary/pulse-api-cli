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
from plugin_base import PluginBase

class PluginAdd (PluginBase):
     
    def __init__(self):
        PluginBase.__init__(self)
        self.method = "PUT"
        self.path="v1/plugins/private"
        
        self.pluginName = None
        self.organizationName = None
        self.repositoryName = None
        
    def addArguments(self):
        PluginBase.addArguments(self)
        self.parser.add_argument('-o', '--organization-name', dest='organizationName',action='store',required=True,metavar="organization_name",
                                 help='Name of the github user or organization')
        self.parser.add_argument('-r', '--repository-name', dest='repositoryName',action='store',required=True,metavar="respository_name",
                                 help='Name of the github user or organization')

    def getArguments(self):
        '''
        Extracts the specific arguments of this CLI
        '''
        PluginBase.getArguments(self)
        if self.args.organizationName != None:
            self.organizationName = self.args.organizationName
        if self.args.repositoryName != None:
            self.repositoryName = self.args.repositoryName
            
        self.path = "v1/plugins/private/{0}/{1}/{2}".format(self.pluginName,self.organizationName,self.repositoryName)
         
    def getDescription(self):
        return "Imports a meter plugin from a github repository into a Boundary account"
    