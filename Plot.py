from PyQt4.QtCore import QObject, pyqtSignal

from numpy import nan
from matplotlib.axes import Axes
from matplotlib import ticker, colors
from matplotlib.artist import setp
import numpy

import Util
from Waves import Waves
from Wave import Wave
from Trace import Trace

class Plot(QObject):
    """This class contains all the information about a plot inside a figure.
    
    plotNum is 0-based
    """

    # Signals
    plotRenamed = pyqtSignal(str)
    traceAdded = pyqtSignal()
    traceRemoved = pyqtSignal()
    propertyChanged = pyqtSignal()

    # Properties
    properties = {
                    'plotNum':                         { 'type': int, 'default': 0 },
                    'plotName':                        { 'type': str, 'default': '' },
                    'plotNameFont':                    { 'type': dict, 'default': {'size': 18, 'verticalalignment': 'baseline'} },
                    'plotBackgroundColor':             { 'type': str, 'default': '#ffffff' },
                    'plotBottomAxisAutoscale':         { 'type': bool, 'default': True },
                    'plotBottomAxisMinimum':           { 'type': float, 'default': -10 },
                    'plotBottomAxisMaximum':           { 'type': float, 'default': 10 },
                    'plotBottomAxisScaleType':         { 'type': str, 'default': 'Linear' },
                    'plotBottomAxisTicks':             { 'type': bool, 'default': True },
                    'plotBottomAxisLabel':             { 'type': str, 'default': ''},
                    'plotBottomAxisVisible':           { 'type': bool, 'default': True },
                    'plotBottomAxisMajorTicksNumber':  { 'type': int, 'default': 5 },
                    'plotBottomAxisMajorTicksSpacing': { 'type': float, 'default': 2 },
                    'plotBottomAxisMinorTicksNumber':  { 'type': int, 'default': 3 },
                    'plotBottomAxisUseTickSpacing':    { 'type': bool, 'default': False },
                    'plotBottomAxisUseTickNumber':     { 'type': bool, 'default': True },
                    'plotBottomAxisTickLabelFormat':   { 'type': str, 'default': '%.2g'},
                    'plotBottomAxisTickLabelFont':     { 'type': dict, 'default': {'verticalalignment': 'top'} },
                    'plotBottomAxisLabelFont':         { 'type': dict, 'default': {'verticalalignment': 'top'} },
                    'plotLeftAxisAutoscale':           { 'type': bool, 'default': True },
                    'plotLeftAxisMinimum':             { 'type': float, 'default': -10 },
                    'plotLeftAxisMaximum':             { 'type': float, 'default': 10 },
                    'plotLeftAxisScaleType':           { 'type': str, 'default': 'Linear' },
                    'plotLeftAxisTicks':               { 'type': bool, 'default': True },
                    'plotLeftAxisLabel':               { 'type': str, 'default': ''},
                    'plotLeftAxisVisible':             { 'type': bool, 'default': True },
                    'plotLeftAxisMajorTicksNumber':    { 'type': int, 'default': 5 },
                    'plotLeftAxisMajorTicksSpacing':   { 'type': float, 'default': 2 },
                    'plotLeftAxisMinorTicksNumber':    { 'type': int, 'default': 3 },
                    'plotLeftAxisUseTickSpacing':      { 'type': bool, 'default': False },
                    'plotLeftAxisUseTickNumber':       { 'type': bool, 'default': True },
                    'plotLeftAxisTickLabelFormat':     { 'type': str, 'default': '%.2g'},
                    'plotLeftAxisTickLabelFont':       { 'type': dict, 'default': {'horizontalalignment': 'right'} },
                    'plotLeftAxisLabelFont':           { 'type': dict, 'default': {'horizontalalignment': 'right', 'rotation': 'vertical'} },
                 }

    def __init__(self, figure, plotNum, plotName=""):
        QObject.__init__(self)

        Util.debug(2, "Plot.init", "Creating plot")
        
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
        
        Util.debug(1, "Plot.init", "Created plot " + plotName)
    
        self.get('plotBottomAxisUseTickNumber')

    def __str__(self):
        return "Num: %s, Name: %s" % (self.get('plotNum'), self.get('plotName'))

    def initializeProperties(self):
        Util.debug(3, "Plot.initializeProperties", "Initializing properties for plot " + str(self.get('plotName')))
        self.get('plotBottomAxisUseTickNumber')
        for prop in self.properties.keys():
            vars(self)["_" + prop] = self.properties[prop]['default']

    def get(self, variable):
        try:
            Util.debug(3, "Plot.get", "Getting variable " + str(variable) + "=" + str(vars(self)["_" + variable]) + " for plot " + str(self._plotName))
            return vars(self)["_" + variable]
        except AttributeError:
            return self.properties[variable]['default']
        except KeyError:
            pass

    def set_(self, variable, value):
        # Only plotName can be blank
        if (value != "" or variable == 'plotName') and value != vars(self)["_" + variable]:
            if variable in self.properties.keys():
                if self.properties[variable]['type'] == bool:
                    # Need to do specialized bool testing because bool('False') == True
                    if (type(value) == str and value == "True") or (type(value) == bool and value):
                        vars(self)["_" + variable] = True
                    else:
                        vars(self)["_" + variable] = False
                else:
                    vars(self)["_" + variable] = self.properties[variable]['type'](value)
            else:
                vars(self)["_" + variable] = value

            Util.debug(2, "Plot.set", "Setting " + str(variable) + " to " + str(value) + " for plot " + str(self.get('plotName')))

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
        Util.debug(1, "Plot.addTrace", "Added trace " + trace.getXName() + "-" + trace.getYName() + " to plot " + str(self.get('plotName')))
        trace.getX().dataModified.connect(self.refresh)
        trace.getY().dataModified.connect(self.refresh)
        trace.propertyChanged.connect(self.refresh)
        return True
    
    def traces(self):
        return self._traces

    def numTraces(self):
        return len(self._traces)

    def getTraceAsFloat(self, trace):
        Util.debug(2, "Plot.getTraceAsFloat", "Getting trace " + trace.getXName() + "-" + trace.getYName() + " as floats")
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
        Util.debug(2, "Plot.getTracesAsFloat", "Getting traces as floats")
        tmpTraces = []
        for trace in self._traces:
            tmpTraces.append(self.getTraceAsFloat(trace))

        return tmpTraces

    def convertTraceDataToFloat(self, trace):
        Util.debug(2, "Plot.convertTraceDataToFloat", "Converting data")
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
        
        Util.debug(1, "Plot.refresh", "Refreshing plot")

        if not self._figure:
            return False
        
        # Do not refresh the plot if it is not being displayed
        if self.get('plotNum') + 1 > self._figure.numPlots():
            return False 

        #print "building r: " + str(self._figure.get('figureRows')) + ", c: " + str(self._figure.get('figureColumns')) + ", n: " + str(self.get('plotNum'))
        
        if self._figure.get('figureLinkPlotAxes'):
            self._axes = self._figure.grid[self.get('plotNum')]
        else:
            self._axes = self._figure.mplFigure().add_subplot(self._figure.get('figureRows'), self._figure.get('figureColumns'), self.get('plotNum') + 1)

        self._axes.clear()

        Util.debug(2, "Plot.refresh", "Setting plot properties")
        self._axes.set_title(self.get('plotName'), **(self.get('plotNameFont')))
        self._axes.set_axis_bgcolor(str(self.get('plotBackgroundColor')))
#        self._axes.set_axis_bgcolor(colors.colorConverter.to_rgba('#FF0000', .1))

        Util.debug(2, "Plot.refresh", "Setting traces")
        # Plotting data
        for trace in self._traces:
            [x, y] = self.convertTraceDataToFloat(trace)
            self._axes.plot(x, y, **(trace.getFormat()))
        
        # Set minimum and maximum for axes
        Util.debug(2, "Plot.refresh", "Setting axes properties")
        if not self.get('plotBottomAxisAutoscale'):
            self._axes.set_xlim(self.get('plotBottomAxisMinimum'), self.get('plotBottomAxisMaximum'))
        if not self.get('plotLeftAxisAutoscale'):
            self._axes.set_ylim(self.get('plotLeftAxisMinimum'), self.get('plotLeftAxisMaximum'))

        # Set axis scaling 
        
        
        # Set ticks
        Util.debug(2, "Plot.refresh", "Setting ticks")

        for axisName in ['Bottom', 'Left']:
            axis = None
            if axisName == 'Bottom':
                axis = self._axes.get_xaxis()
            elif axisName == 'Left':
                axis = self._axes.get_yaxis()

            if self.get('plot' + axisName + 'AxisTicks'):
    
                # Set major ticks
                axis.set_major_formatter(ticker.FormatStrFormatter(self.get('plot' + axisName + 'AxisTickLabelFormat')))
                
                if self.get('plot' + axisName + 'AxisUseTickNumber'):
                    Util.debug(3, "Plot.refresh" + str(self), axisName + " axis using set number of ticks")
                    # User has defined how many major tick marks to display
                    majorTicksNum = self.get('plot' + axisName + 'AxisMajorTicksNumber')
                    axis.set_major_locator(ticker.LinearLocator(majorTicksNum))
                    
                    # The minor ticks option defines how many ticks between each pair of major ticks
                    # Therefore, we need to calculate how many total minor ticks there will be
                    # There are majorTicksNum-1 sections between the major ticks, and we need to add 1 because of the endpoints
                    minorTicksNum = (self.get('plot' + axisName + 'AxisMinorTicksNumber') + 1) * (len(axis.get_major_ticks()) - 1) + 1
                    axis.set_minor_locator(ticker.LinearLocator(minorTicksNum))
                    axis.set_minor_formatter(ticker.NullFormatter())
                else:
                    Util.debug(3, "Plot.refresh", axisName + " axis using spacing for ticks")
                    # User has defined the spacing between major tick marks
                    majorTicks = list(numpy.arange(self.get('plot' + axisName + 'AxisMinimum'), self.get('plot' + axisName + 'AxisMaximum'), self.get('plot' + axisName + 'AxisMajorTicksSpacing')))
                    if (self.get('plot' + axisName + 'AxisMaximum') - majorTicks[-1]) % self.get('plot' + axisName + 'AxisMajorTicksSpacing') == 0:
                        majorTicks.append(self.get('plot' + axisName + 'AxisMaximum'))
                    axis.set_major_locator(ticker.FixedLocator(majorTicks))
                    
                    # We need to calculate the minor tick values
                    minorTicksSpacing = float(self.get('plot' + axisName + 'AxisMajorTicksSpacing')) / float((self.get('plot' + axisName + 'AxisMinorTicksNumber') + 1))
                    minorTicks = list(numpy.arange(self.get('plot' + axisName + 'AxisMinimum'), self.get('plot' + axisName + 'AxisMaximum'), minorTicksSpacing))
                    axis.set_minor_locator(ticker.FixedLocator(minorTicks))
                    axis.set_minor_formatter(ticker.NullFormatter())
            else:
                axis.set_major_locator(ticker.NullLocator())
                axis.set_minor_locator(ticker.NullLocator())

            # Set font for tick labels
            if self.get('plot' + axisName + 'AxisTickLabelFont') != {}:
                setp(axis.get_majorticklabels(), **(self.get('plot' + axisName + 'AxisTickLabelFont')))

            # Set labels
            axis.set_label_text(self.get('plot' + axisName + 'AxisLabel'), self.get('plot' + axisName + 'AxisLabelFont'))

        if drawBool:
            Util.debug(2, "Plot.refresh", "Drawing plot")
            self._figure._canvas.draw()

        Util.debug(1, "Plot.refresh", "Refreshed plot")
        return True

    def removeTrace(self, trace):
        Util.debug(1, "Plot.removeTrace", "Removing trace " + trace.getXName() + "-" + trace.getYName())
        self._traces.remove(trace)
        self.traceRemoved.emit()

######
# Working on tick marks right now
######





