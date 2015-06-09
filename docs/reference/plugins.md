## Plugins

Commands to administer plugins in a Boundary account.

### plugin-add

**API Documentation**

(http://premium-documentation.boundary.com/v1/put/plugins/private/:plugin/:org/:repo)[http://premium-documentation.boundary.com/v1/put/plugins/private/:plugin/:org/:repo]

**Usage**

```bash
usage: plugin-add [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n plugin_name -o
                  organization_name -r respository_name

Imports a meter plugin from a github repository into a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
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
                        Name of the github repository
```

### plugin-get

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/:plugin](http://premium-documentation.boundary.com/v1/get/plugins/:plugin)

**Usage**

```bash
usage: plugin-get [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n plugin_name

Get the details of a plugin in a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
  -n plugin_name, --plugin-Name plugin_name
                        Plugin name
```

### plugin-get-components

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/:plugin/components](http://premium-documentation.boundary.com/v1/get/plugins/:plugin/components)

**Usage**

```bash
usage: plugin-get-components [-h] [-l {debug,info,warning,error,critical}]
                             [-a api_host] [-e e_mail] [-t api_token] -n
                             plugin_name

Get the components of a plugin in a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
  -n plugin_name, --plugin-Name plugin_name
                        Plugin name
```

### plugin-install

**API Documentation**

[http://premium-documentation.boundary.com/v1/put/plugins/installed/:plugin](http://premium-documentation.boundary.com/v1/put/plugins/installed/:plugin)

**Usage**

```bash
usage: plugin-install [-h] [-l {debug,info,warning,error,critical}]
                      [-a api_host] [-e e_mail] [-t api_token] -n plugin_name

Installs a plugin into a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
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
```

### plugin-installed

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins/installed](http://premium-documentation.boundary.com/v1/get/plugins/installed)

**Usage**

```bash
usage: plugin-installed [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token]

Gets the plugins installed into a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
```

### plugin-list

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/plugins](http://premium-documentation.boundary.com/v1/get/plugins)

**Usage**

```bash
usage: plugin-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                   [-e e_mail] [-t api_token]

Lists the plugins in a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        Boundary API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the Boundary account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        Boundary account
```

### plugin-remove

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/plugins/private/:plugin](http://premium-documentation.boundary.com/v1/delete/plugins/private/:plugin)

**Usage**

```bash
usage: plugin-remove [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n plugin_name

Remove a staged pre-release meter plugin from a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
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
```

### plugin-uninstall

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/plugins/installed/:plugin](http://premium-documentation.boundary.com/v1/delete/plugins/installed/:plugin)

**Usage**

```bash
usage: plugin-uninstall [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -n
                        plugin_name [-d] [-r]

Uninstalls a plugin from a Boundary account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
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
  -d, --remove-Dashes   Remove dashboards associated with the plugin
  -r, --remove-Metrics  Remove metrics associated with the plugin
```
