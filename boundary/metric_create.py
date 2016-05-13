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
from boundary import MetricModify


class MetricCreate (MetricModify):
     
    def __init__(self):
        """
        """
        MetricModify.__init__(self, False)
        self.method = "POST"

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        MetricModify.get_arguments(self)

        self.path = "v1/metrics"
         
    def get_description(self):
        """
        """
        return 'Creates a new metric definition in an {0} account'.format(self.product_name)

