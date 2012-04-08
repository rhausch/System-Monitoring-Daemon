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
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# System-Monitoring-Daemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with System-Monitoring-Daemon.  If not, see <http://www.gnu.org/licenses/>.
##

from socket import *

from sensors.cpu import *
from sensors.memory import *

HOST = ''
PORT = 6000
ADDR = (HOST, PORT)
BUFSIZE = 4096
MAX_QUEUE = 5


class Stats:
	def __init__(self):
		self.sensors = []
		self.sensors.append(cpu_monitor())
		self.sensors.append(mem_monitor())

	def getStats(self):
		message = ''
		for s in self.sensors:
			s.update()
			message += '{'+s.getFormatedData()+'}'
		return message
		

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


serv_sock.bind((ADDR)) #tuple with one param
serv_sock.listen(MAX_QUEUE)


while 1:
	try:
		(conn_sock,addr) = serv_sock.accept()
	except KeyboardInterrupt:
		print "exiting..."
		break;
	except:
		conn_sock = 0
	if conn_sock:
		#fork
		#conn_sock.send('{ cpu_load: %d}' % (stats.cpu_load))
		client = ClientHandler(stats)
		client.handle(conn_sock)


serv_sock.close()

