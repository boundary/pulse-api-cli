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

from boundary import ApiCli
from dateutil import parser

"""
Gets measurements from a Boundary account
"""


class MeasurementGet(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        self.metricName = None
        self.source = None
        self.aggregate = None
        self.startTime = None
        self.stopTime = None

    def addArguments(self):
        """
        Add specific command line arguments for this command   
        """

        # Call our parent to add the default arguments
        ApiCli.addArguments(self)

        # Command specific arguments
        self.parser.add_argument('-n', '--name', dest='metricName', action='store', required=True,
                                 metavar="metric_name", help='Metric identifier')
        self.parser.add_argument('-g', '--aggregate', dest='aggregate', action='store',
                                 choices=['sum', 'avg', 'max', 'min'], metavar='aggregate',
                                 help='Metric default aggregate')
        self.parser.add_argument('-s', '--source', dest='source', action='store', metavar="source",
                                 help='Source of measurement')
        self.parser.add_argument('-b', '--start', dest='start', action='store', required=True, metavar="start",
                                 help='Start of time range as ISO 8601 string or epoch seconds')
        self.parser.add_argument('-d', '--end', dest='end', action='store', metavar="end",
                                 help='End of time range as ISO 8601 string or epoch seconds')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)
        if self.args.metricName is not None:
            self.metricName = self.args.metricName

        if self.args.source is not None:
            self.source = self.args.source
        else:
            self.source = ""

        if self.args.aggregate is not None:
            self.aggregate = self.args.aggregate
        else:
            self.aggregate = "avg"

        # The start time is a required argument on
        # the command line so self.start.args should never
        # have a value of None
        if self.args.start is None:
            startTime = int(datetime.now().strftime("%s"))
        else:
            startTime = int(self.parseTimeDate(self.args.start).strftime("%s"))

        # If the end time is not specified then
        # default to the current time
        if self.args.end is None:
            stopTime = int(datetime.now().strftime("%s"))
        else:
            stopTime = int(self.parseTimeDate(self.args.end).strftime("%s"))

        # Convert to epoch time in milli-seconds
        startTime *= 1000
        stopTime *= 1000

        self.path = "v1/measurements/{0}".format(self.metricName)
        self.url_parameters = {"source": self.source, "start": str(startTime), "end": str(stopTime),
                               "agg": self.aggregate}

    def parseTimeDate(self, s):
        """
        Attempt to parse the passed in string into a valid datetime.
        If we get a parse error then assume the string is an epoch time
        and convert to a datetime.
        """
        try:
            ret = parser.parse(s)
        except ValueError:
            try:
                ret = datetime.utcfromtimestamp(s)
            except TypeError:
                ret = None
        return ret

    def getDescription(self):
        """
        Returns the description of this command
        """
        return "Retrieves measurement values from a metric in a Boundary account"
