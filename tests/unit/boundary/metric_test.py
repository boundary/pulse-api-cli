#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class MetricTest(object):

    @staticmethod
    def metric_assert(self,
                      metric,
                      display_name,
                      display_name_short,
                      description,
                      unit,
                      aggregate,
                      resolution,
                      disabled):
        self.assertEqual(display_name, metric['displayName'])
        self.assertEqual(display_name_short, metric['displayNameShort'])
        self.assertEqual(description, metric['description'])
        self.assertEqual(unit, metric['unit'])
        self.assertEqual(aggregate, metric['defaultAggregate'])
        self.assertEqual(resolution, metric['defaultResolutionMS'])
        self.assertEqual(disabled, metric['isDisabled'])
