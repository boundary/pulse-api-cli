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
from six.moves import http_client
import json


class EventGet(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.event_id = None

    def addArguments(self):
        ApiCli.addArguments(self)

        self.parser.add_argument('-i', '--event-id', dest='event_id', action='store', required=True,
                                 metavar='event_id', help='Host group the alarm applies to')

    def getArguments(self):

        if self.args.event_id is not None:
            self.event_id = self.args.event_id

        self.path = "v1/events/{0}".format(self.event_id)

    def getDescription(self):
        return "Gets a single event by id from a Boundary account"

    def handleResults(self, result):
        # Only process if we get HTTP result of 200
        if result.status_code == http_client.OK:
            out = json.dumps(json.loads(result.text), sort_keys=True, indent=4, separators=(',', ': '))
            print(self.colorize_json(out))
