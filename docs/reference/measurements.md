Commands to insert and extract measurements from a                                  Boundary account.


## measurement-create

**API Documentation**


**Usage**


```
usage: measurement-create [-h] [-l {debug,info,warning,error,critical}]
                          [-a api_host] [-e e_mail] [-t api_token] -n
                          metric_name -m measurement [-s source]
                          [-d timestamp]

Adds a measurement value to a Boundary account

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

## measurement-get

** API Documentation **

[http://premium-documentation.boundary.com/v1/get/measurements/:metric](http://premium-documentation.boundary.com/v1/get/measurements/:metric)

** Usage **




