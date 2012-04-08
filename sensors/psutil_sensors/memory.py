#!/usr/bin/python
#
# Memory monitor ontop of psutil
#
# Copyright 2012 Dan Ballard and Robert Hausch
#
## License:
#
# This file is part of System-Monitoring-Daemon.
#
# System-Monitoring-Daemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# System-Monitoring-Daemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with System-Monitoring-Daemon.  If not, see <http://www.gnu.org/licenses/>.
##


import psutil

class mem_monitor:
	def __init__(self):
		self.mem_usage = ''
		self.virt_mem_usage = ''

	def update(self):
		self.mem_usage = psutil.phymem_usage()
		self.mem_usage['buffers'] = psutil.phymem_buffers()
		self.mem_usage['cached'] = psutil.cached_phymem()
		self.virt_mem_usage = psutil.virtmem_usage()

	def getFormatedData(self):
		message = '{"type": "Memory", "value": "%.1f", "data": [{"name": "Physical", "value": "%.1f"},{"name": "Virtual", "value": "%.1f"}]}' % (self.mem_usage.percent, self.mem_usage.percent, self.virt_mem_usage.percent)
		return message


