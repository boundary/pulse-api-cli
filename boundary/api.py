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
import requests

from api_cli import ApiCli


class Metric:

    def __init__(self, display_name=None):
        self._display_name = display_name

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def method(self, value):
        self._display_name = value

    def __repr__(self):
        return 'Metric(display_name="{0}")'.format(self._display_name)


class Metrics:

    def __init__(self, metrics):
        self._metrics = metrics

    def __len__(self):
        return len(self._metrics)

    def __getitem__(self, position):
        metric_values = self._metrics["result"][position]
        metric = None
        if metric_values is not None:
            metric = Metric(display_name=metric_values["displayName"])

        return metric

    def __str__(self):
        print("foo")
        return str(self._metrics)


class API(ApiCli):

    def __init__(self, api_host="premium-api.boundary.com", email=None, api_token=None):
        ApiCli.__init__(self)
        self.metrics = None
        self.getEnvironment()
        if api_host is not None:
            self.apihost = api_host
        if email is not None:
            self.email = email
        if api_token is not None:
            self.apitoken = api_token

    def metric_get(self, enabled=False, custom=False):
        """
        Returns a metric definition identified by name
        :param name:
        :return: MetricDefinition
        """
        self.path = 'v1/metrics?enabled={0}&{1}'.format(enabled, custom)
        self.callAPI();
        return self.metrics

    def handleResults(self, result):
        # Only process if we get HTTP result of 200
        if result.status_code == requests.codes.ok:
            metrics = json.loads(result.text)
            self.metrics = Metrics(metrics)


if __name__ == "__main__":
    api = API()
    api.metric_get()
