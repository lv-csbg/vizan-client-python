vizan-client-python
===================

.. contents:: **Table of Contents**
    :backlinks: none

Installation
------------

vizan-client-python is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 2.7/3.5+ and PyPy.

.. code-block:: bash

    $ pip install vizan-client-python

Local Web server
________________

For local server you need to install docker and perform post-installation steps on Linux
Then you need to download the image.

.. code-block:: bash

    $ docker pull lvcsbg/tools:vizan-webserver

And run Local server

.. code-block:: python

    from vizan_client import LocalServer
    local_server = LocalServer()

Usage
-------------

With Local Server running no need to provide url, so :

.. code-block:: python

    from vizan_client import visualise
    model_filename = 'data/iML1515.json'
    svg_filename = 'data/E_coli_source.svg'
    output_filename = 'FBA_result.svg'
    visualise(model_filename, svg_filename, output_filename, analysis_type='FBA')

Development
-----------

To install the development version from Github:

.. code-block:: bash

    git clone https://github.com/lv-csbg/vizan-client-python.git
    cd vizan-client-python
    pip install .

License
-------

vizan-client-python is distributed under the terms of `GPL v3 License <https://choosealicense.com/licenses/gpl-3.0/>`_

docker_server module is also distributed under the terms of `MIT License <https://choosealicense.com/licenses/mit/>`_
