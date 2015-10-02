## Sources

### source-delete

**API Documentation**

**Usage**

```bash
usage: source-delete [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -s
                     source1[,source2]

Delete sources from a TrueSight Pulse account

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
  -s source1[,source2], --sources source1[,source2]
                        List of sources to delete
```

**Examples**

Remove the source `my-web-server-001` from an account

```bash
$ source-delete -s my-web-server-001
{
  "result": {
    "success": true
  }
}
```

### source-list

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/account/sources/:lastModified?](http://premium-documentation.boundary.com/v1/get/account/sources/:lastModified?)

**Usage**

```bash
usage: source-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                   [-e e_mail] [-t api_token]

Lists the sources in a TrueSight Pulse account

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

Display the sources in an account

```bash
$ source-list
{
  "result": {
    "lastModified": 1433982466486,
    "sources": [
      {
        "name": "my-web-server-001",
        "type": "source",
        "displayName": null,
        "enabled": true,
        "visible": true,
        "removed": false,
        "streams": {
          "TRUESIGHT_PULSE_RANDOM_NUMBER": {
            "enabled": false,
            "removed": false,
            "visible": true
          }
        }
      },
      {
        "name": "my-web-server-002",
        "type": "source",
        "displayName": null,
        "enabled": true,
        "visible": true,
        "removed": false,
        "streams": {
          "TRUESIGHT_PULSE_RANDOM_NUMBER": {
            "enabled": false,
            "removed": false,
            "visible": true
          }
        }
      }
    ]
  }
}
```
