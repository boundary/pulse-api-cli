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
Implements command to remove a metric definition from a Boundary account.
"""

from api_cli import ApiCli

"""
Uses the following Boundary API:

https://premium-api.boundary.com/v1/alarm/:alarmId
"""


class AlarmDelete(ApiCli):
    def __init__(self):
        """
        """
        ApiCli.__init__(self)
        self.method = "DELETE"
        self.alarmId = None

    def addArguments(self):
        """
        """
        ApiCli.addArguments(self)
        self.parser.add_argument('-i', '--alarm-id', dest='alarmId', action='store',
                                 required=True, metavar='alarm-id', help='Alarm identifier')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)
        if self.args.alarmId is not None:
            self.alarmId = self.args.alarmId

        self.path = "v1/alarm/{0}".format(self.alarmId)

    def validateArguments(self):
        """
        """
        return ApiCli.validateArguments(self)

    def getDescription(self):
        """
        """
        return "Deletes a metric definition from a Boundary account"