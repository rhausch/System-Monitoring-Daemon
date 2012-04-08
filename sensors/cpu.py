#!/usr/bin/python

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
		message = '{"type": "Cpu", "value": "%.1f", "data": [%s]}' % ( sum(self.cpu_usage)/self.num_cpus, data )
		return message

