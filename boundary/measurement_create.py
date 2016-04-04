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
import socket
import time
import json

from boundary import ApiCli
import requests

"""
Implements command line utility to add a measurement value to a Boundary account
Uses the following Boundary API:

http://premium-documentation.boundary.com/v1/post/measurements

"""


class MeasurementCreate(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "POST"
        self.path = "v1/measurements"
        self.metricName = None
        self.measurement = None
        self.source = None
        self.timestamp = None
        self._properties = None

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-n', '--metric-name', dest='metricName', action='store', required=True,
                                 metavar='metric_name', help='Metric identifier')
        self.parser.add_argument('-m', '--measurement', dest='measurement', action='store', required=True,
                                 metavar="measurement", help='Measurement value')
        self.parser.add_argument('-s', '--source', dest='source', action='store', required=False, metavar="source",
                                 help='Source of measurement. Defaults to the host where the command is run')
        self.parser.add_argument('-d', '--timestamp', dest='timestamp', action='store', metavar="timestamp",
                                 help='Time of occurrence of the measurement in either epoch seconds or \
                                 epoch milliseconds. Defaults to the receipt time at api endpoint')
        self.parser.add_argument('-p', '--property', dest='properties', action='append', required=False,
                                 metavar='property=value',
                                 help='Property to add to the measurement')

    def _process_properties(self):
        """
        Transforms the command line properties into python dictionary
        :return:
        """
        if self.args.properties is not None:
            self._properties = {}
            for p in self.args.properties:
                d = p.split('=')
                self._properties[d[0]] = d[1]

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)
        if self.args.metricName is not None:
            self.metricName = self.args.metricName

        if self.args.measurement is not None:
            self.measurement = self.args.measurement

        if self.args.source is not None:
            self.source = self.args.source
        else:
            self.source = socket.gethostname()

        if self.args.timestamp is not None:
            self.timestamp = int(self.args.timestamp)

        m = {'metric': self.metricName,
             'measure': self.measurement}

        if self.source is not None:
            m['source'] = self.source
        if self.timestamp is not None:
            m['timestamp'] = int(self.timestamp)

        self._process_properties()

        if self._properties is not None:
            m['metadata'] = self._properties

        self.data = json.dumps(m, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}

    def _call_api(self):
        """
        Override so we can handle the incomplete read error generated
        by Boundary API that creates a measurement.
        Handle here instead of ApiCli since we do not want to mask errors
        to other API calls.
        """
        try:
            ApiCli._call_api(self)
        except requests.exceptions.ChunkedEncodingError:
            pass

    def get_description(self):
        return 'Adds a measurement value to a {0} account'.format(self.product_name)

    def _handle_results(self):
        """
        Call back function to be implemented by the CLI.
        """

        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            payload = json.loads(self._api_result.text)
            out = json.dumps(payload, sort_keys=True, indent=4, separators=(',', ': '))
            print(self.colorize_json(out))
