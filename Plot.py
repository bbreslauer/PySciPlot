from PyQt4.QtGui import QGraphicsScene, QGraphicsView, QWidget
from PyQt4.QtCore import Qt, QRectF
from PlotCanvas import PlotCanvas
from PlotScene import PlotScene
from SubPlot import SubPlot
from Wave import Wave
from Waves import Waves

class Plot():
    def __init__(self, mainWindow=None, viewParent=None):
        self.mainWindow = mainWindow
        self.scene = PlotScene(viewParent)
        self.view = PlotCanvas(viewParent)
        
        self.subplots = []
    
    def getPlotView(self):
        return self.view
    
    def getPlotScene(self):
        return self.scene

    def addSubPlot(self, subplot):
        self.subplots.append(subplot)
        
    def insertSubPlot(self, location, subplot):
        self.subplots.insert(location, subplot)
        
    def buildScene(self):
        for subplot in self.subplots:
            self.scene.addSubPlot(subplot)
        
        self.scene.build()
        
        self.view.setScene(self.scene)
        self.view.show()
        
        
        
        
        
