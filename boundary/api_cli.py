#!/usr/bin/env python
###
### Copyright 2014-2015 Boundary, Inc.
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###     http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
###

import argparse
import json
import logging
import os
import requests
import urllib2
import urllib

'''
Base class for all the Boundary CLI commands
'''
class ApiCli():

  def __init__(self):
    self.message = None
    self.path = None
    self.apihost = "premium-api.boundary.com"
    self.email = None
    self.apitoken = None
    self.parser = argparse.ArgumentParser(description=self.getDescription())
    self.scheme = "https"
    self.path = None
    self.url_parameters = None
    self.method = "GET"
    self.data = None
    
    # Construct a dictionary with each of the HTTP methods that we support
    self.methods = {"DELETE": self.doDelete,"GET": self.doGet,"POST": self.doPost,"PUT": self.doPut}

  def getDescription(self):
    '''
    Returns a description of the CLI
    '''
    return "General API CLI"

  def getEnvironment(self):
    '''
    Gets the configuration stored in environment variables
    '''
    try:
      self.email = os.environ['BOUNDARY_EMAIL']
    except(KeyError):
      self.email = None
    try:
      self.apitoken = os.environ['BOUNDARY_API_TOKEN']
    except(KeyError):
      self.apitoken = None
    try:
      self.apihost = os.environ['BOUNDARY_API_HOST']
    except(KeyError):
      self.apihost = 'premium-api.boundary.com'

  def addArguments(self):
    '''
    Configure handling of command line arguments.
    '''
    self.parser.add_argument('-v', '--verbose',dest='verbose', action='store_true', help='verbose mode')
    self.parser.add_argument('-a', '--api-host',dest='apihost',action='store',metavar="api_host",help='API host endpoint')
    self.parser.add_argument('-e', '--email',dest='email',action='store',metavar="e_mail",help='e-mail used to create the Boundary account')
    self.parser.add_argument('-t', '--api-token',dest='apitoken',required=False,action='store',metavar="api_token",help='API token to access the Boundary account')
    
  def parseArgs(self):
    '''
    Handles the parse of the command line arguments
    '''
    self.addArguments()
    self.args = self.parser.parse_args()
    
  def getArguments(self):
    '''
    CLIs get called back so that they can process any command line arguments
    that are given. This method handles the standard command line arguments for:
    API Host, user, password, etc.
    '''
    if self.args.apihost != None:
        self.apihost = self.args.apihost
    if self.args.email != None:
        self.email = self.args.email
    if self.args.apitoken != None:
        self.apitoken = self.args.apitoken
      
  def setErrorMessage(self,message):
        self.message = message
      
  def validateArguments(self):
    if self.email == None:
        self.setErrorMessage("E-mail for the account not provided")
        return False
    if self.apitoken == None:
        self.setErrorMessage("API Token for the account not provided")
        return False
    return True

  def getUrlParameters(self):
    urlParameters = ""
    if self.url_parameters != None:
        urlParameters = "?"
        values = self.url_parameters
        first = True
        for key in values:
            if first == True:
                first = False
            else:
                urlParameters = urlParameters + "&"
            urlParameters = urlParameters + "{0}={1}".format(key,values[key])
    return urlParameters

  def doGet(self):
    '''
    HTTP Get Request
    '''
    return requests.get(self.url,auth=(self.email,self.apitoken),data=self.data)

  def doDelete(self):
    '''
    HTTP Delete Request
    '''
    return requests.delete(self.url,auth=(self.email,self.apitoken),data=self.data)

  def doPost(self):
    return requests.post(self.url,auth=(self.email,self.apitoken),data=self.data)

  def doPut(self):
    '''
    HTTP Put Request
    '''
    return requests.put(self.url,auth=(self.email,self.apitoken),data=self.data)

  def callAPI(self):
    '''
    Make an API call to get the metric definition
    '''

    self.url = "{0}://{1}/{2}{3}".format(self.scheme,self.apihost,self.path,self.getUrlParameters())

    result = self.methods[self.method]()
    if result.status_code != urllib2.httplib.OK:
        print(self.url)
        if self.data != None:
            print(self.data)
        print(result)
    self.handleResults(result)
      
  def handleResults(self,result):
    '''
    Call back function to be implemented by the CLI.
    Default is to just print the results to standard out
    '''
    print(result.text)
  
  def execute(self):
    '''
    Run the steps to execute the CLI
    '''
    self.getEnvironment()
    self.parseArgs()
    self.getArguments()
    if self.validateArguments() == True:
        self.callAPI()
    else:
        print(self.message)

