from matplotlib import pyplot

from Waves import Waves
from Wave import Wave
from DataPair import DataPair

class PlotData():
    def __init__(self):
        self.data = []
    
    def addData(self, x, y):
        self.data.append(DataPair(x, y))
        return True
    
    def buildPlot(self, plot):
        for pair in self.data:
            xData = Wave.convertToFloatList(pair.getX())
            yData = Wave.convertToFloatList(pair.getY())

            plot.plot(xData, yData, 'o-')
        return True
        
    def getData(self):
        return self.data
