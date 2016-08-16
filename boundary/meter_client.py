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
from socket import *
import logging

from boundary import ApiCli

import json


class MeterClient(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.rpc_data = []
        self.rpc_host = 'localhost'
        self.rpc_port = 9192
        self.rpc_message = None
        self.rpc_method = 'status'
        self.rpc_parameters = None
        self.MAX_LINE = 1024

    def get_description(self):
        """
        Text describing this command
        """
        return 'Communicates with an {0} meter using JSON RPC'.format(self.product_name)

    def add_arguments(self):
        self.add_logging_argument()
        self.parser.add_argument('-m', '--method', dest='rpc_method', action='store', default='query_metric',
                                 choices=['debug', 'discovery', 'event', 'get_process_info', 'get_system_info',
                                          'get_service_listeners', 'metric', 'query_metric', 'status'],
                                 help='Sets the RPC method to call on the meter')
        self.parser.add_argument('-r', '--rpc-host', dest='rpc_host', action='store', metavar='host',
                                 help='Sets the host or ip address to contact the meter on')
        self.parser.add_argument('-p', '--parameters', dest='rpc_parameters', action='store', nargs='*',
                                 metavar='key=value',
                                 help='Sets the host or ip address to contact the meter on')

    def get_arguments(self):
        self.configureLogging()

        if self.args.rpc_method is not None:
            self.rpc_method = self.args.rpc_method

        if self.args.rpc_host is not None:
            self.rpc_host = self.args.rpc_host

        if self.args.rpc_parameters is not None:
            self.rpc_parameters = self.args.rpc_parameters

    def handleResults(self, result):
        print(self.colorize_json(self.rpc_data[0]))

    def parse_rpc_parameters(self):
        p = {}

        if self.rpc_parameters is not None:
            for rpc_p in self.rpc_parameters:
                sp = rpc_p.split('=')
                print(sp)
                p[sp[0]] = sp[1]
                print(p)

        return p

    def get_json(self):
        message = {}

        message['jsonrpc'] = '2.0'
        message['method'] = self.rpc_method
        message['id'] = 1

        # discovery - Retrieve the list of supported methods.
        # debug - Enable/disable meter debug
        # event - Push an event or an array of events
        # get_process_info - Retrieve a list of processes matching a regex and return cpu/mem/disk info.
        # get_system_info - Provide all the system metadata. cpu, mem, disk, network, etc.
        # get_service_listeners - Retrieve a list of services listening on ports and protocols.
        # metric - Push a metric sample or array of samples
        # query_metric - Request internal metrics from the meter.
        # status - Enable/disable periodic stats emission

        if self.rpc_method == 'debug':
            message['params'] = {'match': 'system.cpu.usage'}
        elif self.rpc_method == 'discovery':
            message['params'] = {}
            pass
        elif self.rpc_method == 'event':
            pass
        elif self.rpc_method == 'get_process_info':
            message['params'] = self.parse_rpc_parameters()
        elif self.rpc_method == 'get_system_info':
            message['params'] = self.parse_rpc_parameters()
        elif self.rpc_method == 'get_service_listeners':
            message['params'] = self.parse_rpc_parameters()
        elif self.rpc_method == 'metric':
            pass
        elif self.rpc_method == 'query_metric':
            message['params'] = self.parse_rpc_parameters()
        elif self.rpc_method == 'status':
            message['params'] = self.parse_rpc_parameters()
        else:
            pass

        self.rpc_message = json.dumps(message)
        logging.debug('rpc_message: ' + self.rpc_message)

    def _call_api(self):
        """
        Make a call to the meter via JSON RPC
        """

        # Allocate a socket and connect to the meter
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.rpc_host, self.rpc_port))
        self.get_json()
        message = [self.rpc_message.encode('utf-8')]

        for line in message:
            sockobj.send(line)
            data = sockobj.recv(self.MAX_LINE)
            print(data)
            self.rpc_data.append(data)

        sockobj.close()
