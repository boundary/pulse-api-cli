#
# Copyright 2016 BMC Software, Inc.
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
from boundary import PropertyHandler
import json
import requests


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


class EventCreate(ApiCli, PropertyHandler):
    def __init__(self):
        ApiCli.__init__(self)
        PropertyHandler.__init__(self)
        self.method = "POST"
        self.path = 'v1/events'

        self._fingerprint_fields = None
        self._title = None
        self._source = None
        self._severity = None
        self._status = None
        self._tenant_id = None

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-b', '--status', dest='status', action='store',
                                 choices=['acknowledged', 'closed', 'ok', 'open'])
        self.parser.add_argument('-r', '--severity', dest='severity', action='store',
                                 choices=['info', 'warn', 'error', 'critical'],
                                 help='Severity of the the event')
        self.parser.add_argument('-m', '--message', dest='message', action='store',
                                 metavar='message', help='Text describing the event')
        self.parser.add_argument('-f', '--fingerprint-fields', dest='fingerprint_fields', action='store',
                                 required=True, type=split_string, metavar='field_list',
                                 help='List of fields that make up the fingerprint')
        self.parser.add_argument('-o', '--tenant-id', dest='tenant_id', action='store',
                                 metavar='tenant_id', help='Tenant Id')
        # Use the mixin to add argument to handle properties
        self._add_property_argument(self.parser, 'Add properties to an event')
        self.parser.add_argument('-s', '--source', dest='source', action='store', metavar='ref:type:name:properties',
                                 type=split_string, help='A description or resolution of the alarm')

        self.parser.add_argument('-w', '--title', dest='title', metavar='title', action='store', required=True,
                                 help='Title of the event')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)

        if self.args.tenant_id is not None:
            self._tenant_id = self.args.tenant_id

        if self.args.fingerprint_fields is not None:
            self._fingerprint_fields = self.args.fingerprint_fields

        if self.args.title is not None:
            self._title = self.args.title

        if self.args.source is not None:
            self._source = self.args.source

        if self.args.severity is not None:
            self._severity = self.args.severity

        if self.args.message is not None:
            self._message = self.args.message

        event = {}

        if self._title is not None:
            event['title'] = self._title

        if self._severity is not None:
            event['severity'] = self._severity

        if self._message is not None:
            event['message'] = self._message

        if self._source is not None:
            if 'source' not in event:
                event['source'] = {}
            if len(self._source) >= 1:
                event['source']['ref'] = self._source[0]
            if len(self._source) >= 2:
                event['source']['type'] = self._source[1]

        self._process_properties(self.args.properties)
        if self._properties is not None:
            event['properties'] = self._properties

        if self._fingerprint_fields is not None:
            event['fingerprintFields'] = self._fingerprint_fields

        self.data = json.dumps(event, sort_keys=True)
        self.headers = {'Content-Type': 'application/json'}

    def _validate_arguments(self):
        """
        TODO: Implement validation of event creation arguments
        """
        return ApiCli._validate_arguments(self)

    def get_description(self):
        return "Creates a new event in an {0} account".format(self.product_name)

    def good_response(self, status_code):
        """
        A successful call to the Event Creation API returns a 201 and not 200
        so check for that response and return True when we receive a 201 response
        """
        return status_code == requests.codes.accepted

    def _handle_results(self):
        # Only process if we get HTTP result of 201
        if self._api_result.status_code == requests.codes.ok:
            location = self._api_result.headers['location']
            s = str.split(location, '/')
            out = s[-1]
            event_id = {
                "eventId": int(out)
            }
            out = json.dumps(event_id, sort_keys=True, indent=4, separators=(',', ': '))
            print(self.colorize_json(out))
