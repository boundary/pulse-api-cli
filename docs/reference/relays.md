## Relays

Commands to administer relays in a TrueSight Pulse account.

### relay-list

**API Documentation**

(http://http://premium-documentation.boundary.com/v1/get/relays)[http://premium-documentation.boundary.com/v1/get/relays]

**Usage**

```bash
usage: plugin-add [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n plugin_name -o
                  organization_name -r respository_name

Imports a meter plugin from a github repository into a TrueSight Pulse account

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
  -n plugin_name, --plugin-name plugin_name
                        Plugin name
  -o organization_name, --organization-name organization_name
                        Name of the github user or organization
  -r respository_name, --repository-name respository_name
                        Name of the github repository
```

**Examples**

Adds a plugin from a github repository `jdgwartney/boundary-plugin-disk-summary` with the name `diskuse-summary` into
a TrueSight Pulse account

```bash
$ plugin-add -n diskuse-summary -o jdgwartney -r boundary-plugin-diskuse-summary
{
  "result": {
    "success": true
  }
}
```

### plugin-get

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/:plugin](http://premium-documentation.boundary.com/v1/get/plugins/:plugin)

**Usage**

```bash
usage: plugin-get [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n plugin_name

Get the details of a plugin in a TrueSight Pulse account

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
  -n plugin_name, --plugin-Name plugin_name
                        Plugin name
```

**Examples**



### plugin-get-components

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/:plugin/components](http://premium-documentation.boundary.com/v1/get/plugins/:plugin/components)

**Usage**

```bash
usage: plugin-get-components [-h] [-l {debug,info,warning,error,critical}]
                             [-a api_host] [-e e_mail] [-t api_token] -n
                             plugin_name

Get the components of a plugin in a TrueSight Pulse account

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
  -n plugin_name, --plugin-Name plugin_name
                        Plugin name
```

**Examples**

Displays runtime and metadata about a plugin `diskuse-summary`

```bash
$ plugin-get-components -n diskuse-summary
{
  "result": {
    "projectId": 7053,
    "pluginName": "diskuse-summary",
    "metrics": [
      "DISKUSE_SUMMARY"
    ],
    "dashboards": [],
    "relays": []
  }
}
```

### plugin-install

**API Documentation**

[http://premium-documentation.boundary.com/v1/put/plugins/installed/:plugin](http://premium-documentation.boundary.com/v1/put/plugins/installed/:plugin)

**Usage**

```bash
usage: plugin-install [-h] [-l {debug,info,warning,error,critical}]
                      [-a api_host] [-e e_mail] [-t api_token] -n plugin_name

Installs a plugin into a TrueSight Pulse account

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
  -n plugin_name, --plugin-name plugin_name
                        Plugin name
```

**Examples**

Installs a plugin `diskuse-summary` into a TrueSight Pulse account so the plugin can be deployed to a meter

```bash
$ plugin-install -n diskuse-summary 
{
  "result": {}
}
```


### plugin-installed

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/installed](http://premium-documentation.boundary.com/v1/get/plugins/installed)

**Usage**

```bash
usage: plugin-installed [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token]

Gets the plugins installed into a TrueSight Pulse account

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

### plugin-list

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins](http://premium-documentation.boundary.com/v1/get/plugins)

**Usage**

```bash
usage: plugin-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                   [-e e_mail] [-t api_token]

Lists the plugins in a TrueSight Pulse account

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

List all of the plugins in a TrueSight Pulse account

```bash
$ plugin-list
{
  "result": {
    "aerospike": {
      "download": "https://github.com/boundary/boundary-plugin-aerospike-server/archive/e6a08431789523419714d14fda725b4578e5e41a.zip",
      "repoUrl": "https://github.com/boundary/boundary-plugin-aerospike-server/tree/e6a08431789523419714d14fda725b4578e5e41a",
      "name": "aerospike",
      "description": "Aerospike Server",
      "postExtract": "npm install",
      "command": "node . --interval $(pollInterval)",
      "ignore": "node_modules",
      
  ...
```

### plugin-remove

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/plugins/private/:plugin](http://premium-documentation.boundary.com/v1/delete/plugins/private/:plugin)

**Usage**

```bash
usage: plugin-remove [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n plugin_name

Remove a staged pre-release meter plugin from a TrueSight Pulse account

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
  -n plugin_name, --plugin-name plugin_name
                        Plugin name
```

**Examples**

Remove a plugin named `diskuse-summary` from an account

```bash
$ plugin-remove -n diskuse-summary 
{
  "result": {
    "success": true
  }
}
```

### plugin-uninstall

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/plugins/installed/:plugin](http://premium-documentation.boundary.com/v1/delete/plugins/installed/:plugin)

**Usage**

```bash
usage: plugin-uninstall [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -n
                        plugin_name [-d] [-r]

Uninstalls a plugin from a TrueSight Pulse account

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
  -n plugin_name, --plugin-name plugin_name
                        Plugin name
  -d, --remove-Dashes   Remove dashboards associated with the plugin
  -r, --remove-Metrics  Remove metrics associated with the plugin
```

**Examples**

Uninstall a plugin from all meters in an account

```bash
$ plugin-uninstall -n diskuse-summary 
{
  "result": {
    "success": true
  }
}
```
