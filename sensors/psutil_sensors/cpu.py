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
		self.cpu_usage = psutil.cpu_percent(0.1, percpu=True)
		self.cpu_times = psutil.cpu_times()

	def getFormatedData(self):
		data = '{"name": "Usage", "values": ['+','.join('{"value": %.1f}'%x for x in self.cpu_usage)+']}'
		data += ',{"name": "Times", "values": [{"name": "user", "value": %.2f},{"name": "system", "value": %.2f},{"name": "idle", "value": %.2f},{"name":"nice", "value": %.2f},{"name": "iowait", "value": %.2f},{"name": "irq", "value": %.2f},{"name": "softirq", "value": %.2f}]}' % (self.cpu_times.user, self.cpu_times.system, self.cpu_times.idle, self.cpu_times.nice, self.cpu_times.iowait, self.cpu_times.irq, self.cpu_times.softirq)
		message = '{"type": "Cpu", "value": %.1f, "data": [%s]}' % ( sum(self.cpu_usage)/self.num_cpus, data )
		return message

