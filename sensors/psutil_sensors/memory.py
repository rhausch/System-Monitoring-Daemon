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
		phys_mem = psutil.phymem_usage()
		self.mem_usage = {'total': phys_mem.total, 'used': phys_mem.used, 
				'free': phys_mem.free, 'percent': phys_mem.percent,
				'buffers': psutil.phymem_buffers(),
				'cached': psutil.cached_phymem()}
		virt_mem = psutil.virtmem_usage()
		self.swap_usage = {'total': virt_mem.total, 'used': virt_mem.used, 'free': virt_mem.free, 'percent': virt_mem.percent}

	def getFormatedData(self):
		return {'memory': self.mem_usage, 'swap': self.swap_usage}


