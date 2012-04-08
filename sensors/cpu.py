#!/usr/bin/python

import psutil

class cpu_monitor:
	def __init__(self):
		self.num_cpus = len(psutil.cpu_percent(0,percpu=True))

	def update(self):
		self.cpu_usage = psutil.cpu_percent(0.1, percpu=True)
		self.cpu_times = psutil.cpu_times()

	def getFormatedData(self):
		message = ''
		message += 'Cpu usage: '
		message += ', '.join('%.1f'%x for x in self.cpu_usage)
		message += ' CPU times: '
		message += ', '.join('%.3f'%x for x in self.cpu_times)
		return message

