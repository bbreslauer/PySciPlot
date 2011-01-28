# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from PyQt4.QtCore import QString
from Wave import Wave

class TraceListEntry():
    def __init__(self, trace):
        self._columns = 2
        self._trace = trace

    def __reduce__(self):
        return tuple([self.__class__, tuple([self._trace])])
    
    def numColumns(self):
        return self._columns
    
    def columnName(self, col):
        if col == 0:
            return "X"
        elif col == 1:
            return "Y"
        return
        
    def columnValue(self, col):
        if col == 0:
            return QString(self._trace.xName())
        elif col == 1:
            return QString(self._trace.yName())
        return

    def getTrace(self):
        return self._trace

