#!/usr/bin/env python
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

from boundary import ApiCli
import csv
import sys


class MeasurementPlot(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.file_name = None

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-f', '--file-name', dest='file_name', action='store', required=False,
                                 metavar='metric_name',
                                 help='File name including path of data to plot')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        # ApiCli.getArguments(self)
        if self.args.file_name is not None:
            self.file_name = self.args.file_name

    def _plot_data(self):
        if self.file_name is not None:
            f = open(self.file_name,'r')
        else:
            f = sys.stdin
        reader = csv.reader(f, delimiter=',')
        first = True
        for row in reader:
            if first:
                first = False
            else:
                print('{0},{1},{2}'.format(row[0], row[1], row[2]))

        # Close the file handle only if we opened it
        if f != sys.stdin:
            f.close()

    def execute(self):
        """
        Run the steps to execute the CLI
        """
        # self._get_environment()
        self.addArguments()
        self._parse_args()
        self.getArguments()
        if self._validate_arguments():
            self._plot_data()
        else:
            print(self._message)
