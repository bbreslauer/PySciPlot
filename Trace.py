from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import QColor

class Trace(QObject):
    """An x-y pair of data."""

    # Dictionaries for matplotlib symbol lookups
    pointMarkerSymbols = {  'None': '',
                            'Point': '.',
                            'Pixel': ',',
                            'Circle': 'o',
                            'Triangle - Down': 'v',
                            'Triangle - Up': '^',
                            'Triangle - Left': '<',
                            'Triangle - Right': '>',
                            'Y - Down': '1',
                            'Y - Up': '2',
                            'Y - Left': '3',
                            'Y - Right': '4',
                            'Square': 's',
                            'Pentagon': 'p',
                            'Star': '*',
                            'Hexagon 1': 'h',
                            'Hexagon 2': 'H',
                            'Plus': '+',
                            'X': 'x',
                            'Diamond': 'D',
                            'Thin Diamond': 'd',
                            'Vertical Line': '|',
                            'Horizontal Line': '_',
                         }
    lineStyleSymbols =   {  'None': '',
                            'Solid': '-',
                            'Dashed': '--',
                            'Dash Dot': '-.',
                            'Dotted': ':'
                         }
                            

    # Signals
    xChanged = pyqtSignal()
    yChanged = pyqtSignal()
    propertyChanged = pyqtSignal()

    def __init__(self, x=0, y=0, traceColor='Black',
                                 lineStyle='Solid',
                                 pointMarker='None',
                                 pointMarkerFaceColor='Black',
                                 pointMarkerEdgeColor='Black',
                                 pointMarkerEdgeWidth=1.0
                ):
        QObject.__init__(self)
        self._plot = None
        self.initializeVariables()
        self.setX(x)
        self.setY(y)
        self.setLineColor(traceColor)
        self.setLinestyle(lineStyle)
        self.setPointMarker(pointMarker)
        self.setPointMarkerFaceColor(pointMarkerFaceColor)
        self.setPointMarkerEdgeColor(pointMarkerEdgeColor)
        self.setPointMarkerEdgeWidth(pointMarkerEdgeWidth)

    def initializeVariables(self):
        self._x = None
        self._y = None
        self._lineColor = None
        self._linestyle = None
        self._pointMarker = None
        self._pointMarkerFaceColor = None
        self._pointMarkerEdgeColor = None
        self._pointMarkerEdgeWidth = None
        
        


    def setPlot(self, plot):
        self._plot = plot
    
    def setX(self, x):
        self._x = x
        self.xChanged.emit()
        
    def setY(self, y):
        self._y = y
        self.yChanged.emit()

    def setLineColor(self, color):
        if self._lineColor != color:
            self._lineColor = color
            self.propertyChanged.emit()
            return True
        return False
        
    def setLinestyle(self, style):
        if self._linestyle != style:
            self._linestyle = style
            self.propertyChanged.emit()
            return True
        return False

    def setPointMarker(self, marker):
        if self._pointMarker != marker:
            self._pointMarker = marker
            self.propertyChanged.emit()
            return True
        return False

    def setPointMarkerFaceColor(self, color):
        if self._pointMarkerFaceColor != color:
            self._pointMarkerFaceColor = color
            self.propertyChanged.emit()
            return True
        return False

    def setPointMarkerEdgeColor(self, color):
        if self._pointMarkerEdgeColor != color:
            self._pointMarkerEdgeColor = color
            self.propertyChanged.emit()
            return True
        return False

    def setPointMarkerEdgeWidth(self, width):
        if self._pointMarkerEdgeWidth != width:
            self._pointMarkerEdgeWidth = width
            self.propertyChanged.emit()
            return True
        return False

    
    
    def getX(self):
        return self._x
        
    def getY(self):
        return self._y

    def getXName(self):
        return self._x.name()

    def getYName(self):
        return self._y.name()

    def getLineColor(self):
        return self._lineColor

    def getLinestyle(self):
        return self._linestyle

    def getLinestyleSymbol(self):
        return self.lineStyleSymbols[self.getLinestyle()]

    def getPointMarker(self):
        return self._pointMarker

    def getPointMarkerSymbol(self):
        return self.pointMarkerSymbols[self.getPointMarker()]

    def getPointMarkerFaceColor(self):
        return self._pointMarkerFaceColor

    def getPointMarkerEdgeColor(self):
        return self._pointMarkerEdgeColor

    def getPointMarkerEdgeWidth(self):
        return self._pointMarkerEdgeWidth

    def getFormat(self):
        return dict(color=self.getLineColor(),
                    linestyle=self.getLinestyleSymbol(),
                    marker=self.getPointMarkerSymbol(),
                    markerfacecolor=self.getPointMarkerFaceColor(),
                    markeredgecolor=self.getPointMarkerEdgeColor(),
                    markeredgewidth=self.getPointMarkerEdgeWidth()
               )



