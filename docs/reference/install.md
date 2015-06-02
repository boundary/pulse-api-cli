The `boundary` package can installed in the python global installation by the following:

   ```bash
     $ sudo pip install boundary
   ```
It is recommended that you use the python [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) package to create an alternative python installation and then install the boundary package into this alternate python environment.

   ```bash
     lerma:~ davidg$ virtualenv ~/python # Create a new python environment
     New python executable in /Users/davidg/python/bin/python
     Installing setuptools, pip...done.
     $ . ~/python/bin/activate # enable the new python environment
     $ pip install boundary # Install boundary package
   ```

