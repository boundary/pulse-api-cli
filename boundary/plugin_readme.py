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
import logging

from boundary import ApiCli
from jinja2 import Environment, PackageLoader, Template


class PluginReadme(ApiCli):

    def __init__(self):
        ApiCli.__init__(self)
        self.metric_manifest_path = None
        self.plugin_manifest_path = None
        self.readme_path = None
        self.readme_template_path = None
        self.env = Environment(loader=PackageLoader('boundary', 'templates'))

        self.readme_template = """
# {{plugin_name}}} Plugin


### Prerequisites

#### Supported OS

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |

#### Boundary Meter versions v4.2 or later

- To install new meter go to Settings->Installation or \
[see instructons](https://help.boundary.com/hc/en-us/sections/200634331-Installation).
- To upgrade the meter to the latest version - \
[see instructons](https://help.boundary.com/hc/en-us/articles/201573102-Upgrading-the-Boundary-Meter).

#### For Boundary Meter earlier than v4.2

|  Runtime | node.js | Python | Java |
|:---------|:-------:|:------:|:----:|
| Required |    +    |        |      |

- [How to install node.js?](https://help.boundary.com/hc/articles/202360701)

### Plugin Setup

None

### Plugin Configuration Fields

|Field Name|Description                                       |
|:----------|:------------------------------------------------|
|Disk Name  |The name of the disk to be appended to the hostname to display in the \
legend for the Disk Use Summary templates."|
|Mount Point|The mounted point to check for free space. (either this or the Mounted device \
need to be set for the plugin to function properly)|
|Device     |The mounted device to check for free space. (either this or the Mount Point directory \
need to be set for the plugin to function properly)|
|Poll Interval | How often to poll for metrics |

### Metrics Collected

|Metric Name       |Description               |
|:-----------------|:-------------------------|
|Disk Use Summary  |The percentage of disk used for the given mounted disk|

### Dashboards

None

### References

None

"""

    def add_arguments(self):

        ApiCli.add_arguments(self)

        self.parser.add_argument('-m', '--metric-manifest-path', dest='metric_manifest_path',
                                 action='store', required=False, metavar='path', default=None,
                                 help='Path to metrics.json manifest. Defaults to metrics.json')

        self.parser.add_argument('-p', '--plugin-manifest-path', dest='plugin_manifest_path',
                                 action='store', required=False, metavar='path', default=None,
                                 help='Path to plugin.json manifest. Defaults to plugin.json')

        self.parser.add_argument('-o', '--readme-path', dest='readme_path',
                                 action='store', required=False, metavar='path', default=None,
                                 help='Path to README.md manifest. Defaults to standard out')

        self.parser.add_argument('-r', '--readme-template-path', dest='readme_template_path',
                                 action='store', required=False, metavar='path', default=None,
                                 help='Path to README.md template. Defaults to internal template')

    def get_arguments(self):

        ApiCli.get_arguments(self)

        if self.args.metric_manifest_path is not None:
            self.metric_manifest_path = self.args.metric_manifest_path

        if self.args.metric_manifest_path is not None:
            self.plugin_manifest_path = self.args.metric_manifest_path

    def read_plugin_manifest(self):

        if self.plugin_manifest_path is not None:
            pass

    def generate_readme(self):
        logging.debug("generate README.md")
        logging.debug("metric_manifest_path: " + str(self.metric_manifest_path))
        logging.debug("plugin_manifest_path: " + str(self.plugin_manifest_path))
        logging.debug("readme_path: " + str(self.plugin_manifest_path))
        pass

    def get_description(self):
        return 'Generates README from plugin.json and template'

    def callAPI(self):

        template = self.env.get_template('readme.md')
        context = {}
        context['plugin_name'] = 'Foo'
        print(template.render(context))


