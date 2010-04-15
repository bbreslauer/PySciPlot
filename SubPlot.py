from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Wave import Wave
from Waves import Waves

class SubPlot:
    def __init__(self, parent=None):
        self.plot = parent
        
        # set defaults
        self.plotXMin = -3
        self.plotXMax =  10
        self.plotYMin = -6
        self.plotYMax =  10
        self.sceneXMin = 0
        self.sceneXMax = 0
        self.sceneYMin = 0
        self.sceneYMax = 0
        
        self.xWave = None
        self.yWave = None
    
    def setPlotXMin(self, xmin):
        self.xMin = xmin
        self.resetPlotSceneTransformation()
        
    def setPlotXMax(self, xmax):
        self.xMax = xmax
        self.resetPlotSceneTransformation()
        
    def setPlotYMin(self, ymin):
        self.yMin = ymin
        self.resetPlotSceneTransformation()
        
    def setPlotYMax(self, ymax):
        self.yMax = ymax
        self.resetPlotSceneTransformation()
        
    def setXWave(self, xwave):
        self.xWave = xwave
    
    def setYWave(self, ywave):
        self.yWave = ywave

    def setSceneCoordinates(self, xmin, ymin, xmax, ymax):
        self.sceneXMin = xmin
        self.sceneXMax = xmax
        self.sceneYMin = ymin
        self.sceneYMax = ymax
        self.resetPlotSceneTransformation()
    
    def setPlotCoordinates(self, xmin, ymin, xmax, ymax):
        self.plotXMin = xmin
        self.plotXMax = xmax
        self.plotYMin = ymin
        self.plotYMax = ymax
        self.resetPlotSceneTransformation()
    
    def resetPlotSceneTransformation(self):
        # find x scaling factor
        self.xScale = (self.sceneXMax - self.sceneXMin) / (self.plotXMax - self.plotXMin)
        
        # find y scaling factor
        # make it negative because the scene counts top to bottom, but we count bottom to top
        self.yScale = -(self.sceneYMax - self.sceneYMin) / (self.plotYMax - self.plotYMin)
        
        # find x zero
        self.xZero = self.sceneXMin - (self.plotXMin * self.xScale)
        
        # find y zero
        self.yZero = self.sceneYMax - (self.plotYMin * self.yScale)
        
    
    # calculating functions    
    def mapToScene(self, x, y):
        return ((self.xZero + x*self.xScale), (self.yZero + y*self.yScale))
        
    def sceneWidth(self):
        return self.sceneXMax - self.sceneXMin
        
    def sceneHeight(self):
        return self.sceneYMax - self.sceneYMin
    
    
    
    
    # drawing functions
    def drawBorder(self, scene):
        scene.addRect(QRectF(self.sceneXMin, self.sceneYMin, self.sceneWidth(), self.sceneHeight()))

    def drawXAxis(self, scene):
        scene.addLine(self.xZero, self.sceneYMin, self.xZero, self.sceneYMax)
        
    def drawYAxis(self, scene):
        scene.addLine(self.sceneXMin, self.yZero, self.sceneXMax, self.yZero)
    
    def drawAxes(self, scene):
        self.drawXAxis(scene)
        self.drawYAxis(scene)
        self.drawXText(scene, "X axis is here")
    
    def drawXText(self, scene, text):
        textItem = scene.addText(text)
        textItem.setPos(150, 400)
    
    
    
    
    
    
