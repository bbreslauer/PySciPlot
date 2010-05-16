from PyQt4.QtCore import QObject, pyqtSignal

class Trace(QObject):
    """An x-y pair of data."""

    # Signals
    xChanged = pyqtSignal()
    yChanged = pyqtSignal()
    colorChanged = pyqtSignal()

    def __init__(self, x=0, y=0, traceColor='Black'):
        QObject.__init__(self)
        self.setX(x)
        self.setY(y)
        self.setColor(traceColor)
    
    def setX(self, x):
        self._x = x
        self.xChanged.emit()
        
    def setY(self, y):
        self._y = y
        self.yChanged.emit()

    def setColor(self, color):
        self._color = color
        self.colorChanged.emit()
        
    def getX(self):
        return self._x
        
    def getY(self):
        return self._y

    def getXName(self):
        return self._x.name()

    def getYName(self):
        return self._y.name()

    def getFormat(self):
        return dict(color=self._color, linestyle='solid')



