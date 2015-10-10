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
from boundary import AlarmModify


class AlarmUpdate(AlarmModify):
    def __init__(self):
        AlarmModify.__init__(self, True)
        self.alarm_id = None
        self.method = "PUT"

    def addArguments(self):

        self.parser.add_argument('-i', '--alarm-id', dest='alarm_id', action='store', required=True,
                                 metavar='alarm_id', help='Id of the alarm to update')
        self.parser.add_argument('-n', '--alarm-name', dest='alarm_name', action='store',
                                 metavar='alarm_name', help='Name of the alarm')

        AlarmModify.addArguments(self)

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """

        AlarmModify.getArguments(self)

        if self.args.alarm_id is not None:
            self.alarm_id = self.args.alarm_id

        self.path = "v1/alarm/{0}".format(self.alarm_id)

    def getDescription(self):
        return 'Updates an alarm definition in an {0} account'.format(self.product_name)
