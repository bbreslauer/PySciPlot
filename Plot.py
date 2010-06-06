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
    propertyChanged = pyqtSignal()

    # Properties
    properties = [
                    'plotNum',
                    'plotName',
                    'plotBackgroundColor',
                 ]

    def __init__(self, figure, plotNum, plotName=""):
        QObject.__init__(self)

        self.initializeProperties()

        self.set_('figure', figure)
        self.set_('plotNum', plotNum)
        self.set_('plotName', plotName)
        self.set_('plotBackgroundColor', '#ffffff')
        
        self._traces = []

        self.traceAdded.connect(self.refresh)
        self.traceRemoved.connect(self.refresh)
        self.plotRenamed.connect(self.refresh)
        self.propertyChanged.connect(self.refresh)
    
    def __str__(self):
        return "Num: %s, Name: %s" % (self.get('plotNum'), self.get('plotName'))

    def initializeProperties(self):
        for prop in self.properties:
            vars(self)["_" + prop] = None

    def get(self, variable):
        return vars(self)["_" + variable]

    def set_(self, variable, value):
        # Only plotName can be blank
        if value != "" or variable == 'plotName':
            vars(self)["_" + variable] = value

            # See if we should emit any signals
            if variable == 'plotName':
                self.plotRenamed.emit(value)
            else:
                self.propertyChanged.emit()

            return True
        return False
    
    def addTrace(self, trace):
        self._traces.append(trace)
        #trace.addPlot(self)
        self.traceAdded.emit()
        trace.getX().dataModified.connect(self.refresh)
        trace.getY().dataModified.connect(self.refresh)
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


    def refresh(self, drawBool=True):
        print "building r: " + str(self._figure.get('figureRows')) + ", c: " + str(self._figure.get('figureColumns')) + ", n: " + str(self.get('plotNum'))
        self._axes = self._figure.mplFigure().add_subplot(self._figure.get('figureRows'), self._figure.get('figureColumns'), self.get('plotNum'))
        self._axes.clear()

        self._axes.set_title(self.get('plotName'))
        self._axes.set_axis_bgcolor(str(self.get('plotBackgroundColor')))

        for trace in self._traces:
            [x, y] = self.convertTraceDataToFloat(trace)
            self._axes.plot(x, y, **(trace.getFormat()))

        if drawBool:
            self._figure._canvas.draw()

        return True

    def removeTrace(self, trace):
        self._traces.remove(trace)
        self.traceRemoved.emit()



