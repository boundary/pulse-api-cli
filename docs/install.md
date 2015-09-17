## Installing

The TrueSight Pulse CLIs can be installed directly into your systems global installation of python, but it is highly
recommended that you set up a virtual Python installation as described below.

### Global Install
The `boundary` package is installed into the python global installation by using `pip` and running the following command:

```bash
$ sudo pip install boundary
```

### Virtual Python Install

It is highly recommended that you use the python [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
package to create an alternative python installation and then install the boundary package into this alternate
python environment. Python can be an integral part of the operating system and installing the TrueSight Pulse CLI package
in a separate python environment prevents disturbing the global installation by upgrading to newer packages that
may be required by the TrueSight Pulse CLI package.

```bash
# Install python virtual environment in home directory
$ virtualenv ~/python 
New python executable in /Users/davidg/python/bin/python
Installing setuptools, pip...done.

# Activate the new python environment
$ . ~/python/bin/activate 

# Install boundary package
$ pip install boundary
```

