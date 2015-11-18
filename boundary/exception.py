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


"""
Base exception class for pulse exceptions
"""


class APIError(Exception):
    pass


class APIConnectionError(APIError):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Error connecting to Boundary API: %s" % self.error


class APIResponseError(APIError):
    def __init__(self, status_code, error):
        self.status_code = status_code
        self.error = error

    def __str__(self):
        return "Error response from Boundary API (%d): %s" % (self.status_code, self.error)
