#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
from unittest import TestCase

from boundary import MetricExport
from cli_runner import CLIRunner
from cli_test import CLITest


class MetricExportTest(TestCase):
    def setUp(self):
        self.cli = MetricExport()

    def test_get_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def metric_assert(self, metric, display_name, display_name_short, description, unit, aggregate, resolution,
                      disabled):
        self.assertEqual(display_name, metric['displayName'])
        self.assertEqual(display_name_short, metric['displayNameShort'])
        self.assertEqual(description, metric['description'])
        self.assertEqual(unit, metric['unit'])
        self.assertEqual(aggregate, metric['defaultAggregate'])
        self.assertEqual(resolution, metric['defaultResolutionMS'])
        self.assertEqual(disabled, metric['isDisabled'])

    def test_export_metric(self):
        runner_export = CLIRunner(MetricExport())

        export = runner_export.get_output([])
        metrics = json.loads(export)

        self.metric_assert(metrics['SYSTEM.CPU.IOWAIT'],
                           'CPU IO Wait Time',
                           'CPU IO Wait',
                           'The percentage of CPU time spent waiting for IO operations.',
                           'percent',
                           'AVG',
                           1000,
                           False)

        self.metric_assert(metrics['SYSTEM.CPU.STOLEN'],
                           'CPU Stolen Time',
                           'CPU Stolen',
                           'The percentage of time a virtual machine was ' +
                           'ready to run but was not allowed to run by the host OS.',
                           'percent',
                           'AVG',
                           1000,
                           False)
        self.metric_assert(metrics['SYSTEM.CPU.SYS'],
                           'CPU System Time',
                           'CPU System',
                           'The percentage of available CPU time being utilized by the OS.',
                           'percent',
                           'AVG',
                           1000,
                           False)
        self.metric_assert(metrics['SYSTEM.CPU.USER'],
                           'CPU User Time',
                           'CPU User',
                           'The percentage of available CPU time being utilized by programs.',
                           'percent',
                           'AVG',
                           1000,
                           False)
        self.metric_assert(metrics['SYSTEM.FS.USE_PERCENT.TOTAL'],
                           'Filesystem Utilization',
                           'FileSys Used',
                           'Percentage of disk space used (written on). ' +
                           'This is the total among all non-virtual, local filesystems.',
                           'percent',
                           'MAX',
                           1000,
                           False)

        self.metric_assert(metrics['SYSTEM.MEM.FREE'],
                           'Memory Bytes Free',
                           'Mem Free',
                           'The amount of unused memory by programs and the OS.',
                           'bytecount',
                           'AVG',
                           1000,
                           False)

        self.metric_assert(metrics['SYSTEM.METER.KEEPALIVE'],
                                   'SYSTEM.METER.KEEPALIVE',
                                   'SYSTEM.METER.KEEPALIVE',
                                   'SYSTEM.METER.KEEPALIVE',
                                   'number',
                                   'AVG',
                                   1000,
                                   False)

        self.metric_assert(metrics['SYSTEM.OS.CONTEXT_SWITCHES'],
                           'Context Switches',
                           'Context Switches',
                           'The number of switches between programs and the OS in the last second.',
                           'number',
                           'MAX',
                           1000,
                           False)

        self.metric_assert(metrics['SYSTEM.OS.LOADAVG.ONE'],
                           'One Minute Load Average',
                           'Load Avg 1 Min',
                           'An averaging of the number of processes utilizing or waiting for CPU ' +
                           'time over that last minute. This number is divided by number of CPUs to provide an ' +
                           'accurate comparative number between systems with different numbers of CPUs.',
                           'number',
                           'AVG',
                           1000,
                           False)

        self.metric_assert(metrics['SYSTEM.OS.LOADAVG.QUEUE'],
                           'Processor Queue',
                           'Proc Queue',
                           'The number of processes that are waiting to run on a CPU.',
                           'number',
                           'MAX',
                           1000,
                           False)

        self.metric_assert(metrics['SYSTEM.PROC.IDLE'],
                           'Number of Idle Processes',
                           'Proc Idle',
                           'The number of processes that have not executed for more than 20 seconds.',
                           'number',
                           'MAX',
                           1000,
                           False)
        self.metric_assert(metrics['SYSTEM.PROC.THREADS'],
                           'Number of Threads',
                           'Proc Threads',
                           'Number of process threads running. ' +
                           'A single process can have many threads, but a thread can only have one process.',
                           'number',
                           'MAX',
                           1000,
                           False)
        self.metric_assert(metrics['SYSTEM.PROC.TOTAL'],
                           'Total Number of Processes',
                           'Proc Count',
                           'The number of processes running, ' +
                           'including duplicates. Processes are programs that support applications.',
                           'number',
                           'MAX',
                           1000,
                           False)
