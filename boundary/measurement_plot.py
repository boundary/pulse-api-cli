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
from datetime import datetime
import sys
from matplotlib import pyplot as plt


class MeasurementPlot(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.file_name = None
        linestyles = []
        # solid line style
        linestyles.append('-')
        # dashed line style
        linestyles.append('--')
        # dash-dot line style
        linestyles.append('-.')
        # dotted line style
        linestyles.append(':')

        markers = []
        # point marker
        markers.append('.')
        # pixel marker
        markers.append(',')
        # circle marker
        markers.append('o')
        # triangle_down marker
        markers.append('v')
        # triangle_up marker
        markers.append('^')
        # triangle_left marker
        markers.append('<')
        # triangle_right marker
        markers.append('>')
        # tri_down marker
        markers.append('1')
        # tri_up marker
        markers.append('2')
        # tri_left marker
        markers.append('3')
        # tri_right marker
        markers.append('4')
        # square marker
        markers.append('s')
        # pentagon marker
        markers.append('p')
        # star marker
        markers.append('*')
        # hexagon1 marker
        markers.append('h')
        # hexagon2 marker
        markers.append('H')
        # plus marker
        markers.append('+')
        # x marker
        markers.append('x')
        # diamond marker
        markers.append('D')
        # thin_diamond marker
        markers.append('d')
        # vline marker
        markers.append('|')
        # hline marker
        markers.append('_')

        colors = []
        colors.append('b')
        # blue
        colors.append('g')
        # green
        colors.append('r')
        # red
        colors.append('c')
        # cyan
        colors.append('m')
        # magenta
        colors.append('y')
        # yellow
        colors.append('k')
        # black
        colors.append('w')
        # white

        self._symbols = [(linestyle, marker, color) for linestyle in linestyles for marker in markers for color in colors]

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-f', '--file-name', dest='file_name', action='store', required=False, metavar='path',
                                 help='File name including path of data to plot')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        # ApiCli.getArguments(self)
        if self.args.file_name is not None:
            self.file_name = self.args.file_name

    def _plot_data(self):
        timestamps = {}
        values = {}
        epoch_ts = None
        metric_name = None
        source = None
        value = None

        if self.file_name is not None:
            f = open(self.file_name, 'r')
        else:
            f = sys.stdin
        reader = csv.reader(f, delimiter=',')
        first = True
        for row in reader:
            if first:
                first = False
            else:
                print('{0},{1},{2},{3}'.format(row[0], row[1], row[2], row[3]))
                epoch_ts = int(row[0])/1000
                metric_name = row[1]
                source = row[2]
                value = float(row[3])
                ts = datetime.fromtimestamp(epoch_ts)
                if source not in timestamps:
                    timestamps[source] = []
                timestamps[source].append(ts)
                if source not in values:
                    values[source] = []
                values[source].append(value)

        # Close the file handle only if we opened it
        if f != sys.stdin:
            f.close()

#        print(values, len(values))
#        print(timestamps, len(values))
        symbol_index = 0
        for source in values:
            linestyle, marker, color = self._symbols[symbol_index]
            plt.plot(timestamps[source], values[source], color=color, marker=marker, linestyle=linestyle, label=source)
            symbol_index += 1

        # add a title
        plt.title(metric_name)
        #  add a label to the y-axis
        plt.ylabel("Bytes")
        plt.show()

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
