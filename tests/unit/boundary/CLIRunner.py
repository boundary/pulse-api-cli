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
import re
import subprocess
import sys


class CLIRunner(object):

    def __init__(self, cli):
        self._cli = cli

    def get_cli_name_from_class(self):
        name = self._cli.__class__.__name__
        m = re.findall("([A-Z][a-z]+)", name)
        m = [a.lower() for a in m]
        cli_name = str.join('-', m)
        return cli_name

    def execute(self, args):
        self.get_output(args)

    def get_output(self, args):
        output = None
        try:
            command = self.get_cli_name_from_class()
            args.insert(0, command)
            print(args)
            output = subprocess.check_output(args=args)
        except subprocess.CalledProcessError as e:
            sys.stderr.write("{0}: {1}\n".format(e.output, e.returncode))
        return output

