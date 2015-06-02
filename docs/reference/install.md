The `boundary` package can installed in the python global installation by using `pip` and running the following command:

```bash
$ sudo pip install boundary
```
It is highly recommended that you use the python [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) package to create an alternative python installation and then install the boundary package into this alternate python environment. Python can be an integral part of the operating system and installing the Boundary CLI package in a separate python environment prevents disturbing the global installation by upgrading to newer packages that may be required by the Boundary package.

```bash
# Install python virtual environment
$ virtualenv ~/python 
New python executable in /Users/davidg/python/bin/python
Installing setuptools, pip...done.

# Activate the new python environment
$ . ~/python/bin/activate 

#  Install boundary package
$ pip install boundary
```

