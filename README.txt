============
Boundary CLI
============

Boundary CLI provides command line access to Boundary REST APIs
Typical usage often looks like this::

    $ metric-list

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


Configuration
=============

The Boundary API CLI uses environment variable for configuration information (user, password, etc).

### Environment Variables
| Environment Variable                    | Description                    |
|:----------------------------------------|:-------------------------------|
| <pre>BOUNDARY_API_HOST</pre>          | Boundary API host              |
| <pre>BOUNDARY_EMAIL</pre>             | Boundary email                 |
| <pre>BOUNDARY_API_TOKEN</pre>         | Boundary API token             |


Command Reference
=================

Metrics
-------

metric-add
~~~~~~~~~~
::
    $ metric-add myhost LOAD_1_MINUTE 30
    {
      "result": {
        "success": true
      }
    }

metric-create
~~~~~~~~~~~~~

usage: metric-create <name> <display-name> <display-name_short> <description> <aggregate> <unit> <defaultResolutionMS>
where:
  name - Name of the metric
  display-name - Name displayed in the Web UI
  display-name-short - Shorter display name
  description - Description of the metric (also used as tooltip)
  aggregate - Type of aggregate (sum, avg, max, or min)
  unit - Type of measurement (percent, number, bytecount, or duration )
  defaultResolutionMS - 

$ metric-create FOO "foo bar" "foo" "it's the foo" sum number
{
  "result": {
    "success": true
  }
}

metric-delete
~~~~~~~~~~~~~

### Add a Metric Value

metric-list
~~~~~~~~~~

$ metric-list
{
  "result": [{
    {
      "id": 6028,
      "name": "LOAD_1_MINUTE",
      "displayName": "CPU Load 1 Minute",
      "description": "CPU load for the last minute",
      "drillFromMetricName": null,
      "unit": "number",
      "catalogId": 2110,
      "displayNameShort": "Load 1 Minute",
      "defaultAggregate": "avg",
      "isDisabled": 0,
      "isDeleted": 0,
      "isBuiltin": 0
    },
...



````bash
usage: metric-add source metric measure
```

#### `metric-delete`
Creates/updates a Boundary Premium metric definition


```bash
usage: metric-delete <name>
```

#### `metric-list`
Lists the metric definitions in your Boundary instance.


Plugins
-------

plugin-add
~~~~~~~~~~

plugin-delete
~~~~~~~~~~~~~

plugin-get
~~~~~~~~~~

plugin-get-components
~~~~~~~~~~~~~~~~~~~~~

plugin-install
~~~~~~~~~~~~~~

plugin-installed
~~~~~~~~~~~~~~~~

plugin-list
~~~~~~~~~~~

plugin-remove
~~~~~~~~~~~~~

plugin-uninstall
~~~~~~~~~~~~~~~~

Sources
-------

source-delete
~~~~~~~~~~~~~

Delete a source from your boundary instance

$ source-delete <source> <metric id>


source-list
~~~~~~~~~~~

Lists all sources in your Boundary instance

$ source-list

User
---

user-get
~~~~~~~~







