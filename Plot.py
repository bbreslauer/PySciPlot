from PyQt4.QtCore import QObject, pyqtSignal

from pylab import nan

from Waves import Waves
from Wave import Wave
from Trace import Trace

class Plot(QObject):
    """This class contains all the information about a plot inside a figure."""

    # Signals
    traceAdded = pyqtSignal()

    def __init__(self, figure, plotNum):
        QObject.__init__(self)
        self._figure = figure
        self._plotNum = plotNum
        self._traces = []

        self.traceAdded.connect(self.refresh)
    
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

        # Make sure waves are the same length, or else matplotlib will complain and not plot them
        diffLength = len(xData) - len(yData)
        if diffLength < 0:
            xData.extend([nan] * diffLength)
        elif diffLength > 0:
            yData.extend([nan] * diffLength)

        return Trace(xData, yData)

    def getTracesAsFloat(self):
        tmpTraces = []
        for i in range(self.numTraces()):
            tmpTraces.append(self.getTraceAsFloat(i))

        return tmpTraces

    def refresh(self):
        print "building r: " + str(self._figure.rows()) + ", c: " + str(self._figure.columns()) + ", n: " + str(self._plotNum)
        self._axes = self._figure.mplFigure().add_subplot(self._figure.rows(), self._figure.columns(), self._plotNum)
        self._axes.clear()

        for trace in self.getTracesAsFloat():
            self._axes.plot(trace.getX(), trace.getY())

        self._figure._canvas.draw()

        return True

