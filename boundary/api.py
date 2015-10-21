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
import json

from six.moves import http_client
from api_cli import ApiCli
from metric_get import MetricDefinition


class API(ApiCli):

    def __init__(self, api_host="premium-api.boundary.com", email=None, api_token=None):
        ApiCli.__init__(self)
        self.path = "v1/metrics"
        self.metrics = None
        self.getEnvironment()
        if api_host is not None:
            self.apihost = api_host
        if email is not None:
            self.email = email
        if api_token is not None:
            self.apitoken = api_token

    def metric_get(self,enabled=False, custom=False):
        """
        Returns a metric definition identified by name
        :param name:
        :return: MetricDefinition
        """
        self.path = 'v1/metrics?enabled={0}&{1}'.format(enabled, custom)
        self.callAPI();
        return MetricDefinition()

    # def handleResults(self, result):
    #     metric = None
    #     # Only process if we get HTTP result of 200
    #     if result.status_code == http_client.OK:
    #         self.metrics = json.loads(result.text)
    #
    #         # Handle old style metrics
    #         if 'result' in self.metrics:
    #             for m in self.metrics['result']:
    #                 if m['name'] == self.metricName:
    #                     metric = m
    #         # Handle new style metrics
    #         else:
    #             for key in self.metrics:
    #                 if key == self.metricName:
    #                     metric = self.metrics[key]
    #         # pretty print the JSON output
    #         if metric is not None:
    #             out = json.dumps(self.extractFields(metric), sort_keys=True, indent=4, separators=(',', ': '))
    #             print(self.colorize_json(out))

if __name__ == "__main__":
    api = API()
    api.metric_get()
