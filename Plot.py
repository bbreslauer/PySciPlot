from PyQt4.QtCore import QObject, pyqtSignal

from Waves import Waves
from Wave import Wave
from Trace import Trace

class Plot(QObject):
    """This class contains all the information about a plot inside a figure."""

    # Signals
    traceAdded = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        self._traces = []
    
    def addTrace(self, x, y):
        self._traces.append(Trace(x, y))
        self.traceAdded.emit()
        return True
    
    def getTraces(self):
        return self._traces

    def numTraces(self):
        return len(self._traces)

    def getTraceAsFloat(self, traceNum):
        xData = Wave.convertToFloatList(self._traces[traceNum].getX())
        yData = Wave.convertToFloatList(self._traces[traceNum].getY())
        return Trace(xData, yData)

    def getTracesAsFloat(self):
        tmpTraces = []
        for i in range(self.numTraces()):
            tmpTraces.append(self.getTraceAsFloat(i))

        return tmpTraces

    def buildPlot(self, plot):
        for trace in self.getTracesAsFloat():
            plot.plot(trace.getX(), trace.getY())
        return True

