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

import random
import string
import subprocess
import sys

import re
from cli_test_parameters import CLITestParameters


class CLITest:
    def __init__(self):
        pass

    @staticmethod
    def check_description(test_case, cli):
        parameters = CLITestParameters()
        test_case.assertEqual(parameters.get_value(cli.__class__.__name__, 'description'), cli.get_description())

    @staticmethod
    def check_curl(test_case, cli, output):
        parameters = CLITestParameters()
        p = re.compile(r'-u ".*?"\s')
        a = p.findall(output)
        output = output.replace(a[0], '')
        test_case.assertEqual(parameters.get_value(cli.__class__.__name__, 'curl'), output.encode('utf-8'))

    @staticmethod
    def get_cli_name_from_class(i):
        name = i.__class__.__name__
        m = re.findall("([A-Z][a-z]+)", name)
        m = [a.lower() for a in m]
        cli_name = str.join('-', m)
        return cli_name

    @staticmethod
    def check_cli_help(test_case, cli):
        parameters = CLITestParameters()
        name = cli.__class__.__name__
        expected_output = parameters.get_cli_help(name)
        m = re.findall("([A-Z][a-z]+)", name)
        m = [a.lower() for a in m]
        command = str.join('-', m)
        try:
            output = subprocess.check_output([command, '-h'])
            test_case.assertEqual(expected_output, output)
        except subprocess.CalledProcessError as e:
            sys.stderr.write("{0}: {1}\n".format(e.output, e.returncode))

    @staticmethod
    def get_cli_output(cli, args):
        output = None
        try:
            command = CLITest.get_cli_name_from_class(cli)
            args.insert(0, command)
            output = subprocess.check_output(args=args)
        except subprocess.CalledProcessError as e:
            sys.stderr.write("{0}: {1}\n".format(e.output, e.returncode))
        return output

    @staticmethod
    def random_string(n):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
