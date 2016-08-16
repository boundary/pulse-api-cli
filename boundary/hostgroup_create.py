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
from boundary import HostgroupModify


class HostgroupCreate(HostgroupModify):
    def __init__(self):
        HostgroupModify.__init__(self, False)
        self.path = "v1/hostgroups"
        self.sources = None

    def add_arguments(self):
        HostgroupModify.add_arguments(self)

        self.parser.add_argument('-n', '--host-group-name', dest='host_group_name', action='store', required=True,
                                 metavar="host_group_name", help='Host group name')

        self.parser.add_argument('-s', '--sources', dest='sources', action='store', required=True, metavar='sources',
                                 help='Comma separated sources to add to the host group. If empty adds all hosts.')

    def get_description(self):
        return "Creates host group definition in a {0} account".format(self.product_name)
