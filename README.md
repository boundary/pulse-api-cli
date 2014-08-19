Boundary API Shell
==================

Shell scripts for using the Boundary APIs.

Prerequisites
-------------

### Required At Runtime

1. Bash Shell, version 3.2.X or later
2. [Curl](http://curl.haxx.se/), a command line tool for transferring data with URL syntax
3. [jq JSON processor](http://stedolan.github.io/jq/) a lightweight and flexible command-line JSON processor

### Required For Installation Only
1. [wget](https://www.gnu.org/software/wget/),package for retrieving files using HTTP, HTTPS and FTP. (required for installtion only)
2. [unzip](required for  installation only),


Installation
------------

### Install Bash Shell
Most Linux/Unix environments already have the Bash Shell installed and configured as the default shell.

For Windows install [Win-Bash](http://win-bash.sourceforge.net) or other Bash Shell distribution for Windows

### Install Jq
Download the binaries for [jq](http://stedolan.github.io/jq/) from [here](http://stedolan.github.io/jq/download/) for you specific platform.

### Install Boundary API Shell
1. Download the distribution

    ```bash
    $ curl https://github.com/jdgwartney/boundary-api-shell/archive/RE-00.01.00.zip
    ```
2. Change directory to directory where the distribution was downloaded:

    ```bash
    $ cd distribution_directory
    ```
    
3. Extract the distribution

    ```bash
    $ unzip RE-00.01.00.zip
    ```
    
Configuration
-------------
The Boundary API Shell uses environment variable for configuration information (user, password, etc) for executing curl commands that use the Boundary REST APIs.

### Environment Variables
| Environment Variable                    | Description                    |
| ----------------------------------------|:------------------------------:|
| <code>BOUNDARY_API_HOST</code>          | Boundary Enterprise API Host   |
| <code>BOUNDARY_API_KEY</code>           | Boundary Enterprise API key    |
| <code>BOUNDARY_PREMIUM_API_HOST</code>  | Boundary Premium API Host      |
| <code>BOUNDARY_PREMIUM_EMAIL</code>     | Boundary Premimum user id/email|
| <code>BOUNDARY_PREMIUM_API_TOKEN</code> | Boundary Premimum API token    |
| <code>BOUNDARY_ORG_ID</code>            | Boundary Organization ID       |

Using
-----
1. Change directory to the unpacked distribution
2. Source `env.sh`:

    ```bash
    $ source env.sh
    ```

The commands have now been added to your `PATH`

Examples
--------
Usage of the Boundary API Shell

### Create a Metric


### Send a Metric Value

### List Meters

### Tag a Meter

Command Reference
-----------------


### Event

#### Create

#### List

#### Query

### Meter

#### Create

#### List

#### Tag

### Metric

#### Add

#### Create

#### Delete







