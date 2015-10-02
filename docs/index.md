# BMC TrueSight Pulse CLIs

## Overview

The BMC TrueSight Pulse CLIs provide command line access to a subset of the TrueSight Pulse REST APIs as
documented here: [http://premium-documentation.boundary.com/overview](http://premium-documentation.boundary.com/overview).

## Requirements
The TrueSight Pulse CLIs are implemented in Python and require version 2.7.9 or later
be installed (NOTE: Python 3.x is currently not supported).

## Installation
The TrueSight Pulse CLIs are distributed via a pip package on
PyPi [https://pypi.python.org/pypi/boundary](https://pypi.python.org/pypi/boundary).
See [Installing](install.md) for complete instructions on installing.

## Authentication

Your TrueSight Pulse e-mail and API token are used for authentication see [Configuring](configuration.md) for instructions.

## Examples

Sample usage of selected TrueSight Pulse CLIs. The reference section
the commands.

### Create a new metric definition

```bash
$ metric-create -n TRUESIGHT_PULSE_FOO_METRIC_IN -d "TrueSight Pulse Foo Metric In" -s "Foo In" -i "Tracks the TrueSight Pulse Foo Metric" -g AVG -u number -r 1000
{
  "result": {
    "success": true
  }
}
```

### Add a measurement value

```bash
$ measurement-create -n TRUESIGHT_PULSE_MEASUREMENT_TEST -m 3456 -s foobar
{"result":{"success":true}}
```
