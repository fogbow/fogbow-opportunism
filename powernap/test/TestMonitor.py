#    powernapd plugin - Monitors process table for presence of process
#
#    Copyright (C) 2011 Canonical Ltd.
#
#    Authors: Dustin Kirkland <kirkland@canonical.com>
#             Andres Rodriguez <andreserl@canonical.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, re, commands, time
import powernapd
from logging import error, debug, info, warn

# Check if the computer is idle
def is_idle():
    return True

class TestMonitor():

    # Initialise
    def __init__(self, config):
        self._type = config['monitor']
        self._name = config['name']
        self._running = config['running']
        self._result = config['result']
        self._absent_seconds = 0
        self._current_state = 0

    def active(self):
        if self._current_state < len(self._result):
            powernapd.RUNNING = self._running[self._current_state]
            result = self._result[self._current_state]
            self._current_state += 1
            return result
        return True

    def start(self):
        pass

