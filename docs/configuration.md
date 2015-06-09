The Boundary CLI uses environment variables for authentication information (user, password, etc) and end-point 
to execute against the Boundary REST APIs, and optionally this information can be overridden via the command line.

## Environment Variables

Environment variables are used to provide the credentials and the endpoint to execute the Boundary API against.

| Environment Variable | Description                                    |
|:---------------------|:-----------------------------------------------|
| BOUNDARY\_API\_HOST  | Boundary API host  (e.g. _premium.boundary.com_) |
| BOUNDARY\_EMAIL      | Boundary email     (e.g. _dude@some.company.com_)|
| BOUNDARY\_API\_TOKEN | Boundary API token (e.g. _api.8cb8d721d8-9999_)  |

</br>
Use the following template, and replace with your account values, and add to your Bash shell `.bash_profile` or
`.bashrc` to set the environment values specific to your account:

```bash
export BOUNDARY_API_HOST="premium.boundary.com"
export BOUNDARY_EMAIL="dude@some.company.com"
export BOUNDARY_API_TOKEN="api.8cb8d721d8-9999"
```


## Common Command Line Arguments

Alternatively, you can provide credentials on the command line, as well as configure the logging output,
and get help on a specific command.

| Argument | Description                                    |
|:---------|:-----------------------------------------------|
|help      | shows the command help and exits               |
|log level | configures output of command execution         |
|api host  | Boundary API host endpont                      |
|e-mail    | E-mail that has access to the Boundary account |


```bash
usage: <command-name>[-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token]

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

## Command Specific Command Line Arguments

Some CLI commands may require additional arguments to provide additional data required for an API call.
Command line specific options can be displayed by running the command
with a `-h` or `--help` as shown here for `metric-create`:

```bash
$ metric-create -h
usage: metric-create [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                     -d display_name -s display_short_name [-i description] -g
                     {AVG,MAX,MIN,SUM}
                     [-u {percent,number,bytecount,duration}] [-r resolution]
                     [-x]

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
