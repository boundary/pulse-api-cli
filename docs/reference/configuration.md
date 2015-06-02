The Boundary CLI uses environment variables for configuration information (user, password, etc) to execute against the Boundary REST APIs, and optionally this information can be overridden via the command line.

## Environment Variables

| Environment Variable | Description                                    |
|:---------------------|:-----------------------------------------------|
| BOUNDARY\_API\_HOST  | Boundary API host  (e.g. _premium.boundary.com_) |
| BOUNDARY\_EMAIL      | Boundary email     (e.g. _dude@some.company.com_)|
| BOUNDARY\_API\_TOKEN | Boundary API token (e.g. _api.8cb8d721d8-9999_)  |

</br>
Use the following template to add to your Bash shell to set the environment values specific to your account:

```bash
export BOUNDARY_API_HOST="premium.boundary.com"
export BOUNDARY_EMAIL="dude@some.company.com"
export BOUNDARY_API_TOKEN="api.8cb8d721d8-9999"
```



## Common Command Line Arguments

| Argument | Description                                    |
|:---------|:-----------------------------------------------|
|help      | shows the command help and exits               |
|log level | configures output of command execution         |
|api host  | Boundary API host endpont                      |
|e-mail    | E-mail that has access to the Boundary account |


```
   usage: <command name> [-h] [-l {debug,info,warning,error,critical}]
                       [-a api_host] [-e e_mail] [-t api_token] -n metric_name

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

