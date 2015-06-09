## Host Groups
Commands to administer host groups in a Boundary account.

### hostgroup-create

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/hostgroups](http://premium-documentation.boundary.com/v1/post/hostgroups)

**Usage**

```bash
usage: hostgroup-create [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -n
                        host_group_name -s sources

Creates host group definition in a Boundary account

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
  -n host_group_name, --host-group-name host_group_name
                        Host group name
  -s sources, --sources sources
                        Comma separated sources to add to the host group. If
                        empty adds all hosts.
```

**Examples**

Create a host group with a single source/host

```bash
$ hostgroup-create -n 'single-source-hostgroup' -s my-server1
{
  "result": {
    "id": 17876,
    "name": "single-source-hostgroup",
    "hostnames": [
      "my-server1"
    ],
    "system": false
  }
}
```

Create a hostgroup `my-host-group` with multiple sources/hosts `server`, `server2`, and `server 3`

```bash
$ hostgroup-create -n 'my-host-group' -s server1,server2,server3
{
  "result": {
    "id": 17875,
    "name": "my-host-group",
    "hostnames": [
      "server1",
      "server2",
      "server3"
    ],
    "system": false
  }
}
```

### hostgroup-delete

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/hostgroup/:hostgroupId](http://premium-documentation.boundary.com/v1/delete/hostgroup/:hostgroupId)

**Usage**

```bash
usage: hostgroup-delete [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -i
                        host_group_id [-f]

Deletes a host group definition by id from a Boundary account

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
  -i host_group_id, --host-group-id host_group_id
                        Host group id to delete
  -f, --force           Remove the host group, even if in use by a dashboard
                        or alarm
```

**Examples**

```bash
$ hostgroup-delete -i 17874
{
  "result": {
    "success": true
  }
}
```

### hostgroup-get

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/hostgroup/:hostgroupId](http://premium-documentation.boundary.com/v1/get/hostgroup/:hostgroupId)

**Usage**

```bash
usage: hostgroup-get [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -i host_group_id

Retrieves a single host group definition by id from a Boundary account

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
  -i host_group_id, --host-group-id host_group_id
                        Host group id
```

**Examples**

Show the host group definition using the host group id

```bash
$ hostgroup-get -i 17875
{
  "result": {
    "id": 17875,
    "name": "my-host-group",
    "system": false,
    "hostnames": [
      "server1",
      "server2",
      "server3"
    ]
  }
}
```

### hostgroup-list

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/hostgroups](http://premium-documentation.boundary.com/v1/get/hostgroups)

**Usage**

```bash
usage: hostgroup-list [-h] [-l {debug,info,warning,error,critical}]
                      [-a api_host] [-e e_mail] [-t api_token]

Lists the Host Groups in an Boundary account

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

**Examples**

List all of the host groups configured

```bash
$ hostgroup-list
{
  "result": [
    {
      "id": 17877,
      "name": "database-hosts",
      "system": false,
      "hostnames": [
        "db-server1",
        "db-server2",
        "db-server3"
      ]
    },
    {
      "id": 15241,
      "name": "default",
      "system": true,
      "hostnames": []
    },
    {
      "id": 17878,
      "name": "web-hosts",
      "system": false,
      "hostnames": [
        "web-server1",
        "web-server2",
        "web-server3",
        "web-server4",
        "web-server5"
      ]
    }
  ]
}
```

### hostgroup-search

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/hostgroups/search](http://premium-documentation.boundary.com/v1/get/hostgroups/search)

**Usage**

```bash
usage: hostgroup-search [-h] [-l {debug,info,warning,error,critical}]
                        [-a api_host] [-e e_mail] [-t api_token] -n
                        host_group_name

Searches for Host Group by name in an Boundary account

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
  -n host_group_name, --host-group-name host_group_name
                        Host group name
```

**Examples**

Search for a host group name `my-host-group`

```bash
$ hostgroup-search -n 'my-host-group' 
{
  "result": [
    {
      "id": 17873,
      "name": "my-host-group",
      "system": false,
      "hostnames": [
        "red",
        "green",
        "blue"
      ]
    }
  ]
}
```

