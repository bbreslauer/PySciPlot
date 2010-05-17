from PyQt4.QtCore import QString
from Wave import Wave

class TraceListEntry():
    def __init__(self, plotNum, trace):
        self._columns = 3
        self._trace = trace
        if not type(plotNum) is int or plotNum < 1:
            plotNum = 1
        self._plotNum = plotNum
    
    def numColumns(self):
        return self._columns
    
    def columnName(self, col):
        if col == 0:
            return "Plot Number"
        elif col == 1:
            return "X"
        elif col == 2:
            return "Y"
        return
        
    def columnValue(self, col):
        if col == 0:
            return self._plotNum
        elif col == 1:
            return QString(self._trace.getXName())
        elif col == 2:
            return QString(self._trace.getYName())
        return

    def getTrace(self):
        return self._trace

    def getPlotNum(self):
        return self._plotNum

