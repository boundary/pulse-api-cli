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
"""
Implements command to remove a metric definition from a Boundary account.
"""

from boundary import ApiCli

"""
Uses the following Boundary API:

http://premium-documentation.boundary.com/v1/delete/metrics/:metric
"""


class MetricDelete(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "DELETE"
        self.metric_name = None

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metric_name', action='store', required=True,
                                 metavar='metric_name', help='Metric identifier')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)
        if self.args.metric_name != None:
            self.metric_name = self.args.metric_name

        self.path = "v1/metrics/{0}".format(self.metricName)

    def validateArguments(self):
        return ApiCli.validateArguments(self)

    def getDescription(self):
        return 'Deletes a metric definition from a {0} account'.format(self.product_name)
