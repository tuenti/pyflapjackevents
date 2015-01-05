#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

#
# Copyright 2014 Tuenti Technologies S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json

import pytest

from pyflapjackevents.event import FlapjackEvent, InvalidFlapjackEvent

def test_correct_values_serialization():


    event = FlapjackEvent(
        'test-entity',
        'test-check',
        FlapjackEvent.EVENT_SERVICE,
        FlapjackEvent.STATE_OK,
        timestamp = '1'*10,
        summary = 'test-summary',
        details = 'test-details',
        tags = ['tag1', 'tag2'],
        perfdata = 'test-perfdata')

    assert json.loads(event.to_json()) == {
        'entity': 'test-entity',
        'check': 'test-check',
        'details': 'test-details',
        'time': 1111111111,
        'type': 'service',
        'state': 'ok',
        'tags': ['tag1', 'tag2'],
        'perfdata': 'test-perfdata',
        'summary': 'test-summary',
    }

def test_invalid_state():
    with pytest.raises(InvalidFlapjackEvent):
        event = FlapjackEvent(
        'test-entity',
        'test-check',
        FlapjackEvent.EVENT_SERVICE,
        'fake-state',
        timestamp = 1111111111,
        summary = 'test-summary',
        details = 'test-details',
        tags = ['tag1', 'tag2'],
        perfdata = 'test-perfdata')


def test_invalid_event():
    with pytest.raises(InvalidFlapjackEvent):
        event = FlapjackEvent(
        'test-entity',
        'test-check',
        'fake-event-type',
        FlapjackEvent.STATE_OK,
        timestamp = 1111111111,
        summary = 'test-summary',
        details = 'test-details',
        tags = ['tag1', 'tag2'],
        perfdata = 'test-perfdata')


def test_invalid_tag():
    with pytest.raises(InvalidFlapjackEvent):
        event = FlapjackEvent(
        'test-entity',
        'test-check',
        'fake-event-type',
        FlapjackEvent.STATE_OK,
        timestamp = 1111111111,
        summary = 'test-summary',
        details = 'test-details',
        tags = 'xxx',
        perfdata = 'test-perfdata')

    with pytest.raises(InvalidFlapjackEvent):
        event = FlapjackEvent(
        'test-entity',
        'test-check',
        'fake-event-type',
        FlapjackEvent.STATE_OK,
        timestamp = 1111111111,
        summary = 'test-summary',
        details = 'test-details',
        tags = None,
        perfdata = 'test-perfdata')
