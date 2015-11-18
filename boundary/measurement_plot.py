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

from boundary import ApiCli
import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt


class MeasurementPlot(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.file_name = None

        linestyles = [

            # solid line style
            '-',
            # dashed line style
            '--',
            # dash-dot line style
            '-.',
            # dotted line style
            ':'
        ]

        markers = [
            # point marker
            '.',
            # pixel marker
            ',',
            # circle marker
            'o',
            # triangle_down marker
            'v',
            # triangle_up marker
            '^',
            # triangle_left marker
            '<',
            # triangle_right marker
            '>',
            # tri_down marker
            '1',
            # tri_up marker
            '2',
            # tri_left marker
            '3',
            # tri_right marker
            '4',
            # square marker
            's',
            # pentagon marker
            'p',
            # star marker
            '*',
            # hexagon1 marker
            'h',
            # hexagon2 marker
            'H',
            # plus marker
            '+',
            # x marker
            'x',
            # diamond marker
            'D',
            # thin_diamond marker
            'd',
            # vline marker
            '|',
            # hline marker
            '_',
        ]

        colors = [
            # blue
            'b',
            # green
            'g',
            # red
            'r',
            # cyan
            'c',
            # magenta
            'm',
            # yellow
            'y',
            # black
            'k',
            # white
            'w',
        ]

        self._symbols = [(linestyle, marker, color) for linestyle in linestyles for marker in markers for color in
                         colors]

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-f', '--file-name', dest='file_name', action='store', required=False, metavar='path',
                                 help='File name including path of data to plot')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        # ApiCli.get_arguments(self)
        if self.args.file_name is not None:
            self.file_name = self.args.file_name

    def _plot_data(self):
        timestamps = {}
        values = {}
        metric_name = None

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
                epoch_ts = int(row[0]) / 1000
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

        symbol_index = 0
        for source in values:
            linestyle, marker, color = self._symbols[symbol_index]
            plt.plot(timestamps[source], values[source], color=color, marker=marker, linestyle=linestyle, label=source)
            symbol_index += 1

        # add legend
        plt.legend(loc=9)

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
        self.add_arguments()
        self._parse_args()
        self.get_arguments()
        if self._validate_arguments():
            self._plot_data()
        else:
            print(self._message)
