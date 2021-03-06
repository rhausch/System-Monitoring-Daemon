# Sensors Module
#	Load appropriate sensor sub module to monitor system with
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


# Load appropriate sensor code

has_psutil = False
try:
	import psutil
	has_psutil = True
except:
	None

sensors = []

if has_psutil:
	from psutil_sensors import *
	sensors.append(cpu.cpu_monitor())
	sensors.append(memory.mem_monitor())
