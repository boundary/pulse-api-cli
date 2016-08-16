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
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import json
import urllib2


class WebHookBase(object):
    def __init__(self):
        pass


"""
Wrapper for metric from Web Hook JSON payload
"""


class WebHookMetric(WebHookBase):
    def __init__(self, id, name, type):
        WebHookBase.__init__(self)
        self._id = id
        self._name = name

        # Acceptable types
        types = ['number', 'percent', 'max', 'min']

        # If the type is not one of our expected values
        # then raise an error
        if type in types:
            self._type = type
        else:
            raise AttributeError("Type not one of: " + str(types))

    #
    # id
    #
    @property
    def id(self):
        return self._id

    #
    # name
    #
    @property
    def name(self):
        return self._name

    #
    # type
    #
    @property
    def type(self):
        return self._type


"""
Class wrapper for text attribute of Web Hook action JSON payload
"""


class WebHookText(WebHookBase):
    def __init__(self, isSet, serverName, link, labelHTML, labelText):
        WebHookBase.__init__(self)
        self._isSet = isSet
        self._serverName = serverName
        self._link = link
        self._labelHTML = labelHTML
        self._labelText = labelText

    #
    # isSet
    #
    @property
    def isSet(self):
        return self._isSet

    #
    # serverName
    #
    @property
    def server_name(self):
        return self._server_name


class WebHookServer(WebHookBase):
    def __init__(self, is_set, hostname, aggregate, metric, value, threshold, time, link):
        """
        Constructor for a WebHookServer
        """
        WebHookBase.__init__(self)
        self.is_set = is_set
        self.hostname = hostname
        self.aggregate = aggregate
        self.metric = metric
        self.value = value
        self.threshold = threshold
        self.time = time
        self.link = link

    @property
    def is_set(self):
        return self.is_set


"""
Class to store POST'ed data from Web Hook
"""


class WebHookAction(WebHookBase):
    def __init__(self, affected_servers={}):
        self.json = None
        self._data = {}
        self._alarm_name = self._data['alarmName']
        self._metric = self._data['metric']
        self._status = self._data['status']
        self._resolved_servers = None

        if 'affectedServers' in self._data:
            self._affectedServers = self._data['affectedServers']

    def parse_json(self, text):
        self.json = json.loads(text)

    #
    # affectedServers
    #

    @property
    def affected_servers(self):
        return self._affected_servers

    #
    # alarmName
    #
    @property
    def alarm_name(self):
        return self._alarm_name

    #
    # resolvedServers
    #
    @property
    def resolvedServers(self):
        return self._resolvedServers

    #
    # status
    #
    @property
    def status(self):
        return self._status

    #
    # metric
    @property
    def metric(self):
        return self._metric

    def __str__(self):
        print(self)


class WebHookHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        """
        Handles the POST request sent by Boundary Url Action
        """
        self.send_response(urllib2.httplib.OK)
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print("Client: {0}".format(str(self.client_address)))
        print("headers: {0}".format(self.headers))
        print("path: {0}".format(self.path))
        print("body: {0}".format(body))
        # self.wfile.write("data: {0}\n".format(str(body)))

        # self.wfile.write("Client: {0}\n".format(str(self.client_address)))
        # self.wfile.write("Path: {0}\n".format(self.path))

    # print("Body: {0}".format(self.process_payload(body)))

    def validate_data(self, data):
        return True

    def process_payload(self, json_data):
        data = json.loads(json_data)
        return data

    def handle_action(self, action):
        print(action)


class WebHookApp:
    def __init__(self, address='127.0.0.1', port=9080, cls=WebHookHandler):
        self.address = address
        self.port = port
        self.cls = cls

    def start(self):
        server = HTTPServer((self.address, self.port), self.cls)
        # TODO: Enable SSL
        # openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
        # server.socket = ssl.wrap_socket (server.socket, certfile='/Users/davidg/server.pem', server_side=True)
        print("Starting Webhook on {0}:{1}, use <Ctrl-C> to stop".format(self.address, self.port))
        server.serve_forever()


def main():
    c = WebHookApp()
    c.start()


if __name__ == "__main__":
    main()
