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

import json
import logging

"""
Reads and provides access to a plugin.json file the manifest of plugins.
"""


class PluginManifest(object):
    def __init__(self, path="plugin.json"):
        """
        Initialize the PluginManifest instance
        """
        self.path = path
        self.manifest_json = None
        self.manifest = None

    def get_metric_names(self):
        """
        Returns the list of metrics associated with the plugin manifest
        """
        return self.manifest['metrics']

    def read(self):
        """
        Load the metrics file from the given path
        """
        f = open(self.path, "r")
        self.manifest_json = f.read()

    def parse(self):
        """
        Parses the manifest JSON into a dictionary
        """
        self.manifest = json.loads(self.manifest_json)

    def load(self):
        """
        Read the JSON file and parse into a dictionary
        """
        self.read()
        self.parse()

    @property
    def command(self):
        return self.manifest['command']

    @property
    def command_lua(self):
        return self.manifest['command_lua']

    @property
    def description(self):
        return self.manifest['description']

    @property
    def icon(self):
        return self.manifest['icon']

    @property
    def ignore(self):
        return self.manifest['ignore']

    @property
    def metrics(self):
        return self.manifest['metrics']

    @property
    def name(self):
        logging.debug(self.manifest)
        return self.manifest['name']

    @property
    def param_array(self):
        return self.manifest['paramArray']

    @property
    def post_extract(self):
        return self.manifest['postExtract']

    @property
    def post_extract_lua(self):
        return self.manifest['postExtract_lua']

    @property
    def tags(self):
        return self.manifest['tags']

    @property
    def version(self):
        return self.manifest['version']

    def get_manifest(self):
        """
        Returns the dictionary from the parse JSON plugin manifest
        """
        return self.manifest
