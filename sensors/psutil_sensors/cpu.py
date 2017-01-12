#!/usr/bin/python
#
# CPU sensor ontop of psutil
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

class cpu_monitor:
	def __init__(self):
		self.num_cpus = len(psutil.cpu_percent(0,percpu=True))

	def update(self):
		self.cpu = []
		cpu_usage = psutil.cpu_percent(0.1, percpu=True)
		cpu_times = psutil.cpu_times(True)
		for i in range(0,len(cpu_usage)):
			self.cpu.append( {'percent': cpu_usage[i], 'user': cpu_times[i].user,
					'nice': cpu_times[i].nice, 'system': cpu_times[i].system,
					'idle': cpu_times[i].idle, 'iowait': cpu_times[i].iowait,
					'irq': cpu_times[i].irq, 'softirq': cpu_times[i].softirq})

	def getFormatedData(self):
		return {'cpu': self.cpu}

