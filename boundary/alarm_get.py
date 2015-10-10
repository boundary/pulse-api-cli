#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Implements a command to get the information about an alarm
"""

from boundary import ApiCli

"""
Uses the following Boundary API:

https://premium-api.boundary.com/v1/alarms/search?name=
"""


class AlarmGet(ApiCli):
    def __init__(self):
        """
        """
        ApiCli.__init__(self)
        self.method = "GET"
        self.alarmName = None
        self.alarmId = None

    def addArguments(self):
        """
        """
        ApiCli.addArguments(self)

        # Make these options mutually exclusive where by the user
        # can only specify fetching of an alarm definition by id or name
        group = self.parser.add_mutually_exclusive_group()

        group.add_argument('-i', '--alarm-id', dest='alarmId', action='store',
                                 metavar='alarm-id', help='Alarm identifier')
        group.add_argument('-n', '--alarm-name', dest='alarmName', action='store',
                                 metavar='alarm-name', help='Alarm name')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)

        if self.args.alarmName is not None:
            self.alarmName = self.args.alarmName

        if self.args.alarmId is not None:
            self.alarmId = self.args.alarmId

        if self.alarmId is not None:
            self.path = "v1/alarm/{0}".format(self.alarmId)

        if self.alarmName is not None:
            self.path = "v1/alarms/search"
            self.url_parameters={"name": self.alarmName}

    def validateArguments(self):
        """
        """
        return ApiCli.validateArguments(self)

    def getDescription(self):
        """
        """
        return "Retrieves an alarm definition from a {0} account".format(self.product_name)
