# Alarm

Commands to administer definitions of metric alarms in a Boundary account.

## alarm-create

Creates a alarm definition in a Boundary account.

### Usage
```bash
usage: alarm-create [-h] [-l {debug,info,warning,error,critical}]
                    [-a api_host] [-e e_mail] [-t api_token] -n alarm_name
                    [-m metric_name] [-g aggregate] [-o operation] [-v value]
                    -r interval [-i hostgroup_id] [-d note] [-p] [-x]

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
  -n alarm_name, --alarm-name alarm_name
                        Name of the alarm
  -m metric_name, --metric metric_name
                        Name of the metric to alarm
  -g aggregate, --trigger-aggregate aggregate
                        Metric aggregate to alarm upon
  -o operation, --trigger-operation operation
                        Trigger threshold comparison
  -v value, --trigger-threshold value
                        Trigger threshold value
  -r interval, --trigger-interval interval
                        Interval to alarm on, can be one of: "1 second","15
                        seconds","1 minute","5 minutes","1 hour"
  -i hostgroup_id, --host-group-id hostgroup_id
                        Host group the alarm applies to
  -d note, --note note  A description or resolution of the alarm
  -p, --per-host-notify
                        An alarm by default will run the associated actions
                        when any server in the host group violates the
                        threshold, and then at the end when all servers are
                        back within the threshold. If perHostNotify is set to
                        true, the actions will run when ANY server in the
                        group violates and falls back within the threshold.
  -x, --is-disabled     Enable or disable the alarm
```

### Examples

## alarm-delete

```bash
usage: alarm-delete [-h] [-l {debug,info,warning,error,critical}]
                    [-a api_host] [-e e_mail] [-t api_token] -i alarm-id

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
                        API token for given e-mail that has access to the
                        Boundary account
  -i alarm-id, --alarm-id alarm-id
                        Alarm identifier
```


### Examples

## alarm-list

Returns a list of alarm definitions from a Boundary account

#### Usage

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

#### Examples

## alarm-update

### Examples
