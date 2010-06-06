from PyQt4.QtCore import QObject, pyqtSignal

class Trace(QObject):
    """An x-y pair of data."""
    
    # Properties
    # Each property has three values, the first is the gui name, the second is the matplotlib name, and the third is whether to use a symbol lookup table
    properties = {
                    'traceLineColor':            ['color',              False],
                    'traceLineStyle':            ['linestyle',          True],
                    'traceLineWidth':            ['linewidth',          False],
                    'tracePointMarker':          ['marker',             True],
                    'tracePointMarkerEdgeColor': ['markeredgecolor',    False],
                    'tracePointMarkerEdgeWidth': ['markeredgewidth',    False],
                    'tracePointMarkerFaceColor': ['markerfacecolor',    False],
                 }


    # Dictionaries for matplotlib symbol lookups
    symbols = { 'tracePointMarker': 
                                    {  'None': '',
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
                                    },
                'traceLineStyle':  
                                    {  'None': '',
                                       'Solid': '-',
                                       'Dashed': '--',
                                       'Dash Dot': '-.',
                                       'Dotted': ':'
                                    }
            }
                            

    # Signals
    xChanged = pyqtSignal()
    yChanged = pyqtSignal()
    propertyChanged = pyqtSignal()

    def __init__(self, x=0, y=0):
        QObject.__init__(self)
        self._plot = None
        self.initializeVariables()
        self.initializeProperties()
        self.setX(x)
        self.setY(y)

        self.set_('traceLineColor', 'Black')
        self.set_('traceLineStyle', 'Solid')
        self.set_('traceLineWidth', 1.0)
        self.set_('tracePointMarker', 'None')
        self.set_('tracePointMarkerFaceColor', 'Black')
        self.set_('tracePointMarkerEdgeColor', 'Black')
        self.set_('tracePointMarkerEdgeWidth', 1.0)

    def initializeVariables(self):
        self._x = None
        self._y = None
        
    def initializeProperties(self):
        for prop in self.properties.keys():
            vars(self)["_" + prop] = None

    def get(self, variable, lookupSymbol=False):
        if lookupSymbol and self.properties[variable][1]:
            return self.symbols[variable][vars(self)["_" + variable]]
        return vars(self)["_" + variable]

    def set_(self, variable, value):
        # Only plotName can be blank
        if value != "" and value != vars(self)["_" + variable]:
            vars(self)["_" + variable] = value

            self.propertyChanged.emit()

            return True
        return False


    def setPlot(self, plot):
        self._plot = plot
    
    def setX(self, x):
        self._x = x
        self.xChanged.emit()
        
    def setY(self, y):
        self._y = y
        self.yChanged.emit()

    
    
    def getX(self):
        return self._x
        
    def getY(self):
        return self._y

    def getXName(self):
        return self._x.name()

    def getYName(self):
        return self._y.name()

    def getLinestyleSymbol(self):
        return self.lineStyleSymbols[self.getLinestyle()]

    def getPointMarkerSymbol(self):
        return self.pointMarkerSymbols[self.getPointMarker()]

    def getFormat(self):
        formatDict = dict()

        for prop in self.properties.keys():
            formatDict[self.properties[prop][0]] = str(self.get(prop, True))

        return formatDict

