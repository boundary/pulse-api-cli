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


class EventList(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.path = "v1/events"

    def addArguments(self):
        ApiCli.addArguments(self)

    def getDescription(self):
        return "Lists the events in a {0} account".format(self.product_name)

    def handleResults(self, result):
        # Only process if we get HTTP result of 200
        if result.status_code == http_client.OK:
            out = json.dumps(json.loads(result.text), sort_keys=True, indent=4, separators=(',', ': '))
            print(out)

