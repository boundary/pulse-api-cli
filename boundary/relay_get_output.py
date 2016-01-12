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


class RelayGetOutput(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self._meter = None
        self._since = None

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-n', '--name', metavar='meter_name', dest='meter', action='store', required=True,
                                 help='Name of the meter to get output information')

        self.parser.add_argument('-s', '--since', metavar='since', dest='since', action='store', required=False,
                                 default=1,
                                 help='Pull since items from end of log')

    def get_arguments(self):
        ApiCli.get_arguments(self)

        self._meter = self.args.meter if self.args.meter is not None else None
        self._since = self.args.since if self.args.since is not None else None

        self.method = 'GET'
        self.path = 'v1/relays/{0}/output/{1}'.format(self._meter, self._since)


    def get_description(self):
        return 'Queries for relay output messages in a {0} account'.format(self.product_name)
