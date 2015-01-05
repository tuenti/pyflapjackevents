# pyflapjackevents


pyflapjackevents is a small library that serializes [Flapjack](flapjack|http://flapjack.io/) events as described in it's own [Data structures](http://flapjack.io/docs/1.0/development/DATA_STRUCTURES/). It's main intention is to allow sending monitor events to flapjack from python programs.


An example:

```
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
```


This would serialize the event and send it to the appropriate Redis channel for flapjack consumption.

## Installation

Just do:

```
pip install pyflapjackevents 
```

or installing it from source:

```
git clone https://github.com/tuenti/pyflapjackevents.git
cd pyflapjackevents
python setup.py install
```
## Requirements

There're no special requirements for this library.

## Credits & Contact

pyflapjackevents was created by Tuenti Technologies S.L.. You can follow Tuenti engineering team on Twitter @tuentieng.

## License
pyflapjackevents is available under the Apache License, Version 2.0. See LICENSE file for more info.
