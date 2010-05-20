from PyQt4.QtCore import QObject, pyqtSignal

from pylab import nan

from Waves import Waves
from Wave import Wave
from Trace import Trace

class Plot(QObject):
    """This class contains all the information about a plot inside a figure."""

    # Signals
    plotRenamed = pyqtSignal(str)
    traceAdded = pyqtSignal()
    traceRemoved = pyqtSignal()

    def __init__(self, figure, plotNum, name=""):
        QObject.__init__(self)
        self._figure = figure
        self._plotNum = plotNum
        self._name = ""
        self.setName(name)
        self._traces = []

        self.traceAdded.connect(self.refresh)
        self.traceRemoved.connect(self.refresh)
    
    def __str__(self):
        return "Num: %s, Name: %s" % (self._plotNum, self._name)

    def getName(self):
        return self._name

    def getPlotNum(self):
        return self._plotNum

    def addTrace(self, trace):
        self._traces.append(trace)
        self.traceAdded.emit()
        trace.propertyChanged.connect(self.refresh)
        return True
    
    def getTraces(self):
        return self._traces

    def numTraces(self):
        return len(self._traces)

    def getTraceAsFloat(self, trace):
        xData = Wave.convertToFloatList(trace.getX())
        yData = Wave.convertToFloatList(trace.getY())

        # Make sure waves are the same length, or else matplotlib will complain and not plot them
        diffLength = len(xData) - len(yData)
        if diffLength < 0:
            xData.extend([nan] * (- diffLength))
        elif diffLength > 0:
            yData.extend([nan] * diffLength)

        return Trace(xData, yData)

    def getTracesAsFloat(self):
        tmpTraces = []
        for trace in self._traces:
            tmpTraces.append(self.getTraceAsFloat(trace))

        return tmpTraces

    def convertTraceDataToFloat(self, trace):
        xData = Wave.convertToFloatList(trace.getX())
        yData = Wave.convertToFloatList(trace.getY())

        # Make sure waves are the same length, or else matplotlib will complain and not plot them
        diffLength = len(xData) - len(yData)
        if diffLength < 0:
            xData.extend([nan] * (- diffLength))
        elif diffLength > 0:
            yData.extend([nan] * diffLength)

        return [xData, yData]


    def refresh(self):
        print "building r: " + str(self._figure.rows()) + ", c: " + str(self._figure.columns()) + ", n: " + str(self._plotNum)
        self._axes = self._figure.mplFigure().add_subplot(self._figure.rows(), self._figure.columns(), self._plotNum)
        self._axes.clear()

        for trace in self._traces:
            [x, y] = self.convertTraceDataToFloat(trace)
            self._axes.plot(x, y, **(trace.getFormat()))

        self._figure._canvas.draw()

        return True

    def removeTrace(self, trace):
        self._traces.remove(trace)
        self.traceRemoved.emit()

    def setName(self, name):
        if name != "":
            self._name = name
            self.plotRenamed.emit(name)
            return True
        return False



