from PyQt4.QtCore import QString
from Wave import Wave

class PlotListEntry():
    def __init__(self, x, y, plotNum):
        self.columns = 3
        self.x = x
        self.y = y
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
            return QString(self.x.name())
        elif col == 2:
            return QString(self.y.name())
        return

    def getPlotNum(self):
        return self.plotNum
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y



