# Events
An event appears as a moment in time on one or more graphs. Events can be color coded with associated text and comment stream. An event stream can be placed on a dashboard in order to view the list of events.

## event-create

### Examples

## event-get

### Examples

## event-list

### Examples

## event-query

### Examples

```
usage: alarm-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token]

List alarm definitions associated with the TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical. Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access the
                        TrueSight Pulse account
```
