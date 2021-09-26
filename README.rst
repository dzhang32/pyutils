pyutils
#######

.. image:: https://github.com/dzhang32/pyutils/workflows/test-deploy-package/badge.svg
    :target: https://github.com/dzhang32/pyutils/actions?query=workflow%3Atest-deploy-package
    
.. image:: https://codecov.io/gh/dzhang32/pyutils/branch/main/graph/badge.svg
    :target: https://app.codecov.io/gh/dzhang32/pyutils

|

``pyutils`` is a home for the various utility functions I have found myself using commonly enough to package up.

Installation instructions
-------------------------

Install the development version from GitHub using `pip`

.. code-block:: text

  python3 -m pip install git+https://github.com/dzhang32/pyutils.git


Or, by cloning this repo and running `setup.py`

.. code-block:: text

  git clone https://github.com/dzhang32/pyutils
  cd pyutils
  python3 setup.py install

Development tools
-----------------

The documentation website is automatically updated thanks to `Sphinx <https://www.sphinx-doc.org/>`_ and this `GitHub Action <https://github.com/JamesIves/github-pages-deploy-action>`_. 
