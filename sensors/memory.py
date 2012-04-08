#!/usr/bin/python

import psutil

class mem_monitor:
	def __init__(self):
		self.mem_usage = ''
		self.virt_mem_usage = ''

	def update(self):
		self.mem_usage = psutil.phymem_usage()
		self.virt_mem_usage = psutil.virtmem_usage()

	def getFormatedData(self):
		message = 'Memory- Phys: %.1f Virt: %.1f' % (self.mem_usage.percent, self.virt_mem_usage.percent)
		return message


