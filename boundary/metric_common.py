#  Copyright 2014-2015 Boundary, Inc.
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
from api_cli import ApiCli


class MetricCommon (ApiCli):
    
    def __init__(self):
        ApiCli.__init__(self)
        
    def extractFields(self, metric):
        '''
        Extract only the required fields for the create/update API call
        '''
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
        return m

    def metricDefintionV2(self,metrics):
        return 'result' not in metrics

