#
# Copyright 2015 BMC Software, Inc.
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
from boundary import AlarmModify


class AlarmCreate(AlarmModify):
    def __init__(self, **kwargs):
        AlarmModify.__init__(self, False)
        self._kwargs = kwargs
        self.method = "POST"
        self._alarm_result = None

    def add_arguments(self):

        self.parser.add_argument('-n', '--alarm-name', dest='alarm_name', action='store', required=True,
                                 metavar='alarm_name', help='Name of the alarm')

        AlarmModify.add_arguments(self)

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        AlarmModify.get_arguments(self)

    def get_description(self):
        return 'Creates an alarm definition in an {0} account'.format(self.product_name)


