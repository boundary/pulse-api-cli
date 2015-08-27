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
from datetime import datetime
import json

from boundary import ApiCli
from dateutil import parser
from six.moves import http_client

"""
Gets measurements from a Boundary account
"""


class MeasurementGet(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        self.metricName = None
        self.format = "json"
        self.sample = 1
        self.source = None
        self.aggregate = None
        self.startTime = None
        self.stopTime = None
        self.now = datetime.now()

    def addArguments(self):
        """
        Add specific command line arguments for this command   
        """

        # Call our parent to add the default arguments
        ApiCli.addArguments(self)

        # Command specific arguments
        self.parser.add_argument('-f', '--format', dest='metricName', action='store', required=False,
                                 metavar="metric_name", help='Metric identifier')
        self.parser.add_argument('-n', '--name', dest='metricName', action='store', required=True,
                                 metavar="metric_name", help='Metric identifier')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate', action='store', required=False,
                                 choices=['sum', 'avg', 'max', 'min'], metavar='aggregate',
                                 help='Metric default aggregate')
        self.parser.add_argument('-r', '--sample', dest='sample', action='store', metavar="sample",required=False,
                                 help='Down sample rate sample in seconds')
        self.parser.add_argument('-s', '--source', dest='source', action='store', metavar="source",required=False,
                                 help='Source of measurement')
        self.parser.add_argument('-b', '--start', dest='start', action='store', required=True, metavar="start",
                                 help='Start of time range as ISO 8601 string or epoch seconds')
        self.parser.add_argument('-d', '--end', dest='end', action='store', metavar="end", required=False,
                                 help='End of time range as ISO 8601 string or epoch seconds')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)
        if self.args.metricName is not None:
            self.metricName = self.args.metricName

        if self.args.sample is not None:
            self.sample = self.args.sample

        if self.args.source is not None:
            self.source = self.args.source
        else:
            self.source = ""

        if self.args.aggregate is not None:
            self.aggregate = self.args.aggregate
        else:
            self.aggregate = "avg"

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

        self.path = "v1/measurements/{0}".format(self.metricName)
        self.url_parameters = {"source": self.source,
                               "start": str(start_time),
                               "end": str(stop_time),
                               "sample": str(self.sample),
                               "agg": self.aggregate}

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

    def getDescription(self):
        """
        Returns the description of this command
        """
        return "Retrieves measurement values from a metric in a Boundary account"

    def output_csv(self):
        pass

    def output_json(self, text):
        payload = json.loads(text)
        out = json.dumps(payload, sort_keys=True, indent=4, separators=(',', ': '))
        print(out)

    def output_csv(self):
        pass

    def handleResults(self, result):
        """
        Call back function to be implemented by the CLI.
        """

        # Only process if we get HTTP result of 200
        if result.status_code == http_client.OK:
            if self.format == "json":
                self.output_json(result.text)
            elif self.format == "csv":
                pass
            elif self.format == "xml":
                pass
            else
                pass
