#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from boundary import ApiCli


class RelaySetConfig(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = 'PUT'
        self.file = None

    def addArguments(self):
        """
        """
        ApiCli.addArguments()

        self.parser.add_argument('-f', '--file', metavar='path', dest='file', action='store', required=True,
                                 help='Name of the meter to get plugin configuration information')

    def getArguments(self):
        ApiCli.getArguments()

        if self.args.file is not None:
            self.file = self.args.path

        self.path = 'v1/relays/{0}/config'.format(self.meter)

    def getDescription(self):
        return "Returns relay configuration from a Boundary account"
