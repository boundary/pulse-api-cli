Metric Definition
-----------------


Examples
--------
Usage of the Boundary CLI

### Create a new metric definition
**NOTE** It can take up to a minute to add a create a new metric in a Boundary account

```bash
$ metric-create -n BOUNDARY_FOO_METRIC_IN -d "Boundary Foo Metric In" -s "Foo In" -i "Tracks the Boundary Foo Metric" -g avg -i number -r 1000
{
  "result": {
    "success": true
  }
}
```

### Reference a metric definition in another account

Adds a already defined metric definition into an acounnt

```bash
$ metric-ref -n BOUNDARY_BIG_BYTES_OUT
```

### Add a Measurement Value
**NOTE** Requires that the environment variables as outlined above are set since 

```bash
$ measurement-create -n BOUNDARY_MEASUREMENT_TEST -m 3456 -s foobar
{"result":{"success":true}}
```

### List all of the metric definitions
`metric-list` provides complete details of each of the metrics installed into an account
```bash
$ metric-list
{
  "result": [
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
```

### Export metric definitions to a <code>json</code> file

Export all of the metric definitions that begin with `BOUNDARY`
```bash
$ metric-export -p '^BOUNDARY'
{
    "result": [
        {
            "defaultAggregate": "ave",
            "defaultResolutionMS": 1000,
            "description": "Example Metric",
            "displayName": "Boundary Big Bytes Out",
            "displayNameShort": "B Out",
            "isDisabled": 0,
            "name": "BOUNDARY_BIG_BYTES_OUT",
            "unit": "number"
        }
    ]
}

```

### Batch Import Metrics
**Note** It can take up a to a minute per metric definition that is added to a Boundary account

Given the following `json` file named `metrics.json`:
```json
{
    "result": [
        {
            "defaultAggregate": "ave",
            "defaultResolutionMS": 1000,
            "description": "Example Metric",
            "displayName": "Boundary Big Bytes Out",
            "displayNameShort": "B Out",
            "isDisabled": 0,
            "name": "BOUNDARY_BIG_BYTES_OUT",
            "unit": "number"
        }
    ]
}
```

Import the metrics into an account

```bash
$ metric-import -f metrics.json
```

