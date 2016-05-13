#
# Copyright 2016 BMC Software, Inc.
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


class PropertyHandler(object):
    def __init__(self):
        self._properties = None

    def _process_properties(self, properties):
        """
        Transforms the command line properties into python dictionary
        :return:
        """
        if properties is not None:
            self._properties = {}
            for p in properties:
                d = p.split('=')
                self._properties[d[0]] = d[1]

    def _add_property_argument(self, parser, help_text):

        parser.add_argument('-p', '--property', dest='properties', action='append',
                            required=False, metavar='property=value', help=help_text)
