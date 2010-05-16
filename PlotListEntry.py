from PyQt4.QtCore import QString
from Wave import Wave

class PlotListEntry():
    def __init__(self, plotNum, x, y):
        self.columns = 3
        self.xName = x
        self.yName = y
        if not type(plotNum) is int or plotNum < 1:
            plotNum = 1
        self.plotNum = plotNum
    
    def numColumns(self):
        return self.columns
    
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
            return self.plotNum
        elif col == 1:
            return QString(self.xName)
        elif col == 2:
            return QString(self.yName)
        return

