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

from boundary import ApiCall
import argparse
import logging
import sys
from pygments import highlight, lexers, formatters
import pygments.lexers.html as html

"""
Base class for all the Boundary CLI commands
"""


class ApiCli(ApiCall):
    def __init__(self):
        ApiCall.__init__(self)
        self.product_name = 'TrueSight Pulse'
        # Construct a dictionary with each of the HTTP methods that we support

        self.levels = {"debug": logging.DEBUG,
                       "info": logging.INFO,
                       "warn": logging.WARN,
                       "error": logging.ERROR,
                       "critical": logging.CRITICAL}

        # Properties
        self._message = None

        self.args = None

        self.parser = argparse.ArgumentParser(description=self.get_description())
        self._aggregate_times = ['1 second',
                                 '15 seconds',
                                 '1 minute',
                                 '5 minutes',
                                 '1 hour',
                                 '1.5 hours',
                                 '3 hours',
                                 '6 hours',
                                 '12 hours']

    def get_aggregate_grains(self):
        """
        Returns the standard cube aggregates in the alarm/measurement APIs
        """
        return self._aggregate_times

    def get_description(self):
        """
        Returns a description of the CLI
        """
        return "General API CLI"

    def add_logging_argument(self):
        self.parser.add_argument('-l', '--log-level', dest='logLevel', action='store',
                                 choices=['debug', 'info', 'warning', 'error', 'critical'],
                                 help='Sets logging level to one of debug,info,warning,error,critical. ' +
                                      'Default is logging is disabled')

    def add_arguments(self):
        """
        Configure handling of command line arguments.
        """
        self.add_logging_argument()
        self.parser.add_argument('-a', '--api-host', dest='api_host', action='store', metavar="api_host",
                                 help='{0} API host endpoint'.format(self.product_name))
        self.parser.add_argument('-e', '--email', dest='email', action='store', metavar="e_mail",
                                 help='e-mail that has access to the {0} account'.format(self.product_name))
        self.parser.add_argument('-t', '--api-token', dest='api_token', required=False, action='store',
                                 metavar="api_token",
                                 help='API token for given e-mail that has access to the {0} account'.format(
                                     self.product_name))
        self.parser.add_argument('-z', '--curl', dest='curl', required=False, action='store_true', default=False,
                                 help='Output the corresponding curl command line and exit')

    def _parse_args(self):
        """
        Handles the parse of the command line arguments
        """
        # Perform the actual parsing of the command line arguments
        self.args = self.parser.parse_args()

    def _configure_logging(self):
        """
        Configure logging based on command line options
        """
        if self.args.logLevel is not None:
            logging.basicConfig(level=self.levels[self.args.logLevel])
        logging.info("Set logging level to {0}".format(self.args.logLevel))

    def get_arguments(self):
        """
        CLIs get called back so that they can process any command line arguments
        that are given. This method handles the standard command line arguments for:
        API Host, user, password, etc.
        """

        # We call this first so that logging is enabled as soon as possible
        self._configure_logging()

        # Extract the common command line arguments
        if self.args.api_host is not None:
            self._api_host = self.args.api_host
        if self.args.email is not None:
            self._email = self.args.email
        if self.args.api_token is not None:
            self._api_token = self.args.api_token
        self._curl = self.args.curl

        logging.debug("apihost: {0}".format(self._api_host))
        logging.debug("email: {0}".format(self._email))
        logging.debug("apitoken: {0}".format(self._api_token))

    def set_error_message(self, message):
        """
        Sets the error message to be displayed if an error occurs
        """
        self._message = message

    def _validate_arguments(self):
        """
        Validates the command line arguments passed to the CLI
        Derived classes that override need to call this method before
        validating their arguments
        """
        if self._email is None:
            self.set_error_message("E-mail for the account not provided")
            return False
        if self._api_token is None:
            self.set_error_message("API Token for the account not provided")
            return False
        return True

    def colorize_json(self, json):
        if sys.stdout.isatty():
            return highlight(json, lexers.JsonLexer(), formatters.TerminalFormatter())
        else:
            return json

    def colorize_xml(self, xml):
        if sys.stdout.isatty():
            return highlight(xml, html.XmlLexer(), formatters.TerminalFormatter())
        else:
            return xml

    def _handle_results(self):
        """
        Call back function to be implemented by the CLI.
        Default is to just print the results to standard out
        """
        print(self.colorize_json(self._api_result.text))

    def execute(self):
        """
        Run the steps to execute the CLI
        """

        # Set default arguments from environment variables
        self._get_environment()

        # Call our member function to add command line arguments, child classes that override need
        # to call the ApiCli version first to add standard arguments
        self.add_arguments()

        # Parse the command line arguments
        self._parse_args()

        # Arguments are parsed call back to the instance so that it can extract the command line
        # arguments for its use
        self.get_arguments()

        self.get_api_parameters()
        if self._validate_arguments():
            if self._curl:
                self._curl_output()
            else:
                self._call_api()
                self._handle_results()
        else:
            print(self._message)

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
