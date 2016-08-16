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
import requests

from boundary import ApiCli
from boundary import PluginManifest

"""
Reads the plugin.json manifest file looks up the definition and then outputs a markdown table

Format of output table:

|Metric Name|Metric Identifier|Description
|:-----------|:--------|
"""


class MetricMarkdown(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.metric_definitions = None
        self.dashboards = None
        self.metrics = None
        self.manifest = None
        self.file_path = None
        self.fields = None

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-f', '--file', dest='file_path', action='store', required=False, metavar='path',
                                 help='Path to plugin.json manifest. Defaults to plugin.json')

    def get_arguments(self):
        ApiCli.get_arguments(self)

        if self.args.file_path is None:
            self.file_path = 'plugin.json'
        else:
            self.file_path = self.args.file_path

        self.path = "v1/metrics"

        self.load()

    def get_description(self):
        return 'Generates a README file'

    def handle_sesults(self, result):
        if result.status_code == requests.codes.ok:
            result = json.loads(result.text)
            self.metric_definitions = result['result']

            self.generateMarkdown()
        else:
            pass

    def load(self):
        """
        Read the file and parse JSON into dictionary
        """
        manifest = PluginManifest(self.file_path)
        manifest.get()
        self.manifest = manifest.get_manifest()

    def getMetricDefinition(self, name):
        """
        Looks up the metric definition from the definitions from the API call
        """
        metric = None
        for m in self.metric_definitions:
            if m['name'] == name:
                metric = m
                break
        return metric

    def printMetricsHeader(self, m, d):
        """
        Prints out table header based on the size of the data in columns
        """
        mstr = "Metric Name"
        dstr = "Description"

        print('|{0}{1}|{2}{3}|'.format(mstr, ' ' * (m - len(mstr)), dstr, ' ' * (d - len(dstr))))
        print('|:{0}|:{1}|'.format('-' * (m - 1), '-' * (d - 1)))

    def getDashboardColumnLengths(self):
        return (0, 0)

    def getFieldsColumnLengths(self):
        """
        Gets the maximum length of each column in the field table
        """
        nameLen = 0
        descLen = 0
        for f in self.fields:
            nameLen = max(nameLen, len(f['title']))
            descLen = max(descLen, len(f['description']))
        return (nameLen, descLen)

    def getMetricsColumnLengths(self):
        """
        Gets the maximum length of each column
        """
        displayLen = 0
        descLen = 0
        for m in self.metrics:
            displayLen = max(displayLen, len(m['displayName']))
            descLen = max(descLen, len(m['description']))
        return (displayLen, descLen)

    def escapeUnderscores(self):
        """
        Escape underscores so that the markdown is correct
        """
        new_metrics = []
        for m in self.metrics:
            m['name'] = m['name'].replace("_", "\_")
            new_metrics.append(m)
        self.metrics = new_metrics

    def printFieldsHeader(self, f, d):
        """
        Prints out table header based on the size of the data in columns
        """
        fstr = "Field Name"
        dstr = "Description"
        f = max(f, len(fstr))
        d = max(d, len(dstr))

        print('|{0}{1}|{2}{3}|'.format(fstr, ' ' * (f - len(fstr)), dstr, ' ' * (d - len(dstr))))
        print('|:{0}|:{1}|'.format('-' * (f - 1), '-' * (d - 1)))
        return (f, d)

    def printMetrics(self, m, d):
        """
        Prints out table rows based on the size of the data in columns
        """
        for metric in self.metrics:
            mstr = metric['displayName']
            dstr = metric['description']
            mlen = m - len(mstr)
            dlen = d - len(dstr)
            print("|{0}{1}|{2}{3}|".format(mstr, ' ' * mlen, dstr, ' ' * dlen))

    def printFields(self, f, d):
        """
        Prints out table rows based on the size of the data in columns
        """
        for field in self.fields:
            fstr = field["title"]
            dstr = field["description"]
            flen = f - len(fstr)
            dlen = d - len(dstr)
            print("|{0}{1}|{2}{3}|".format(fstr, ' ' * flen, dstr, ' ' * dlen))

    def generateFieldDefinitions(self):
        manifest_fields = self.manifest['paramSchema']
        fields = []
        for f in manifest_fields:
            fields.append(f)
        self.fields = fields

    def generateMetricDefinitions(self):
        manifest_metrics = self.manifest['metrics']
        metrics = []
        for m in manifest_metrics:
            metric = self.getMetricDefinition(m)
            if metric is None:
                logging.error("metric name: {0} not found\n".format(m))
            else:
                metrics.append(metric)

        self.metrics = metrics

    def generateDashboardDefinitions(self):

        if 'dashboards' in self.manifest:
            dashboards = self.manifest['dashboards']

            dashes = []
            for dashboard in dashboards:
                dashes.append(name)
            self.dashboards = dashes

    def outputFieldMarkdown(self):
        """
        Sends the field definitions ot standard out
        """
        f, d = self.getFieldsColumnLengths()

        fc, dc = self.printFieldsHeader(f, d)
        f = max(fc, f)
        d = max(dc, d)
        self.printFields(f, d)

    def outputMetricMarkdown(self):
        """
        Sends the markdown of the metric definitions to standard out
        """
        self.escapeUnderscores()
        m, d = self.getMetricsColumnLengths()

        self.printMetricsHeader(m, d)
        self.printMetrics(m, d)

    def outputDashboardMarkdown(self):
        f,d = self.getDashboardColumnLengths()

    def outputMarkdown(self):
        """
        Sends the markdown to standard out
        """
        self.outputFieldMarkdown()
        self.outputMetricMarkdown()
        self.outputDashboardMarkdown()

    def generateMarkdown(self):
        """
        Look up each of the metrics and then output in Markdown
        """
        self.generateMetricDefinitions()
        self.generateFieldDefinitions()
        self.generateDashboardDefinitions()
        self.outputMarkdown()


