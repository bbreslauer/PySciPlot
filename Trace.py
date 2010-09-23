import Util

from PyQt4.QtCore import QObject, pyqtSignal

class Trace(QObject):
    """An x-y pair of data."""
    
    # Properties
    # Each property has three values, the first is the gui name, the second is the matplotlib name, and the third is whether to use a symbol lookup table
    properties = {
            'traceLineColor':               { 'type': str,   'default': '#000000', 'mplname': 'color',           'symlookup': False },
            'traceLineStyle':               { 'type': str,   'default': 'Solid',   'mplname': 'linestyle',       'symlookup': True  },
            'traceLineWidth':               { 'type': float, 'default': 1.0,       'mplname': 'linewidth',       'symlookup': False },
            'tracePointMarker':             { 'type': str,   'default': 'Point',   'mplname': 'marker',          'symlookup': True  },
            'tracePointMarkerEdgeColor':    { 'type': str,   'default': '#000000', 'mplname': 'markeredgecolor', 'symlookup': False },
            'tracePointMarkerEdgeWidth':    { 'type': float, 'default': 1.0,       'mplname': 'markeredgewidth', 'symlookup': False },
            'tracePointMarkerFaceColor':    { 'type': str,   'default': '#000000', 'mplname': 'markerfacecolor', 'symlookup': False },
            'tracePointMarkerSize':         { 'type': float, 'default': 1.0,       'mplname': 'markersize',      'symlookup': False },
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

    def __init__(self, x=None, y=None):
        QObject.__init__(self)
        Util.debug(2, "Trace.init", "Creating trace")
        self._plot = None
        self.initializeVariables()
        self.initializeProperties()
        self.setX(x)
        self.setY(y)

    def initializeVariables(self):
        Util.debug(3, "Trace.initializeVariables", "Initializing variables")
        self._x = None
        self._y = None
        
    def initializeProperties(self):
        Util.debug(3, "Trace.initializeProperties", "Initializing properties")
        for prop in self.properties.keys():
            vars(self)["_" + prop] = self.properties[prop]['default']

    def get(self, variable, lookupSymbol=False):
        try:
            if lookupSymbol and self.properties[variable]['symlookup']:
                return self.symbols[variable][vars(self)["_" + variable]]
            return vars(self)["_" + variable]
        except AttributeError:
            return self.properties[variable]['default']

    def set_(self, variable, value):
        # Only plotName can be blank
        if value != "" and value != vars(self)["_" + variable]:
            if type(value).__name__ == 'QString':
                value = str(value)
            
            vars(self)["_" + variable] = value

            Util.debug(2, "Trace.set", "Setting " + str(variable) + " to " + str(value) + " for trace")

            self.propertyChanged.emit()

            return True
        return False


    def setPlot(self, plot):
        self._plot = plot
    
    def setX(self, x):
        Util.debug(2, "Trace.setX", "Setting x trace")
        self._x = x
        self.xChanged.emit()
        
    def setY(self, y):
        Util.debug(2, "Trace.setY", "Setting y trace")
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
            formatDict[self.properties[prop]['mplname']] = self.get(prop, True)

        return formatDict

