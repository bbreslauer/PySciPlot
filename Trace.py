from PyQt4.QtCore import QObject, pyqtSignal

class Trace(QObject):
    """An x-y pair of data."""

    # Dictionaries for matplotlib symbol lookups
    pointMarkerSymbols = dict(point='o', pixel=',', circle='o', triangle_down='v')

    # Signals
    xChanged = pyqtSignal()
    yChanged = pyqtSignal()
    propertyChanged = pyqtSignal()
    colorChanged = pyqtSignal()
    pointMarkerChanged = pyqtSignal()
    linestyleChanged = pyqtSignal()

    def __init__(self, x=0, y=0, traceColor='Black', lineStyle='solid', pointMarker='point'):
        QObject.__init__(self)
        self.setX(x)
        self.setY(y)
        self.setColor(traceColor)
        self.setLinestyle(lineStyle)
        self.setPointMarker(pointMarker)
    
    def setX(self, x):
        self._x = x
        self.xChanged.emit()
        
    def setY(self, y):
        self._y = y
        self.yChanged.emit()

    def setColor(self, color):
        self._color = color
        self.colorChanged.emit()
        self.propertyChanged.emit()
        
    def setLinestyle(self, style):
        self._linestyle = style
        self.linestyleChanged.emit()

    def setPointMarker(self, marker):
        self._pointMarker = marker
        self.pointMarkerChanged.emit()
        self.propertyChanged.emit()

    def getX(self):
        return self._x
        
    def getY(self):
        return self._y

    def getXName(self):
        return self._x.name()

    def getYName(self):
        return self._y.name()

    def getColor(self):
        return self._color

    def getLinestyle(self):
        return self._linestyle

    def getPointMarker(self):
        return self._pointMarker

    def getPointMarkerSymbol(self):
        return self.pointMarkerSymbols[self.getPointMarker()]

    def getFormat(self):
        return dict(color=self.getColor(), linestyle=self.getLinestyle(), marker=self.getPointMarkerSymbol())



