## Relays

Commands to administer relays in a TrueSight Pulse account.

### relay-list

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/relays](http://premium-documentation.boundary.com/v1/get/relays)

**Usage**

```bash
usage: relay-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token]

Lists the relays in a TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
```

**Examples**

Lists the relays in a TrueSight Pulse account

```bash
$ relay-list
{
  "result": {
    "success": true
  }
}
```

### relay-get-config

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/:plugin](http://premium-documentation.boundary.com/v1/get/plugins/:plugin)

**Usage**

```bash
usage: relay-get-config [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -n meter_name
                        [-s timestamp]

Returns relay configuration from a TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -n meter_name, --name meter_name
                        Name of the meter to set plugin configuration
                        information
  -s timestamp, --since timestamp
                        Unix timestamp of when configuration was last checked.
                        If configuration has not changed, null is returned.
```

**Examples**

Display the configuration for the relay `web-01`

```bash
$ relay-get-config -n web-01
{
  "result": {
    "config": {
      "metrics": {
        "APACHE_BUSY_RATIO": {
          "name": "APACHE_BUSY_RATIO"
        },
        "APACHE_BUSY_WORKERS": {
          "name": "APACHE_BUSY_WORKERS"
        },
        "APACHE_BYTES_PER_REQUEST": {
          "name": "APACHE_BYTES_PER_REQUEST"
        },
        "APACHE_CPU": {
          "name": "APACHE_CPU"
        },
        "APACHE_IDLE_WORKERS": {
          "name": "APACHE_IDLE_WORKERS"
        },
        "APACHE_REQUESTS": {
...
```

