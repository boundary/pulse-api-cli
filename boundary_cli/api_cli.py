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
from pprint import pprint
from plugin_manifest import PluginManifest
import logging
import os
import sys

import requests

'''
Base class for all the Boundary CLI commands
'''
class ApiCli():

  def __init__(self):
    self.path = None
    self.apihost = None
    self.email = None
    self.apikey = None
    self.parser = argparse.ArgumentParser(description=self.getDescription())
    self.paths="v1/metrics"

  def getDescription(self):
    return "General API CLI"

  def getEnvironment(self):
    try:
      self.email = os.environ['BOUNDARY_EMAIL']
    except(KeyError):
      self.email = None
    try:
      self.apikey = os.environ['BOUNDARY_API_TOKEN']
    except(KeyError):
      self.apikey = None
    try:
      self.apihost = os.environ['BOUNDARY_API_HOST']
    except(KeyError):
        self.apihost = 'premium-api.boundary.com'

  def addArguments(self):
    '''
    Configure handling of command line arguments.
    '''
    self.parser.add_argument('-e','--email',dest='email',action='store',help='e-mail used to create the Boundary account')
    self.parser.add_argument('-t','--api-token',dest='apitoken',required=False,action='store',help='API token to access the Boundary Account')
    self.parser.add_argument('-v', dest='verbose', action='store_true',help='verbose mode')
    
  def parseArgs(self):

    self.addArguments()

    self.args = self.parser.parse_args()

  def getMetricDefinition(self,name):
      '''
      Make an API call to get the metric definition
      '''
      metric = None
      url = "https://{0}/{1}".format(self.apihost,self.path)
      r = requests.get(url, auth=(self.email, self.apikey))
      if r.status_code != 200:
          print(url)
          print(r)
      print(r.text)
  
    
  def execute(self):
    self.parseArgs()
    print("execute") 

if __name__ == "__main__":
  c = ApiCli()
  c.execute()
