from PyQt4.QtCore import QObject, pyqtSignal

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
    colorChanged = pyqtSignal()
    pointMarkerChanged = pyqtSignal()
    linestyleChanged = pyqtSignal()

    def __init__(self, x=0, y=0, traceColor='Black', lineStyle='Solid', pointMarker='None'):
        QObject.__init__(self)
        self._plot = None
        self.setX(x)
        self.setY(y)
        self.setColor(traceColor)
        self.setLinestyle(lineStyle)
        self.setPointMarker(pointMarker)

    def setPlot(self, plot):
        self._plot = plot
    
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
        self.propertyChanged.emit()

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

    def getLinestyleSymbol(self):
        return self.lineStyleSymbols[self.getLinestyle()]

    def getPointMarker(self):
        return self._pointMarker

    def getPointMarkerSymbol(self):
        return self.pointMarkerSymbols[self.getPointMarker()]

    def getFormat(self):
        return dict(color=self.getColor(), linestyle=self.getLinestyleSymbol(), marker=self.getPointMarkerSymbol())



