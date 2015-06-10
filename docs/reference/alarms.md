## Alarms
Commands to administer definitions of metric alarms in a Boundary account.

### alarm-create

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/alarms](http://premium-documentation.boundary.com/v1/post/alarms)

**Usage**

```bash
usage: alarm-create [-h] [-l {debug,info,warning,error,critical}]
                    [-a api_host] [-e e_mail] [-t api_token] -n alarm_name -m
                    metric_name -g {SUM,AVG,MAX,MIN} -o {eq,gt,lt} -v value -r
                    {1 second,15 seconds,1 minute,5 minutes,1 hour,1.5 hours,3
                    hours,6 hours,12 hours} [-u hostgroup_id] [-d note]
                    [-c action-id] [-p] [-x]

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
  -n alarm_name, --alarm-name alarm_name
                        Name of the alarm
  -m metric_name, --metric metric_name
                        Name of the metric to alarm
  -g {SUM,AVG,MAX,MIN}, --trigger-aggregate {SUM,AVG,MAX,MIN}
                        Metric aggregate to alarm upon
  -o {eq,gt,lt}, --trigger-operation {eq,gt,lt}
                        Trigger threshold comparison
  -v value, --trigger-threshold value
                        Trigger threshold value
  -r {1 second,15 seconds,1 minute,5 minutes,1 hour,1.5 hours,3 hours,6 hours,12 hours}, --trigger-interval {1 second,15 seconds,1 minute,5 minutes,1 hour,1.5 hours,3 hours,6 hours,12 hours}
                        Interval to alarm upon
  -u hostgroup_id, --host-group-id hostgroup_id
                        Host group the alarm applies to
  -d note, --note note  A description or resolution of the alarm
  -c action-id, --action action-id
                        An action to be performed when an alarm is triggered
  -p, --per-host-notify
                        An alarm by default will run the associated actions
                        when any server in the host group violates the
                        threshold, and then at the end when all servers are
                        back within the threshold. If perHostNotify is set to
                        true, the actions will run when ANY server in the
                        group violates and falls back within the threshold.
  -x, --is-disabled     Enable or disable the alarm
```

**Examples**

Create an alarm when the maximum value of `BOUNDARY_METRIC_TEST` is greater than a 100 in a 5 minute
period.

```bash
$ alarm-create -n "my-alarm" -m BOUNDARY_METRIC_TEST -g max -o gt -v 100 -r "5 minutes"
{
  "result": {
    "id": 45040,
    "name": "my-alarm",
    "triggerPredicate": {
      "agg": "max",
      "op": "gt",
      "val": "100"
    },
    "metricName": "BOUNDARY_METRIC_TEST",
    "interval": 900,
    "perHostNotify": false,
    "actions": []
  }
}
```

### alarm-delete

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/alarm/:alarmId](http://premium-documentation.boundary.com/v1/delete/alarm/:alarmId)

**Usage**

```bash
usage: alarm-delete [-h] [-l {debug,info,warning,error,critical}]
                    [-a api_host] [-e e_mail] [-t api_token] -i alarm-id

Deletes an alarm definition from a Boundary account

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
  -i alarm-id, --alarm-id alarm-id
                        Alarm identifier
```

**Examples**

Delete an alarm definition with id of 45041

```bash
$ alarm-delete -i 45041
```

### alarm-list

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/alarms](http://premium-documentation.boundary.com/v1/get/alarms)

**Usage**

```bash
usage: alarm-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token]

List alarm definitions associated with the Boundary account

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

List the defined alarms

```bash
$ alarm-list
{
  "result": [
    {
      "id": 16329,
      "name": "CPU usage is high",
      "triggerPredicate": {
        "agg": "avg",
        "op": "gt",
        "val": 0.8
      },
      "metricName": "CPU",
      "interval": 60,
      "hostgroupId": null,
      "note": "auto generated",
      "perHostNotify": false,
      "actions": [
        {
          "id": 2491,
          "name": "Email davidg5"
        }
      ]
    },
    {
      "id": 16335,
      "name": "Disk Writes are high",
      "triggerPredicate": {
        "agg": "sum",
        "op": "gt",
        "val": 209715200
      },
      "metricName": "DISKWB",
      "interval": 60,
      "hostgroupId": null,
      "note": "auto generated",
      "perHostNotify": false,
      "actions": [
        {
          "id": 2491,
          "name": "Email davidg5"
        }
      ]
    },
```


### alarm-update

**API Documentation**


**Usage**