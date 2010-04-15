from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PlotScene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.subplots = []
        self.setSceneRect(QRectF(0, 0, 400, 450))
#        self.setupScene()
    
    def setupScene(self):
        self.setSceneRect(QRectF(0, 0, 400, 400))
        self.addRect(QRectF(0, 0, 400, 400), QPen(), QBrush(QColor(0, 0, 255, 100)))
        self.addRect(QRectF(0, 0, 200, 200))
        self.addText("test")

    def addSubPlot(self, subPlot):
        self.subplots.append(subPlot)
    
    def build(self):
        xMargin = 10
        yMargin = 10
        plotWidth = (self.width() / len(self.subplots)) - xMargin
        plotHeight = self.height() - yMargin
        print "plotWidth: " + str(plotWidth)
        print "plotHeight: " + str(plotHeight)
        
        self.subplots[0].setSceneCoordinates(0, 0, 400, 400)
        
#        currentX = 0
#        currentY = 0
#        for i in range(0, len(self.subplots)):
#            self.addRect(QRectF(currentX, currentY, plotWidth, plotHeight))
#            currentX += plotWidth + xMargin
        
        self.subplots[0].drawBorder(self)
        self.subplots[0].drawAxes(self)
        
        pointPen = QPen()
        pointPen.setWidth(4)

        for i in range(0, len(self.subplots[0].xWave)-1):
            if (self.subplots[0].xWave[i] != '' and self.subplots[0].yWave[i] != '' and self.subplots[0].xWave[i+1] != '' and self.subplots[0].yWave[i+1] != ''):
                thisPoint = self.subplots[0].mapToScene(self.subplots[0].xWave[i], self.subplots[0].yWave[i])
                nextPoint = self.subplots[0].mapToScene(self.subplots[0].xWave[i+1], self.subplots[0].yWave[i+1])
                self.addLine(thisPoint[0], thisPoint[1], thisPoint[0], thisPoint[1], pointPen)
                self.addLine(thisPoint[0], thisPoint[1], nextPoint[0], nextPoint[1])
#                self.addLine(self.subplots[0].xWave[i]*10, self.subplots[0].yWave[i]*10, self.subplots[0].xWave[i+1]*10, self.subplots[0].yWave[i+1]*10)
