from PyQt4.QtCore import QObject, pyqtSignal

from pylab import nan
from matplotlib.axes import Axes
from matplotlib import ticker

import Util
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
    properties = {
                    'plotNum':                  { 'default': 1 },
                    'plotName':                 { 'default': '' },
                    'plotBackgroundColor':      { 'default': '#ffffff' },
                    'plotBottomAxisAutoscale':  { 'default': True },
                    'plotBottomAxisMinimum':    { 'default': -10 },
                    'plotBottomAxisMaximum':    { 'default': 10 },
                    'plotBottomAxisScaleType':  { 'default': 'Linear' },
                    'plotBottomAxisTicks':      { 'default': True },
                    'plotBottomAxisMajorTicks': { 'default': 5 },
                    'plotBottomAxisMinorTicks': { 'default': 3 },
                    'plotLeftAxisAutoscale':    { 'default': True },
                    'plotLeftAxisMinimum':      { 'default': -10 },
                    'plotLeftAxisMaximum':      { 'default': 10 },
                    'plotTopAxisVisible':       { 'default': True },
                    'plotLeftAxisVisible':      { 'default': True },
                    'plotBottomAxisVisible':    { 'default': True },
                    'plotRightAxisVisible':     { 'default': True },
                 }

    def __init__(self, figure, plotNum, plotName=""):
        QObject.__init__(self)

        self.initializeProperties()

        self._figure = None
        self._axes = None
        self._traces = []

        self.set_('figure', figure)
        self.set_('plotNum', plotNum)
        self.set_('plotName', plotName)
        

        self.traceAdded.connect(self.refresh)
        self.traceRemoved.connect(self.refresh)
        self.plotRenamed.connect(self.refresh)
        self.propertyChanged.connect(self.refresh)
    
    def __str__(self):
        return "Num: %s, Name: %s" % (self.get('plotNum'), self.get('plotName'))

    def initializeProperties(self):
        for prop in self.properties.keys():
            vars(self)["_" + prop] = self.properties[prop]['default']

    def get(self, variable):
        return vars(self)["_" + variable]

    def set_(self, variable, value):
        # Only plotName can be blank
        if (value != "" or variable == 'plotName') and value != vars(self)["_" + variable]:
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
        
        # Set minimum and maximum for axes
        if not self.get('plotBottomAxisAutoscale'):
            self._axes.set_xlim(self.get('plotBottomAxisMinimum'), self.get('plotBottomAxisMaximum'))
        if not self.get('plotLeftAxisAutoscale'):
            self._axes.set_ylim(self.get('plotLeftAxisMinimum'), self.get('plotLeftAxisMaximum'))

        # Set axis scaling 
        
        
        # Set ticks
        xaxis = self._axes.get_xaxis()
        if self.get('plotBottomAxisTicks'):
            [minorTicks, majorTicks] = self.getTickValues('bottom')
            xaxis.set_major_locator(ticker.FixedLocator(majorTicks))
            xaxis.set_major_formatter(ticker.ScalarFormatter())
            xaxis.set_minor_locator(ticker.FixedLocator(minorTicks))
            xaxis.set_minor_formatter(ticker.NullFormatter())
        else:
            xaxis.set_major_locator(ticker.NullLocator())
            xaxis.set_minor_locator(ticker.NullLocator())

        if drawBool:
            self._figure._canvas.draw()

        return True

    def removeTrace(self, trace):
        self._traces.remove(trace)
        self.traceRemoved.emit()

    def getTickValues(self, axisName):
        """
        Returns a tuple with two list, the major and minor tick locations.
        """

        if axisName == 'bottom':
            [axisMin, axisMax] = self._axes.get_xlim()
            majorTicksNum = self.get('plotBottomAxisMajorTicks')
            minorTicksNum = self.get('plotBottomAxisMinorTicks')

        majorStepSize = (axisMax - axisMin) / majorTicksNum
        majorTicks = Util.frange(axisMin, axisMax, majorStepSize)

        minorStepSize = majorStepSize / minorTicksNum
        minorTicks = Util.frange(axisMin, axisMax, minorStepSize)

        return [majorTicks, minorTicks]

######
# Working on tick marks right now
######





