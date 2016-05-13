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
import string
from datetime import datetime
from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import (Element, SubElement, Comment)

import requests
from boundary import ApiCli
from dateutil import parser

"""
Gets measurements from a Boundary account
"""


class MeasurementGet(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self._indent = 4
        self.method = "GET"
        self._metric_name = None
        self.format = None
        self.date_format = None
        # Default to 1 second sample period
        self.sample = 1
        self.source = None
        self.aggregate = None
        self.startTime = None
        self.stopTime = None
        self.now = datetime.now()

    def add_arguments(self):
        """
        Add specific command line arguments for this command   
        """

        # Call our parent to add the default arguments
        ApiCli.add_arguments(self)

        # Command specific arguments
        self.parser.add_argument('-f', '--format', dest='format', action='store', required=False,
                                 choices=['csv', 'json', 'raw', 'xml'], help='Output format. Default is raw')
        self.parser.add_argument('-n', '--name', dest='metric_name', action='store', required=True,
                                 metavar="metric_name", help='Metric identifier')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate', action='store', required=False,
                                 choices=['sum', 'avg', 'max', 'min'], help='Metric default aggregate')
        self.parser.add_argument('-r', '--sample', dest='sample', action='store', type=int, metavar="sample",
                                 help='Down sample rate sample in seconds')
        self.parser.add_argument('-s', '--source', dest='source', action='store', metavar="source", required=True,
                                 help='Source of measurement')
        self.parser.add_argument('-b', '--start', dest='start', action='store', required=True, metavar="start",
                                 help='Start of time range as ISO 8601 string or epoch seconds')
        self.parser.add_argument('-d', '--end', dest='end', action='store', metavar="end", required=False,
                                 help='End of time range as ISO 8601 string or epoch seconds')

        self.parser.add_argument('-o', '--date-format', dest='date_format', action='store', metavar="format",
                                 required=False,
                                 help='For CSV, JSON, and XML output formats dates (see Python date.strftime). ' +
                                      'Default format is %%s')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)
        if self.args.metric_name is not None:
            self._metric_name = self.args.metric_name

        if self.args.sample is not None:
            self.sample = self.args.sample

        if self.args.source is not None:
            self.source = self.args.source
        else:
            self.source = None

        if self.args.aggregate is not None:
            self.aggregate = self.args.aggregate
        else:
            self.aggregate = "avg"

        if self.args.format is not None:
            self.format = self.args.format
        else:
            self.format = "json"

        if self.args.date_format is not None:
            self.date_format = self.args.date_format

        start_time = int(self.parse_time_date(self.args.start).strftime("%s"))

        # If the end time is not specified then
        # default to the current time
        if self.args.end is None:
            stop_time = int(self.now.strftime("%s"))
        else:
            stop_time = int(self.parse_time_date(self.args.end).strftime("%s"))

        # Convert to epoch time in milli-seconds
        start_time *= 1000
        stop_time *= 1000

        self.path = "v1/measurements/{0}".format(self._metric_name)
        url_parameters = {"start": str(start_time),
                          "end": str(stop_time),
                          "sample": str(self.sample),
                          "agg": self.aggregate}
        if self.source is not None:
            url_parameters['source'] = self.source
        self.url_parameters = url_parameters

    def parse_time_date(self, s):
        """
        Attempt to parse the passed in string into a valid datetime.
        If we get a parse error then assume the string is an epoch time
        and convert to a datetime.
        """
        try:
            ret = parser.parse(str(s))
        except ValueError:
            try:
                ret = datetime.fromtimestamp(int(s))
            except TypeError:
                ret = None
        return ret

    def _format_timestamp(self, ts):
        if self.date_format is not None:
            fts = datetime.fromtimestamp(int(float(ts)/1000.0)).strftime(self.date_format)
        else:
            fts = datetime.fromtimestamp(int(float(ts)/1000.0)).strftime('%s')

        return str(fts)

    def get_description(self):
        """
        Returns the description of this command
        """
        return 'Retrieves measurement values from a metric in a {0} account'.format(self.product_name)

    def output_csv(self, text):
        """
        Output results in CSV format
        """
        payload = json.loads(text)
        # Print CSV header
        print("{0},{1},{2},{3},{4}".format('timestamp', 'metric', 'aggregate', 'source', 'value'))
        metric_name = self._metric_name
        # Loop through the aggregates one row per timestamp, and 1 or more source/value pairs
        for r in payload['result']['aggregates']['key']:
            timestamp = self._format_timestamp(r[0][0])
            # timestamp = string.strip(timestamp, ' ')
            # timestamp = string.strip(timestamp, "'")
            for s in r[1]:
                print('{0},"{1}","{2}","{3}",{4}'.format(timestamp, metric_name, self.aggregate, s[0], s[1]))

    def output_json(self, text):
        """
        Output results in structured JSON format
        """
        payload = json.loads(text)
        data = []
        metric_name = self._metric_name
        for r in payload['result']['aggregates']['key']:
            timestamp = self._format_timestamp(r[0][0])
            for s in r[1]:
                data.append({
                    "timestamp": timestamp,
                    "metric": metric_name,
                    "aggregate": self.aggregate,
                    "source": s[0],
                    "value": s[1],
                })
        payload = {"data": data}
        out = json.dumps(payload, indent=self._indent, separators=(',', ': '))
        print(self.colorize_json(out))

    def output_raw(self, text):
        """
        Output results in raw JSON format
        """
        payload = json.loads(text)
        out = json.dumps(payload, sort_keys=True, indent=self._indent, separators=(',', ': '))
        print(self.colorize_json(out))

    def output_xml(self, text):
        """
        Output results in JSON format
        """

        # Create the main document nodes
        document = Element('results')
        comment = Comment('Generated by TrueSight Pulse measurement-get CLI')
        document.append(comment)
        aggregates = SubElement(document, 'aggregates')
        aggregate = SubElement(aggregates, 'aggregate')
        measurements = SubElement(aggregate, 'measurements')

        # Parse the JSON result so we can translate to XML
        payload = json.loads(text)

        # Current only support a single metric, if we move to the batch API then
        # we can handle multiple
        metric_name = self._metric_name

        # Loop through the aggregates one row per timestamp, and 1 or more source/value pairs
        for r in payload['result']['aggregates']['key']:
            timestamp = self._format_timestamp(r[0][0])
            for s in r[1]:
                # Each timestamp, metric, source, values is placed in a measure tag
                measure_node = SubElement(measurements, 'measure')
                source = s[0]
                value = str(s[1])
                ts_node = SubElement(measure_node, 'timestamp')
                ts_node.text = str(timestamp)
                metric_node = SubElement(measure_node, 'metric')
                metric_node.text = metric_name
                metric_node = SubElement(measure_node, 'aggregate')
                metric_node.text = self.aggregate
                source_node = SubElement(measure_node, 'source')
                source_node.text = source
                value_node = SubElement(measure_node, 'value')
                value_node.text = value

        rough_string = ElementTree.tostring(document, 'utf-8')
        reparse = minidom.parseString(rough_string)
        output = reparse.toprettyxml(indent=" ")
        print(self.colorize_xml(output))

    def _handle_results(self):
        """
        Call back function to be implemented by the CLI.
        """

        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            if self.format == "json":
                self.output_json(self._api_result.text)
            elif self.format == "csv":
                self.output_csv(self._api_result.text)
            elif self.format == "raw":
                self.output_raw(self._api_result.text)
            elif self.format == "xml":
                self.output_xml(self._api_result.text)
        else:
            pass
