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
from boundary import MetricModify

class MetricCreate (MetricModify):
     
    def __init__(self):
        """
        """
        MetricModify.__init__(self)
        self.method = "POST"
        self.metricName = None
        self.displayName = None
        self.displayNameShort = None
        self.description = None
        self.aggregate = None
        self.unit = None
        self.resolution = None
        self.isDisabled = None

        self.cli_description = "Creates a new metric definition in an Boundary account"

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        MetricModify.getArguments(self)

        self.path = "v1/metrics"
         
    def getDescription(self):
        """
        """
        return "Creates a new metric definition in an Boundary account"

