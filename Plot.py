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
                    'plotNum':                         { 'default': 1 },
                    'plotName':                        { 'default': '' },
                    'plotBackgroundColor':             { 'default': '#ffffff' },
                    'plotBottomAxisAutoscale':         { 'default': True },
                    'plotBottomAxisMinimum':           { 'default': -10 },
                    'plotBottomAxisMaximum':           { 'default': 10 },
                    'plotBottomAxisScaleType':         { 'default': 'Linear' },
                    'plotBottomAxisTicks':             { 'default': True },
                    'plotBottomAxisMajorTicksNumber':  { 'default': 5 },
                    'plotBottomAxisMajorTicksSpacing': { 'default': 2 },
                    'plotBottomAxisMinorTicksNumber':  { 'default': 3 },
                    'plotBottomAxisUseTickSpacing':    { 'default': False },
                    'plotBottomAxisUseTickNumber':     { 'default': True },
                    'plotLeftAxisAutoscale':           { 'default': True },
                    'plotLeftAxisMinimum':             { 'default': -10 },
                    'plotLeftAxisMaximum':             { 'default': 10 },
                    'plotTopAxisVisible':              { 'default': True },
                    'plotLeftAxisVisible':             { 'default': True },
                    'plotBottomAxisVisible':           { 'default': True },
                    'plotRightAxisVisible':            { 'default': True },
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

            # Set major ticks
            xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
            
            if self.get('plotBottomAxisUseTickNumber'):
                # User has defined how many major tick marks to display
                majorTicksNum = self.get('plotBottomAxisMajorTicksNumber')
                xaxis.set_major_locator(ticker.LinearLocator(majorTicksNum))
                
                # The minor ticks option defines how many ticks between each pair of major ticks
                # Therefore, we need to calculate how many total minor ticks there will be
                # There are majorTicksNum-1 sections between the major ticks, and we need to add 1 because of the endpoints
                minorTicksNum = (self.get('plotBottomAxisMinorTicksNumber') + 1) * (len(xaxis.get_major_ticks()) - 1) + 1
                xaxis.set_minor_locator(ticker.LinearLocator(minorTicksNum))
                xaxis.set_minor_formatter(ticker.NullFormatter())
            else:
                # User has defined the spacing between major tick marks
                xaxis.set_major_locator(ticker.MultipleLocator(self.get('plotBottomAxisMajorTicksSpacing')))
                
                # We need to set the minor ticks by spacing instead of number because they will be offset if (axis_max - axis_min) / major_tick_num is not an integer
                minorTicksSpacing = float(self.get('plotBottomAxisMajorTicksSpacing')) / float((self.get('plotBottomAxisMinorTicksNumber') + 1))
                xaxis.set_minor_locator(ticker.MultipleLocator(minorTicksSpacing))
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

######
# Working on tick marks right now
######





