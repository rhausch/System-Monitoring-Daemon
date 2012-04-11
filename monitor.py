#!/usr/bin/python
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

import threading
from socket import *
import time
import json

#from sensors.cpu import *
#from sensors.memory import *
import sensors

HOST = ''
PORT = 6000
ADDR = (HOST, PORT)
BUFSIZE = 4096
MAX_QUEUE = 5


class Stats():
	def __init__(self):
		self.read_lock = threading.Lock()
		self.write_lock = threading.Lock()

		self.sensors = sensors.sensors #[]
		#self.sensors.append(cpu_monitor())
		#self.sensors.append(mem_monitor())
		
		self.stop = threading.Event()
		t = threading.Thread(target=self.update_loop, args=())
		t.start()

	def update_loop(self):
		while not self.stop.isSet():
			self.acquire_write()
			for s in self.sensors:
				s.update()
			self.release_write()
			time.sleep(0.1)

	def getStats(self):
		data = {}
		self.acquire_read()
		for s in self.sensors:
			data.update(s.getFormatedData())
		self.release_read()
		return json.dumps(data)
		
	def acquire_read(self):
		self.read_lock.acquire()
		self.write_lock.acquire()

	def release_read(self):
		self.write_lock.release()
		self.read_lock.release()

	def acquire_write(self):
		self.write_lock.acquire()

	def release_write(self):
		self.write_lock.release()
		
	

class ClientHandler:
	def __init__(self, stats):
		self.stats = stats

	def handle(self, sock):	
		conn_sock.send( self.stats.getStats() )
		conn_sock.close()


stats = Stats()

	
serv_sock = socket(AF_INET, SOCK_STREAM)
# Behave better after crash
serv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


try:
	serv_sock.bind((ADDR)) #tuple with one param
	serv_sock.listen(MAX_QUEUE)
except Exception as err: 
	print "Error: ", type(err), ': ', err
	stats.stop.set()
	exit(0)


while 1:
	try:
		(conn_sock,addr) = serv_sock.accept()
	except KeyboardInterrupt:
		print "\nExiting..."
		break;
	except:
		conn_sock = 0
	if conn_sock:
		#fork
		#conn_sock.send('{ cpu_load: %d}' % (stats.cpu_load))
		client = ClientHandler(stats)
		client.handle(conn_sock)

stats.stop.set()
serv_sock.close()

