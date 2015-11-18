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


class PluginGet(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        self.path = "v1/plugins"
        self.plugin_name = None

    def add_arguments(self):
        ApiCli.add_arguments(self)

        self.parser.add_argument('-n', '--plugin-Name', dest='plugin_name', action='store', metavar='plugin_name',
                                 required=True, help='Plugin name')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)
        if self.args.plugin_name is not None:
            self.plugin_name = self.args.plugin_name

        self.path = "v1/plugins/{0}".format(self.plugin_name)

    def get_description(self):
        return 'Get the details of a plugin in a {0} account'.format(self.product_name)
