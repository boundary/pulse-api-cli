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

class MetricUpdate (MetricModify):
     
    def __init__(self):
        """
        """
        MetricModify.__init__(self)
        self.method = "PUT"
        self.description = "Updates a metric definition in an Boundary account"
         
    def getDescription(self):
        """
        """
        return "Updates a metric definition in an Boundary account"
