httpie-wsse-auth
================

This `HTTPie <http://httpie.org/>`_ auth plugin implements Escher authentication
for Emarsys API requests.

Installation
------------

Be sure that 'HTTPie <http://httpie.org/>`_ is installed, and install this plugin:

.. code-block:: bash

   $ pip install httpie-wsse-auth

After installing, you will see the option ``wsse-auth`` under ``--auth-type`` if you run
``$ http --help``.

Example
-------

.. code-block:: bash

   $ http --auth-type=wsse-auth --auth='access_id:secret_key' https://api.emarsys.net/api/v2/settings

Check out `HTTPie sessions <https://github.com/jkbrzt/httpie#sessions>`_ if you would like to
save authentication information between your requests.