# Boundary CLIs

## Overview

The Boundary CLIs provide command line access to a subset of the Boundary REST APIs as
documented here: [http://premium-documentation.boundary.com/overview](http://premium-documentation.boundary.com/overview).

## Requirements
The Boundary CLIs are implemented in Python and require version 2.7.9 or later
be installed (NOTE: Python 3.x is currently not supported).

## Installation
The Boundary CLIs are distributed via a pip package on
PyPi [https://pypi.python.org/pypi/boundary](https://pypi.python.org/pypi/boundary).
See [Installing](install.md) for complete instructions on installing.

## Authentication

Your Boundary e-mail and API token are used for authentication see [Configuring](configuration.md) for instructions.

## Examples

Sample usage of selected Boundary CLIs. The reference section
the commands.

### Create a new metric definition

```bash
$ metric-create -n BOUNDARY_FOO_METRIC_IN -d "Boundary Foo Metric In" -s "Foo In" -i "Tracks the Boundary Foo Metric" -g AVG -u number -r 1000
{
  "result": {
    "success": true
  }
}
```

### Add a measurement value

```bash
$ measurement-create -n BOUNDARY_MEASUREMENT_TEST -m 3456 -s foobar
{"result":{"success":true}}
```
