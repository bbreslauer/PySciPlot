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
            plot.plot(pair.getX().convertToFloatList(), pair.getY().convertToFloatList(), 'o-')
        return True
        
    def getData(self):
        return self.data
