Boundary API CLI
==================

Commandline scripts that use Boundary APIs.

Prerequisites
-------------

### Required At Runtime

1. Bash Shell, version 3.2.X or later
2. [Curl](http://curl.haxx.se/), a command line tool for transferring data with URL syntax
3. [jq JSON processor](http://stedolan.github.io/jq/) a lightweight and flexible command-line JSON processor

### Required For Installation Only
1. [wget](https://www.gnu.org/software/wget/),package for retrieving files using HTTP, HTTPS and FTP. (required for installtion only)
2. [unzip](http://gnuwin32.sourceforge.net/packages/unzip.htm), UnZip is an extraction utility for archives compressed in .zip format. (required for  installation only)


Installation
------------

### Install Bash Shell
Most Linux/Unix environments already have the Bash Shell installed and configured as the default shell.

For Windows install [Win-Bash](http://win-bash.sourceforge.net) or other Bash Shell distribution for Windows

### Install Jq
Download the binaries for [jq](http://stedolan.github.io/jq/) from [here](http://stedolan.github.io/jq/download/) for you specific platform.

### Install Boundary API Shell
1. Download the distribution from this [link](https://github.com/jdgwartney/boundary-api-shell/archive/RE-00.01.00.zip):

    ```bash
    $ curl https://github.com/jdgwartney/boundary-api-shell/archive/RE-00.02.00.zip
    ```
2. Change directory to directory where the distribution was downloaded:

    ```bash
    $ cd distribution_directory
    ```
    
3. Extract the distribution

    ```bash
    $ unzip RE-00.02.00.zip
    ```
    
Configuration
-------------
The Boundary API CLI uses environment variable for configuration information (user, password, etc) for executing curl commands that use the Boundary REST APIs.

### Environment Variables
| Environment Variable                    | Description                    |
|:----------------------------------------|:-------------------------------|
| <pre>BOUNDARY_API_HOST</pre>          | Boundary API host              |
| <pre>BOUNDARY_EMAIL</pre>             | Boundary email                 |
| <pre>BOUNDARY_API_TOKEN</pre>         | Boundary API token             |

Using
-----
1. Change directory to the unpacked distribution
2. Source `env.sh`:

```bash
$ source env.sh
```

The Boundary API commands have now been added to your `PATH`

Adding to Your Profile
----------------------

The `env.h` can be configured to run at login by adding the following to your `.bash_profile`

```bash
[[ -r <path to distribution>/env.sh ]] && source <path to distribution>/env.sh
```

Run Script Template
-------------------
The following is run script template that can be used to configure environment variables

```bash
BOUNDARY_API_HOST=premium-api.boundary.com
BOUNDARY_API_TOKEN=
BOUNDARY_EMAIL=
```

1. Create a sub directory in your in your `HOME` directory name `.boundary` and add the above template into a file named `config`.

1. Add the following to your `$HOME/.bash_profile`:

```bash
[[ -r "$HOME/.config" ]] && source "$HOME/.config"
```

This will set the environment variables whenever you login.

Examples
--------
Usage of the Boundary API Shell

### `metric-create`

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

### `metric-list`

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

### `meter-list`

```bash
$ meter-list
[
  {
    "id": "8k1zTp62kqBDhMXP3g",
    "obs_domain_id": "11",
    "cert_serial_number": "8k1zTp62kqBDhMXP3h",
    "org_id": "ChMBk5Ou9QBdDPaTai0rfUbZ8bC",
    "name": "boundary-splunk",
    "created_at": 1400787749,
    "updated_at": 1408200754,
    "links": [
      {
        "rel": "self",
        "href": "https://api.boundary.com/ChMBk5Ou9QBdDPaTai0rfUbZ8bC/meters/8k1zTp62kqBDhMXP3g"
      },
      {
        "rel": "cert",
        "href": "https://api.boundary.com/ChMBk5Ou9QBdDPaTai0rfUbZ8bC/meters/8k1zTp62kqBDhMXP3g/cert.pem"
      },
      {
        "rel": "key",
        "href": "https://api.boundary.com/ChMBk5Ou9QBdDPaTai0rfUbZ8bC/meters/8k1zTp62kqBDhMXP3g/key.pem"
      }
    ],
    "tags": [],
    "features": [],
    "connected": "true",
    "connected_at": "1406409472397",
    "export_address": "10.1.0.3",
    "meter_version": "2.0.4-261",
    "nic_driver": [
      "virtio_net"
    ],
    "nic_driver_version": [
      "1.0.0"
    ],
    "nic_firmware_version": [
      ""
    ],
    "nic_id": [
      "0"
    ],
    "nic_ip": [
      "10.1.0.3"
    ],
    "nic_mac": [
      "fa:16:3e:98:ca:83"
    ],
    "nic_name": [
      "eth0"
    ],
    "os_distribution_name": "Fedora 20 (Heisenbug)",
    "os_machine": "x86_64",
    "os_node_name": "boundary-splunk",
    "os_release": "3.11.10-301.fc20.x86_64",
    "os_sysname": "Linux",
    "os_version": "#1 SMP Thu Dec 5 14:01:17 UTC 2013"
  },
  ...
```

### Tag a Meter

```bash
$ meter-tag 8k0DJnjjxuDvcoTvOK foobar
```

Command Reference
-----------------

### Event
Commands to interact with Boundary events

#### `event-create`
Inserts a new Raw Event into Boundary Enterprise

``` bash
usage: event-create <event>
```

#### `event-list`
List the events in your Boundary instance

``` bash
usage: event-list
```

#### `event-query`
Queries the events in your Boundary instance

``` bash
usage: event-query <query>
```

### Meter
Commands to administer Boundary Enterprise meters

#### `meter-create`
Creates a new meter definition in Boundary Enterprise

````bash
usage: meter-create name
```

#### `meter-list`
Lists the meters in Boundary Enterprise

````bash
usage: meter-list [id]
```
#### `meter-tag`
Adds a tag to a Boundary Enterprise Meter

```bash
usage: meter-tag meter_id tag
```

### Metric
Commands to administer metrics in Boundary

#### `metric-add`
Creates a new measurement value in Boundary

````bash
usage: metric-add source metric measure
```

#### `metric-delete`
Creates/updates a Boundary Premium metric definition

```bash
usage: metric-create <name> <display-name> <display-name_short> <description> <aggregate> <unit> <defaultResolutionMS>
where:
  name - Name of the metric
  display-name - Name displayed in the Web UI
  display-name-short - Shorter display name
  description - Description of the metric (also used as tooltip)
  aggregate - Type of aggregate (sum, avg, max, or min)
  unit - Type of measurement (percent, number, bytecount, or duration )
```
#### `metric-delete`

```bash
usage: metric-delete <name>
```

#### `metric-list`
Lists the metric definitions in your Boundary instance.

```bash
usage: metric-list
```

### Plugin


### Sources

#### `source-delete`

```
$ source-delete <source> <metric id>
```


#### `source-list`

Lists all sources in your Boundary instance

```
$ source-list
```

### User

### `user-get`







