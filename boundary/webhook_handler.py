#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
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
import ssl

class WebHookBase(object):

    def __init__(self):
        pass

    def _raiseAttributeChangeError(self, propertyName):
        raise AttributeError("Cannot change property " + propertyName)


    def _raiseAttributeDeleteError(self, propertyName):
        raise AttributeError("Cannot delete property " + propertyName)


"""
Wrapper for metric from Web Hook JSON payload
"""
class WebHookMetric(WebHookBase):

    def __init__(self,id,name,type):
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
    def id(self,value):
        self._raiseAttributeChangeError('id')

    @id.deleter
    def id(self):
        self._raiseAttributeDeleteError('id')

    #
    # name
    #
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._raiseAttributeChangeError('name')

    @name.deleter
    def name(self):
        self._raiseAttributeDeleteError('name')

    #
    # type
    #
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,value):
        self._raiseAttributeChangeError('type')

    @type.deleter
    def type(self):
        self._raiseAttributeDeleteError('type')


"""
Class wrapper for text attribute of Web Hook action JSON payload
"""
class WebHookText(WebHookBase):

    def __init__(self,isSet,serverName,link,labelHTML,labelText):
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
        self._raiseAttributeChangeError('isSet')

    @isSet.deleter
    def isSet(self):
        self._raiseAttributeDeleteError('isSet')

    #
    # serverName
    #
    @property
    def serverName(self):
        self._serverName

    @serverName.setter
    def serverName(self,value):
        self._raiseAttributeChangeError('serverName')

    @serverName.deleter
    def serverName(self):
        self._raiseAttributeDeleteError('serverName')


    # "isSet": true,
    # "serverName": "boundary-snmp-001",
    # "link": "https://premium.boundary.com/7053/default?ival=60&marker=1431464024000!cpu",
    # "labelHTML": "Server <strong>boundary-snmp-001</strong>'s avg CPU utilization is <strong style=\"color:#900\">81.7%</strong> which is greater than the threshold of 80.0% for 1.6s now",
    # "labelText": "Server boundary-snmp-001's avg CPU utilization is 81.7% which is greater than the threshold of 80.0% for 1.6s now"


class WebHookServer(WebHookBase):

    def __init__(self, isSet, hostname, aggregate, metric, value, threshold, time, link):
        """
        Constructor for a WebHookServer
        """
        self.isSet = isSet
        self.hostname = hostname
        self.aggregate = aggregate
        self.metric = metric
        self.value = value
        self.threshold = threshold
        self.time = time
        self.link = link

    @property
    def isSet(self):
        return self.isSet

    @isSet.setter
    def isSet(self):
        self._raiseAttributeChangeError('isSet')

    @isSet.deleter
    def self(self):
        self._raiseAttributeDeleteError('isSet')




"""
Class to store POST'ed data from Web Hook
"""


class WebHookAction(WebHookBase):
    def __init__(self, affectedServers={}):
        self._alarmName = self.data['alarmName']
        self._metric = self.data['metric']
        self._status = self.data['status']

        if 'affectedServers' in self.data:
            self._affectedServers = self.data['affectedServers']

    def parseJSON(self, json_data):
        self.json = json.loads(json_data)

    #
    # affectedServers
    #

    @property
    def affectedServers(self):
        return self._affectedServers

    @affectedServers.setter
    def affectedServers(self, value):
        WebHookAction._raiseAttributeChangeError('affectedServers')

    @affectedServers.deleter
    def affectedServers(self):
        WebHookAction._raiseAttributeChangeError('affectedServers')

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



class WebhookHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        '''
        Handles the POST request sent by Boundary Url Action
        '''
        self.send_response(urllib2.httplib.OK)
        self.end_headers()
        contentLength = int(self.headers['Content-Length'])
        data = self.rfile.read(contentLength)
        print(data)
        self.wfile.write('data: %s\n' % str(data))

        self.wfile.write('Client: %s\n' % str(self.client_address))
        # self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)

        self.processPayload(data)

        return

    def validateData(self,data):
        return True

    def processPayload(self,json_data):

        data = json.loads(json_data)




    def handleAction(self,action):
        print(action)


class WebhookApp:
    def __init__(self, address='127.0.0.1', port=8090, cls=WebhookHandler):
        self.address = address
        self.port = port
        self.cls = cls

    def start(self):
        server = HTTPServer((self.address, self.port), self.cls)
        # TODO: Enable SSL
        # openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
        # server.socket = ssl.wrap_socket (server.socket, certfile='/Users/davidg/server.pem', server_side=True)
        print('Starting Webhook, use <Ctrl-C> to stop')
        server.serve_forever()


if __name__ == "__main__":
    c = WebhookApp()
    c.start()
