pyflapjackevents
================


==============  ===============  =========
VERSION         DOWNLOADS        TESTS
==============  ===============  =========
|pip version|   |pip downloads|  |travis|
==============  ===============  =========


pyflapjackevents is a small library that serializes `flapjack <http://flapjack.io>`_ events as described in it's own `Data structures <http://flapjack.io/docs/1.0/development/DATA_STRUCTURES/>`_. It's main intention is to allow sending monitor events to flapjack from python programs.


An example:

.. code-block:: python

    server = redis.Redis(host='localhost', port='6380')
    sink = FlapjackEventSink(server, 'events')
    event = FlapjackEvent(
        'test-entity',
        'test-check',
        FlapjackEvent.EVENT_SERVICE,
        FlapjackEvent.STATE_OK,
        summary = 'test-summary',
        details = 'test-details',
    )
    sink.send(event)



This would serialize the event and send it to the appropriate Redis channel for flapjack consumption.

Installation
------------
Just do::

    pip install pyflapjackevents 


or installing it from source::

    git clone https://github.com/tuenti/pyflapjackevents.git
    cd pyflapjackevents
    python setup.py install

Requirements
------------
There're no special requirements for this library.

Credits & Contact
-----------------
pyflapjackevents was created by Tuenti Technologies S.L.. You can follow Tuenti engineering team on Twitter `@tuentieng <https://twitter.com/tuentieng>`_.

License
-------
pyflapjackevents is available under the Apache License, Version 2.0. See LICENSE file for more info.


.. |travis| image:: https://api.travis-ci.org/tuenti/pyflapjackevents.png
  :target: `Travis`_
  :alt: Travis results


.. |pip version| image:: https://pypip.in/v/pyflapjackevents/badge.png
    :target: https://pypi.python.org/pypi/pyflapjackevents
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/pyflapjackevents/badge.png
    :target: https://pypi.python.org/pypi/pyflapjackevents
    :alt: Number of PyPI downloads

.. _Travis: https://travis-ci.org/magmax/inception
