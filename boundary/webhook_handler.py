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

    def _raise_attribute_change_error(self, property_name):
        raise AttributeError("Cannot change property " + property_name)

    def _raise_attribute_delete_error(self, property_name):
        raise AttributeError("Cannot delete property " + property_name)


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

    @id.setter
    def id(self, value):
        self._raise_attribute_change_error('id')

    @id.deleter
    def id(self):
        self._raise_attribute_delete_error('id')

    #
    # name
    #
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._raise_attribute_change_error('name')

    @name.deleter
    def name(self):
        self._raise_attribute_delete_error('name')

    #
    # type
    #
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._raise_attribute_change_error('type')

    @type.deleter
    def type(self):
        self._raise_attribute_delete_error('type')


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

    @isSet.setter
    def isSet(self):
        self._raise_attribute_change_error('isSet')

    @isSet.deleter
    def isSet(self):
        self._raise_attribute_delete_error('isSet')

    #
    # serverName
    #
    @property
    def server_name(self):
        return self._server_name

    @server_name.setter
    def server_name(self, value):
        self._raise_attribute_change_error('serverName')

    @server_name.deleter
    def server_name(self):
        self._raise_attribute_delete_error('serverName')


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

    @is_set.setter
    def is_set(self, value):
        self._raise_attribute_change_error('is_set')

    @is_set.deleter
    def is_set(self):
        self._raise_attribute_delete_error('is_set')


"""
Class to store POST'ed data from Web Hook
"""


class WebHookAction(WebHookBase):
    def __init__(self, affected_servers={}):
        self.json = None
        self._alarmName = self.data['alarmName']
        self._metric = self.data['metric']
        self._status = self.data['status']
        self._resolvedServers

        if 'affectedServers' in self.data:
            self._affectedServers = self.data['affectedServers']

    def parse_json(self, json_data):
        self.json = json.loads(json_data)

    #
    # affectedServers
    #

    @property
    def affectedServers(self):
        return self._affectedServers

    @affectedServers.setter
    def affectedServers(self, value):
        WebHookAction._raise_attribute_change_error('affectedServers')

    @affectedServers.deleter
    def affectedServers(self):
        WebHookAction._raise_attribute_change_error('affectedServers')

    #
    # alarmName
    #
    @property
    def alarmName(self):
        return self._alarmName

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
        data = self.rfile.read(content_length)
        print(data)
        print(self.headers)
        self.wfile.write('data: %s\n' % str(data))

        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('Path: %s\n' % self.path)
        self.process_payload(data)

        return

    def validate_data(self, data):
        return True

    def process_payload(self, json_data):
        data = json.loads(json_data)

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


if __name__ == "__main__":
    c = WebHookApp()
    c.start()
