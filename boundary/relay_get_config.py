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


class RelayGetConfig(ApiCli):

    def __init__(self):
        ApiCli.__init__(self)

        self.meter = None
        self.since = None

    def addArguments(self):
        """
        """
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--name', metavar='meter_name', dest='meter', action='store', required=True,
                                 help='Name of the meter to set plugin configuration information')

        self.parser.add_argument('-s', '--since', metavar='timestamp', dest='since', action='store', required=False,
                                 help='Unix timestamp of when configuration was last checked. '
                                      + 'If configuration has not changed, null is returned.')

    def getArguments(self):
        """
        """
        ApiCli.getArguments(self)

        if self.args.meter is not None:
            self.meter = self.args.meter

        if self.args.since is not None:
            self.since = self.args.since

        self.path = 'v1/relays/{0}/config'.format(self.meter)

        if self.since is not None:
            self.url_parameters = {"since": self.since}

    def getDescription(self):
        return "Returns relay configuration from a Boundary account"
