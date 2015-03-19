Boundary CLI
============

Boundary CLI provides command line access to Boundary REST APIs

Installation
------------

   ```bash
     $ pip install boundary
   ```

Configuration
-------------
The Boundary CLI uses environment variables for configuration information (user, password, etc) to execute against the Boundary REST APIs, and optionally this information can be overridden via the command line.

### Environment Variables
| Environment Variable                  | Description                    |
|:--------------------------------------|:-------------------------------|
| <pre>BOUNDARY_API_HOST</pre>          | Boundary API host              |
| <pre>BOUNDARY_EMAIL</pre>             | Boundary email                 |
| <pre>BOUNDARY_API_TOKEN</pre>         | Boundary API token             |

### Common Command Line Arguments

| Argument | Description                                    |
|:---------|:-----------------------------------------------|
|help      | shows the command help and exits               |
|log level | configures output of command execution         |
|api host  | Boundary API host endpont                      |
|e-mail    | E-mail that has access to the Boundary account |
   ```bash
   usage: <command name> [-h] [-l {debug,info,warning,error,critical}]
                       [-a api_host] [-e e_mail] [-t api_token] -n metric_name

  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
  ```
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
**NOTE** Requires that the environment variables as outlined above are set since they cannot be passed on the command line. This command also depends on curl being on the `PATH`. A later release will remove this command and subsitute with a new command `measurement-create` which will have the same capability but named arguments.

```bash
$ metric-add myhost LOAD_1_MINUTE 30
{
  "result": {
    "success": true
  }
}
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

Command Reference
-----------------

### Actions

#### action-installed

   ```bash
usage: action-installed [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token]

Returns the actions associated with the Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
   ```

#### action-types

   ```bash
usage: action-types [-h] [-l {debug,info,warning,error,critical}]
                    [-a api_host] [-e e_mail] [-t api_token]

List action types associated with the Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
   ```
### Alarms

#### alarm-list

   ```bash
usage: alarm-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token]

List alarm definitions associated with the Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
   ```
### Host Groups

#### hostgroup-create
   ```bash
usage: hostgroup-create [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -n
                        host_group_name -s sources

Creates host group definition in a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
  -n host_group_name, --host-group-name host_group_name
                        Host group name
  -s sources, --sources sources
                        Comma separated sources to add to the host group. If
                        empty adds all hosts.
   ```
### Metric
Commands to administer metrics and generate measurements in Boundary

#### measurement-add
Creates a new measurement value in Boundary

````bash
usage: measurement-add [-h] [-l {debug,info,warning,error,critical}]
                       [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                       -m measurement [-s source] [-d timestamp]

Adds a measurement value to a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
  -n metric_name, --metric-name metric_name
                        Metric identifier
  -m measurement, --measurement measurement
                        Measurement value
  -s source, --source source
                        Source of measurement. Defaults to the host where the
                        command is run
  -d timestamp, --timestamp timestamp
                        Time of occurrence of the measurement in either epoch
                        seconds or epoch milliseconds. Defaults to the receipt
                        time at Boundary
```

### metric-create

   ```bash
usage: metric-create [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                     [-d display_name] [-s display_short_name]
                     [-i description] [-g {sum,avg,max,min}]
                     [-u {percent,number,bytecount,duration}] [-r resolution]
                     [-x]

Creates a new metric definition in an Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
  -n metric_name, --metric-name metric_name
                        Metric identifier
  -d display_name, --display-name display_name
                        Metric display name
  -s display_short_name, --display-name-short display_short_name
                        Metric short display name
  -i description, --description description
                        Metric description
  -g {sum,avg,max,min}, --aggregate {sum,avg,max,min}
                        Metric default aggregate
  -u {percent,number,bytecount,duration}, --unit {percent,number,bytecount,duration}
                        Metric unit
  -r resolution, --resolution resolution
                        Metric default resolution
  -x, --is-disabled     disable metric
  ```

#### metric-delete

   ```bash
usage: metric-delete [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name

Deletes a metric definition from a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
  -n metric_name, --metric-name metric_name
                        Metric identifier

   ```
#### metric-export

   ```bash
usage: metric-export [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] [-p pattern]

Export the metric definitions from a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
  -p pattern, --pattern pattern
                        text pattern to use search the name of the metric
   ```

#### metric-import

   ```
$ metric-import -h
usage: metric-import [-h] [-a api_host] [-e e_mail] -f path [-t api_token]

Import metric definitions

optional arguments:
  -h, --help            show this help message and exit
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -f path, --file path  Path to JSON file
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
```

#### metric-list

   ```bash
usage: metric-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                   [-e e_mail] [-t api_token]

Lists the defined metrics in a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account

   ```
#### metric-ref

   ```bash
usage: metric-ref [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n metric_name

Adds an existing metric definition to a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
  -n metric_name, --metric-name metric_name
                        Metric identifier
   ```

### Plugins

Commands to manage meter plugins in a Boundary account

#### plugin-add

```bash
usage: plugin-add [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n plugin_name -o
                  organization_name -r respository_name

Imports a meter plugin from a github repository into a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
  -n plugin_name, --plugin-name plugin_name
                        Plugin name
  -o organization_name, --organization-name organization_name
                        Name of the github user or organization
  -r respository_name, --repository-name respository_name
                        Name of the github user or organization
```

#### plugin-delete

#### plugin-get

#### plugin-get-components

#### plugin-install

#### plugin-installed

#### plugin-list

#### plugin-remove

#### plugin-uninstall


### User

### user-get

   ```bash
usage: user-get [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                [-e e_mail] [-t api_token]

Returns the user associated with the account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        Boundary account
   ```







