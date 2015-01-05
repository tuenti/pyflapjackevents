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

class InvalidFlapjackEvent(Exception):
    pass

class FlapjackEvent(object):

    STATE_OK = 'ok'
    STATE_WARNING = 'warning'
    STATE_CRITICAL = 'critical'
    STATE_UNKNOWN = 'unknown'
    STATE_ACK = 'acknowledgement'
    EVENT_SERVICE = 'service'
    EVENT_ACTION = 'action'

    _valid_state = [
        STATE_OK,
        STATE_WARNING,
        STATE_CRITICAL,
        STATE_UNKNOWN,
        STATE_ACK,
    ]

    _valid_type = [
        EVENT_SERVICE,
        EVENT_ACTION,
    ]

    def __init__(self,
                 entity,
                 check,
                 type,
                 state,
                 timestamp = None,
                 summary = '',
                 details = '',
                 tags = None,
                 perfdata = ''):
        """Creates the event.
        :param entity: Name of the relevant entity (e.g. FQDN)
        :type entity: str.
        :param check: The check name ('service descrition' in Nagios terms.)
        :type check: str.
        :param event_type: One of EVENT_SERVICE or EVENT_ACTION.
        :type event_type: str.
        :param state: One of STATE_* (see class def.)
        :type state: str.
        :param timestamp: UNIX timestamp of the event's creation.
        :type timestamp: int.
        :param summary: The check output in the case of a service event,
                        otherwise a message created for an ack or similar.
        :type summary: str.
        :param details: Long check output for a Nagios service event.
        :type details: str.
        :param tags: List of tags pertaining to the event.
        :type tags: List[str]
        :param perfdata: Performance data for a Nagios service event.
        :type perfdata: str.
        """

        self._data = {}

        if type not in self._valid_type:
            raise InvalidFlapjackEvent('TYPE {} is not valid'.format(type))

        if state not in self._valid_state:
            raise InvalidFlapjackEvent('STATE {} is not valid'.format(state))

        if not (isinstance(tags, list) or tags is None):
            raise InvalidFlapjackEvent('Tags is not a list')

        self._data['state'] = state
        self._data['entity'] = entity
        self._data['check'] = check
        self._data['type'] = type
        self._data['time'] = int(timestamp or time())
        self._data['summary'] = summary
        self._data['details'] = details
        self._data['tags'] = tags or []
        self._data['perfdata'] = perfdata

    def to_json(self):
        """Serializes the event.
        :returns: str - the event json serialized.
        """
        return json.dumps(self._data)
