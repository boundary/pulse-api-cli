Commands to administer host groups in a Boundary account.

## hostgroup-delete

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

## hostgroup-get

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

## hostgroup-list

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


## hostgroup-search

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
