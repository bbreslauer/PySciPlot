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

