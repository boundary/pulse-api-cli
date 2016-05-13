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


class Metric:
    def __init__(self, display_name=None):
        """
        :param display_name:
        :return:
        """
        self._display_name = display_name

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
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
        return str(self._metrics)


class MetricCommon (ApiCli):
    
    def __init__(self):
        ApiCli.__init__(self)
        
    def extract_fields(self, metric):
        """
        Extract only the required fields for the create/update API call
        """
        m = {}
        if 'name' in metric:
            m['name'] = metric['name']
        if 'description' in metric:
            m['description'] = metric['description']
        if 'displayName' in metric:
            m['displayName'] = metric['displayName']
        if 'displayNameShort' in metric:
            m['displayNameShort'] = metric['displayNameShort']
        if 'unit' in metric:
            m['unit'] = metric['unit']
        if 'defaultAggregate' in metric:
            m['defaultAggregate'] = metric['defaultAggregate']
        if 'defaultResolutionMS' in metric:
            m['defaultResolutionMS'] = metric['defaultResolutionMS']
        if 'isDisabled' in metric:
            m['isDisabled'] = metric['isDisabled']
        if 'isBuiltin' in metric:
            m['isBuiltin'] = metric['isBuiltin']
        if 'type' in metric:
            m['type'] = metric['type']
        return m

    def metricDefinitionV2(self, metrics):
        return 'result' not in metrics

