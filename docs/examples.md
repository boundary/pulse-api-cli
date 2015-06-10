## Examples

Sample usage of selected Boundary CLIs

### Create a new metric definition
**NOTE** It can take up to a minute to add a create a new metric in a Boundary account

```bash
$ metric-create -n BOUNDARY_FOO_METRIC_IN -d "Boundary Foo Metric In" -s "Foo In" -i "Tracks the Boundary Foo Metric" -g AVG -u number -r 1000
{
  "result": {
    "success": true
  }
}
```

### Add a Measurement Value
**NOTE** Requires that the environment variables as outlined above are set since 

```bash
$ measurement-create -n BOUNDARY_MEASUREMENT_TEST -m 3456 -s foobar
{"result":{"success":true}}
```

### Export metric definitions to a <code>json</code> file

Export all of the metric definitions that begin with `BOUNDARY`

```bash
$ metric-export -p '^BOUNDARY'
{
    "BOUNDARY_FOO_TEST_1": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": 1000,
        "description": "BOUNDARY_FOO_TEST_1",
        "displayName": "BOUNDARY_FOO_TEST_1",
        "displayNameShort": "BOUNDARY_FOO_TEST_1",
        "isDisabled": false,
        "unit": "number"
    },
    "BOUNDARY_HELLO_WORLD": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": 1000,
        "description": "Example metric for the Hello World Boundary meter plugin",
        "displayName": "Hello World",
        "displayNameShort": "Hello World",
        "isDisabled": false,
        "unit": "number"
    }
}

```

### Batch Import Metrics

Given the following `json` file named `metrics.json`:
```json
{
    "BOUNDARY_METRIC_TEST_ONE": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": 0,
        "description": "Boundary test metric one",
        "displayName": "BOUNDARY_METRIC_TEST_TWO",
        "displayNameShort": "BOUNDARY_METRIC_TEST_TWO",
        "isDisabled": false,
        "unit": "bytecount"
    },
    "BOUNDARY_METRIC_TEST_TWO": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": 0,
        "description": "Boundary test metric two",
        "displayName": "BOUNDARY_METRIC_TEST_TWO",
        "displayNameShort": "BOUNDARY_METRIC_TEST_TWO",
        "isDisabled": false,
        "unit": "number"
    }

}
```

Import the metrics into an Boundary account by running the following:

```bash
$ metric-import -f metrics.json
```

