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
import json
from six.moves import http_client


class Source(object):
    def __init__(self, ref=None, _type=None, name=None, properties=None):
        self._ref = ref
        self._type = _type
        self._name = name
        self._properties = properties

    @property
    def ref(self):
        return self._ref

    @ref.setter
    def ref(self, ref):
        self._ref = ref

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, _type):
        self._type = _type

    @property
    def name(self):
        return self._name


def split_string(s):
    return str.split(s, ':')


def string_to_dict(s):
    return json.loads(s)


class EventCreate(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "POST"
        self.path = 'v1/events'

        self.fingerprint_fields = None
        self.title = None
        self.source = None
        self.severity = None
        self.status = None

    def addArguments(self):
        ApiCli.addArguments(self)
        self.parser.add_argument('-b', '--status', dest='status', action='store',
                                 choices=[])
        self.parser.add_argument('-v', '--severity', dest='severity', action='store',
                                 choices=['INFO', 'WARN', 'ERROR', 'CRITICAL'],
                                 help='Severity of the the event')
        self.parser.add_argument('-m', '--message', dest='message', action='store',
                                 metavar='message', help='Text describing the event')
        self.parser.add_argument('-f', '--fingerprint-fields', dest='fingerprint_fields', action='store', required=True,
                                 type=split_string, metavar='aggregate', help='Metric aggregate to alarm upon')
        self.parser.add_argument('-o', '--organization-id', dest='organization_id', action='store',
                                 metavar='organization_id', help='Boundary account Id')
        #
        self.parser.add_argument('-p', '--properties', dest='properties', action='store')
        # self.parser.add_argument('-v', '--trigger-threshold', dest='triggerThreshold', action='store',
        # metavar='value',
        #                          help='Trigger threshold value')
        # self.parser.add_argument('-r', '--sender', dest='triggerInterval', action='store',
        #                          metavar='interval', help='Optional information about the sender of the event. \
        #                          This is used to describe a third party event system forwarding this event into \
        #                          Boundary, or a Boundary service sending the event.')
        # self.parser.add_argument('-i', '--host-group-id', dest='hostGroupId', action='store', metavar='hostgroup_id',
        #                          help='Host group the alarm applies to')
        self.parser.add_argument('-s', '--source', dest='source', action='store', metavar='ref:type:name:properties',
                                 type=string_to_dict, help='A description or resolution of the alarm')

        self.parser.add_argument('-w', '--title', dest='title', metavar='title', action='store', required=True,
                                 help='Title of the event')

        # self.parser.add_argument('-x', '--tags', dest='isDisabled', action='store_true',
        #                          help='Tags to assi')

    def getArguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.getArguments(self)
        if self.args.fingerprint_fields is not None:
            self.fingerprint_fields = self.args.fingerprint_fields

        if self.args.title is not None:
            self.title = self.args.title

        if self.args.source is not None:
            self.source = self.args.source

        if self.args.severity is not None:
            self.severity = self.args.severity

        if self.args.message is not None:
            self.message = self.args.message

        event = {
            "title": "foobar",
            "fingerprintFields": ['@title'],
            "source": {"ref": "foo", "type": "bar", "name": "foobar"}
        }

        if self.title is not None:
            event['title'] = self.title

        if self.severity is not None:
            event['severity'] = self.severity

        if self.message is not None:
            event['message'] = self.message

        if self.source is not None:
            event['source'] = self.source

        if self.fingerprint_fields is not None:
            event['fingerprintFields'] = self.fingerprint_fields

        self.data = json.dumps(event, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}

    def validateArguments(self):
        """
        TODO: Implement validation of event creation arguments
        """
        return ApiCli.validateArguments(self)

    def getDescription(self):
        return "Creates a new metric event in an Boundary account"

    def good_response(self, status_code):
        """
        A successful call to the Event Creation API returns a 201 and not 200
        so check for that response and return True when we receive a 201 response
        """
        return status_code == http_client.CREATED

    def handleResults(self, result):
        # Only process if we get HTTP result of 201
        if result.status_code == http_client.CREATED:
            location = result.headers['location']
            s = str.split(location, '/')
            out = s[-1]
            event_id = {
                "eventId": int(out)
            }
            out = json.dumps(event_id, sort_keys=True, indent=4, separators=(',', ': '))
            print(out)
