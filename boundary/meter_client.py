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
        self.rpc_method = None
        self.rpc_parameters = {}
        self.MAX_LINE=1024

    def getDescription(self):
        """
        Text describing this command
        """
        return "Communicates with an meter using JSON RPC"

    def addArguments(self):
        self.addLoggingArgument()
        self.parser.add_argument('-m', '--method', dest='rpc_method', action='store', default='query_metric',
                                 choices=['discovery', 'debug', 'status', 'query_metric', 'metric', 'event',
                                          'get_system_info', 'get_service_listeners'],
                                 help='Sets the RPC method to call on the meter')
        self.parser.add_argument('-r', '--rpc-host', dest='rpc_host', action='store', metavar='host',
                                 help='Sets the host or ip address to contact the meter on')
        self.parser.add_argument('-p', '--parameters', dest='rpc_parameters', action='store', metavar='parameters',
                                 help='Sets the host or ip address to contact the meter on')

    def getArguments(self):
        self.configureLogging()

        if self.args.rpc_method is not None:
            self.rpc_method = self.args.rpc_method

        if self.args.rpc_host is not None:
            self.rpc_host = self.args.rpc_host

        if self.args.rpc_parameters is not None:
            self.rpc_parameters = self.args.rpc_parameters

    def handleResults(self, result):
        print(self.rpc_data[0])

    def get_json(self):
        message = {}

        message['jsonrpc'] = '2.0'
        message['method'] = self.rpc_method
        message['id'] = 1
        message['params'] = {'match': 'system.cpu.usage'}
        self.rpc_message = json.dumps(message)
        logging.debug('rpc_message: ' + self.rpc_message)

    def callAPI(self):
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
