httpie-wsse-auth
================

This `HTTPie <https://github.com/jkbr/httpie>`_ auth plugin implements WSSE authentication.

Installation
------------

.. code-block:: bash

   $ pip install httpie-wsse-auth

After installing, you will see the option ``wsse-auth`` under ``--auth-type`` if you run
``$ http --help``.

Example
-------

.. code-block:: bash

   $ http --auth-type=wsse-auth --auth='access_id:secret_key' example.org
