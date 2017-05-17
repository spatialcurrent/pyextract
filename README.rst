pyextract
==============

.. image:: https://travis-ci.org/spatialcurrent/pyextract.png
    :target: https://travis-ci.org/spatialcurrent/pyextract

.. image:: https://img.shields.io/pypi/v/pyextract.svg
    :target: https://pypi.python.org/pypi/pyextract

.. image:: https://readthedocs.org/projects/pyextract/badge/?version=master
        :target: http://pyextract.readthedocs.org/en/latest/
        :alt: Master Documentation Status

Description
-----------------

This repo contains a nullsafe-like function for Python that can be used to extract data from dicts, lists, etc.

Installation
-----------------

Install via PyPI_ with:

.. _PyPI: https://pypi.python.org/pypi

.. code-block:: bash

    pip install pyextract

Or install directly from GitHub_ with:

.. _GitHub: https://github.com/

.. code-block:: bash

    pip install git+git://github.com/spatialcurrent/pyextract.git@master

Usage
-----------------

The position args are **keyChain**, **node**, and **fallback**.  If the keyChain is invalid, then the fallback value is returned.  The fallback is only returned if (1) the location described by the keyChan is invalid or (2) the value located is None.  If the value located is a blank string, zero, false, etc., then it will return.  If handling for blank strings, then use the 3rd pattern below to fallback even if the value found is a blank string.

.. code:: python

   from pyextract.extract import extract

   x = { "a": {"b": "c"} }
   y = extract(["a", "b"], x, None)
   # y == c

   x = { "a": {"b": None} }
   y = extract(["a", "b"], x, None)
   # y == None

   x = { "a": {"b": None} }
   y = extract(["a", "b"], x, "") or "c"
   # y == c

Contributing
-----------------

`Spatial Current, Inc.`_ is currently accepting pull requests for this repository.  We'd love to have your contributions!  Please see `Contributing.rst`_ for how to get started.

.. _`Spatial Current, Inc.`: https://spatialcurrent.io
.. _Contributing.rst: https://github.com/spatialcurrent/pyextract/blob/master/CONTRIBUTING.rst

License
-----------------

This work is distributed under the **MIT License**.  See **LICENSE** file.
