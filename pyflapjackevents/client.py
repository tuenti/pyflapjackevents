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

class FlapjackEventSink(object):

    def __init__(self, redis, channel):
        """Initialize the event sink.
        :param redis: Redis client, already initialized to send the events to.
        :type redis: redis.Redis object.
        :param name: Name of the redis channel consumed by flapjack.
        :type name: str.
        """
        self.redis = redis
        self.channel = channel

    def send(self, event):
        """Send event to flapjack.
        :param event: Event to be sent via redis.
        :type event: flapjackevents.event.FlapjackEvent.
        """
        self.redis.lpush(self.channel, event.to_json())
