Boundary CLI
============

Boundary CLI provides command line access to Boundary REST APIs
Typical usage often looks like this:

   ```bash
    $ metric-list
   ```

Installation
------------

   ```bash
     $ pip install boundary_cli
   ```

Configuration
-------------
The Boundary CLI uses environment variables for configuration information (user, password, etc) to execute against the Boundary REST APIs, and optionally this information can be overridden via the command line

### Environment Variables
| Environment Variable                  | Description                    |
|:--------------------------------------|:-------------------------------|
| <pre>BOUNDARY_API_HOST</pre>          | Boundary API host              |
| <pre>BOUNDARY_EMAIL</pre>             | Boundary email                 |
| <pre>BOUNDARY_API_TOKEN</pre>         | Boundary API token             |


Examples
--------
Usage of the Boundary CLI

### metric-create

```bash
$ metric-create FOO "foo bar" "foo" "it's the foo" sum number
{
  "result": {
    "success": true
  }
}
```

### Add a Metric Value

```bash
$ metric-add myhost LOAD_1_MINUTE 30
{
  "result": {
    "success": true
  }
}
```

### metric-list

```bash
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
```


Command Reference
-----------------

### Metric
Commands to administer metrics in Boundary

#### metric-add
Creates a new measurement value in Boundary

````bash
usage: metric-add source metric measure
```

#### metric-delete
Creates/updates a Boundary Premium metric definition

    ```bash
    $ metric-create -h
    usage: metric-create [-h] [-a APIHOST] [-e EMAIL] [-t APITOKEN] [-v] -m NAME
                     [-d DISPLAYNAME] [-s DISPLAYNAMESHORT] [-i DESCRIPTION]
                     [-g AGGREGATE] [-u UNIT] [-r RESOLUTION] [-x]

    Creates a new metric definition in an Boundary account

    optional arguments:
      -h, --help            show this help message and exit
      -a APIHOST, --api-host APIHOST
                        API endpoint
      -e EMAIL, --email EMAIL
                        e-mail used to create the Boundary account
      -t APITOKEN, --api-token APITOKEN
                        API token to access the Boundary Account
      -v, --verbose         verbose mode
      -m NAME, --name NAME  Metric identifier
      -d DISPLAYNAME, --display-name DISPLAYNAME
                        Metric display name
      -s DISPLAYNAMESHORT, --display-name-short DISPLAYNAMESHORT
                        Metric short display name
      -i DESCRIPTION, --description DESCRIPTION
                        Metric description
      -g AGGREGATE, --aggregate AGGREGATE
                        Metric default aggregate
      -u UNIT, --unit UNIT  Metric unit
      -r RESOLUTION, --resolution RESOLUTION
                        Metric default resolution
      -x, --is-disabled     verbose mode

    ```

#### metric-delete

   ```bash
    usage: metric-delete <name>
   ```

#### metric-list
Lists the metric definitions in your Boundary instance.

   ```bash
    usage: metric-list
   ```

### Plugins

#### plugin-add

#### plugin-delete

#### plugin-get

#### plugin-get-components

#### plugin-install

#### plugin-installed

#### plugin-list

#### plugin-remove

#### plugin-uninstall`

### Sources

#### source-delete

    ```
    $ source-delete <source> <metric id>
    ```


#### source-list

Lists all sources in your Boundary instance

    ```
    $ source-list
    ```

### User

### `user-get`







