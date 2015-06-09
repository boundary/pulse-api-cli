## Metrics
Commands to administer metric definitions in a Boundary account.


### metric-create

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/metrics](http://premium-documentation.boundary.com/v1/post/metrics)

**Usage**

```bash
usage: metric-create [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                     -d display_name -s display_short_name [-i description] -g
                     {AVG,MAX,MIN,SUM} -u {percent,number,bytecount,duration}
                     [-r resolution] [-x]

Creates a new metric definition in an Boundary account

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
  -n metric_name, --metric-name metric_name
                        Metric identifier
  -d display_name, --display-name display_name
                        Metric display name
  -s display_short_name, --display-name-short display_short_name
                        Metric short display name
  -i description, --description description
                        Metric description
  -g {AVG,MAX,MIN,SUM}, --aggregate {AVG,MAX,MIN,SUM}
                        Metric default aggregate
  -u {percent,number,bytecount,duration}, --unit {percent,number,bytecount,duration}
                        Metric unit
  -r resolution, --resolution resolution
                        Metric default resolution
  -x, --is-disabled     Disable metric

```


### metric-delete

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/metrics/:metric](http://premium-documentation.boundary.com/v1/delete/metrics/:metric)

**Usage**

```bash
usage: metric-delete [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name

Deletes a metric definition from a Boundary account

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
  -n metric_name, --metric-name metric_name
                        Metric identifier
```

### metric-export

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/metrics](http://premium-documentation.boundary.com/v1/get/metrics)

**Usage**

```bash
usage: metric-export [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] [-p pattern]

Export the metric definitions from a Boundary account

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
  -p pattern, --pattern pattern
                        regular expression pattern to use search the name of
                        the metric
```

### metric-get

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/metrics](http://premium-documentation.boundary.com/v1/get/metrics)

**Usage**

```bash
usage: metric-get [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n metric_name

Lists the defined metrics in a Boundary account

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
  -n metric_name, --metric-name metric_name
                        Metric identifier
```

### metric-import

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/metrics](http://premium-documentation.boundary.com/v1/post/metrics)

**Usage**

```bash
usage: metric-import [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -f path

Imports metric definitions from a file into a Boundary account

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
  -f path, --file path  Path to JSON file
```

### metric-update

**API Documentation**

[http://premium-documentation.boundary.com/v1/put/metrics/:metricName](http://premium-documentation.boundary.com/v1/put/metrics/:metricName)

**Usage**

```bash
usage: metric-update [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                     -d display_name -s display_short_name [-i description] -g
                     {AVG,MAX,MIN,SUM} -u {percent,number,bytecount,duration}
                     [-r resolution] [-x]

Updates a metric definition in an Boundary account

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
  -n metric_name, --metric-name metric_name
                        Metric identifier
  -d display_name, --display-name display_name
                        Metric display name
  -s display_short_name, --display-name-short display_short_name
                        Metric short display name
  -i description, --description description
                        Metric description
  -g {AVG,MAX,MIN,SUM}, --aggregate {AVG,MAX,MIN,SUM}
                        Metric default aggregate
  -u {percent,number,bytecount,duration}, --unit {percent,number,bytecount,duration}
                        Metric unit
  -r resolution, --resolution resolution
                        Metric default resolution
  -x, --is-disabled     Disable metric
```