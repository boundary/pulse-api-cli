#!/usr/bin/env python
###
### Copyright 2014-2015, Boundary
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

import json
from pprint import pprint
import sys

'''
Reads and provides access to a plugin.json file the manifest of plugins.
'''
class PluginManifest():

  def __init__(self,path=None):
    '''
    Initialize the PluginManifest instance
    '''
    self.path = path
    self.manifest_json = None
    self.manifest = None
      
  def getMetricNames(self):
    '''
    Returns the list of metrics associated with the plugin manifest
    '''
    return self.manifest['metrics']

  def load(self):
    '''
    Load the metrics file from the given path
    '''
    f = open(self.path,"r")
    self.manifest_json = f.read()

  def parse(self):
    '''
    Parses the manifest JSON into a dictionary
    '''
    self.manifest = json.loads(self.manifest_json)

  def get(self):
    '''
    Read the JSON file and parse into a dictionary
    '''
    self.load()
    self.parse()

  def getManifest(self):
    '''
    Returns the dictionary from the parse JSON plugin manifest
    '''
    return self.manifest

if __name__ == "__main__":
  if len(sys.argv) != 2:
      sys.stderr.write("No file")
      sys.exit(1)
      
  p = PluginManifest(sys.argv[1])
  p.get()
  pprint(p.getManifest())
  pprint(p.getMetricNames())
