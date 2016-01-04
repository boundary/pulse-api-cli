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

from boundary import MetricCreateBulk


class MetricCreateBatch(MetricCreateBulk):

    def __init__(self):
        MetricCreateBulk.__init__(self)

    def get_description(self):
        return 'Creates multiple metric definitions from a file into a {0} account'.format(self.product_name)

