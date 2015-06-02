## source-delete

```bash
(python)lerma:boundary-api-cli davidg$ source-delete -h
usage: source-delete [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -s
                     source1[,source2]

Delete sources from a Boundary account

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
  -s source1[,source2], --sources source1[,source2]
                        List of sources to delete

```

## source-list

```bash
usage: source-list [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                   [-e e_mail] [-t api_token]

Lists the sources in a Boundary account

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
