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
from six.moves import http_client
from metric_common import MetricCommon
import json

class MetricGet (MetricCommon):
     
    def __init__(self):
        MetricCommon.__init__(self)
        self.path = "v1/metrics"
        
    def addArguments(self):
        MetricCommon.addArguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metricName', action='store', required=True, metavar='metric_name', help='Metric identifier')
        
    def getDescription(self):
        return "Lists the defined metrics in a Boundary account"
    
    def getArguments(self):
        MetricCommon.getArguments(self)
        
        if self.args.metricName != None:
            self.metricName = self.args.metricName
    
    def handleResults(self, result):
        metric = None
        # Only process of we get HTTP result of 200
        if result.status_code == http_client.OK:
            self.metrics = json.loads(result.text)
            
            # Handle old style metrics
            if 'result' in self.metrics:
                for m in self.metrics['result']:
                    if m['name'] == self.metricName:
                        metric = m
            # Handle new style metrics
            else:
                for key in self.metrics:
                    if key == self.metricName:
                        metric = self.metrics[key]
            # pretty print the JSON output
            out = json.dumps(self.extractFields(metric), sort_keys=True, indent=4, separators=(',', ': '))
            print out
