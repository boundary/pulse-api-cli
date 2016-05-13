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

from boundary import ApiCli


class RelaySetConfig(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = 'PUT'
        self._file = None
        self._meter = None

    def add_arguments(self):
        """
        """
        ApiCli.add_arguments(self)

        self.parser.add_argument('-f', '--file', metavar='path', dest='file', action='store', required=True,
                                 help='Name of the meter to get plugin configuration information')

    def get_arguments(self):
        ApiCli.get_arguments(self)

        if self.args.file is not None:
            self._file = self.args.path

        self.path = 'v1/relays/{0}/config'.format(self._meter)

    def get_description(self):
        return 'Sets the configuration of a relay in a {0} account'.format(self.product_name)
