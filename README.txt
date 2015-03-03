Boundary CLI
============

| Boundary CLI provides command line access to Boundary REST APIs
| Typical usage often looks like this:

``bash     $ metric-list``

Installation
------------

``bash      $ pip install boundary_cli``

Configuration
-------------

The Boundary CLI uses environment variables for configuration
information (user, password, etc) to execute against the Boundary REST
APIs, and optionally this information can be overridden via the command
line

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

+------------------------+----------------------+
| Environment Variable   | Description          |
+========================+======================+
| BOUNDARY\_API\_HOST    | Boundary API host    |
+------------------------+----------------------+
| BOUNDARY\_EMAIL        | Boundary email       |
+------------------------+----------------------+
| BOUNDARY\_API\_TOKEN   | Boundary API token   |
+------------------------+----------------------+

Examples
--------

Usage of the Boundary CLI

metric-create
~~~~~~~~~~~~~

.. code:: bash

    $ metric-create FOO "foo bar" "foo" "it's the foo" sum number
    {
      "result": {
        "success": true
      }
    }

Add a Metric Value
~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ metric-add myhost LOAD_1_MINUTE 30
    {
      "result": {
        "success": true
      }
    }

metric-list
~~~~~~~~~~~

.. code:: bash

    $ metric-list
    {
      "result": [{
        {
          "id": 6028,
          "name": "LOAD_1_MINUTE",
          "displayName": "CPU Load 1 Minute",
          "description": "CPU load for the last minute",
          "drillFromMetricName": null,
          "unit": "number",
          "catalogId": 2110,
          "displayNameShort": "Load 1 Minute",
          "defaultAggregate": "avg",
          "isDisabled": 0,
          "isDeleted": 0,
          "isBuiltin": 0
        },
    ...

Command Reference
-----------------

Metric
~~~~~~

Commands to administer metrics in Boundary

metric-add
^^^^^^^^^^

Creates a new measurement value in Boundary

\`\ ``bash usage: metric-add source metric measure``

metric-delete
^^^^^^^^^^^^^

Creates/updates a Boundary Premium metric definition

.. code:: bash

    usage: metric-create <name> <display-name> <display-name_short> <description> <aggregate> <unit> <defaultResolutionMS>
    where:
      name - Name of the metric
      display-name - Name displayed in the Web UI
      display-name-short - Shorter display name
      description - Description of the metric (also used as tooltip)
      aggregate - Type of aggregate (sum, avg, max, or min)
      unit - Type of measurement (percent, number, bytecount, or duration )
      defaultResolutionMS - 

``metric-delete``
^^^^^^^^^^^^^^^^^

.. code:: bash

    usage: metric-delete <name>

``metric-list``
^^^^^^^^^^^^^^^

Lists the metric definitions in your Boundary instance.

.. code:: bash

    usage: metric-list

Plugins
~~~~~~~

plugin-add
^^^^^^^^^^

plugin-delete
^^^^^^^^^^^^^

plugin-get
^^^^^^^^^^

plugin-get-components
^^^^^^^^^^^^^^^^^^^^^

plugin-install
^^^^^^^^^^^^^^

plugin-installed
^^^^^^^^^^^^^^^^

plugin-list
^^^^^^^^^^^

plugin-remove
^^^^^^^^^^^^^

plugin-uninstall\`
^^^^^^^^^^^^^^^^^^

Sources
~~~~~~~

``source-delete``
^^^^^^^^^^^^^^^^^

::

    $ source-delete <source> <metric id>

``source-list``
^^^^^^^^^^^^^^^

Lists all sources in your Boundary instance

::

    $ source-list

User
~~~~

``user-get``
~~~~~~~~~~~~

