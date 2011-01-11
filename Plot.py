from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import QColor

from numpy import nan
from matplotlib.axes import Axes
from matplotlib import ticker
from matplotlib.artist import setp
import numpy

import Util, Property
from Waves import Waves
from Wave import Wave
from Trace import Trace
from FigureObject import *

class ScatterPlot(FigureObject):
    """
    This class is used for a scatter plot.
    """

    def __init__(self, plot):
        Util.debug(2, "ScatterPlot.init", "Creating Scatter Plot")

        # Add additional properties without deleting the ones defined in Plot()
        properties = {
                'bottomAxis':       Property.GenericAxis({
                                                    'tickLabelFont':      Property.TextOptions({'verticalalignment': 'top'}),
                                                    'labelFont':          Property.TextOptions({'verticalalignment': 'top'}),
                                                    }),
                'leftAxis':         Property.GenericAxis({
                                                    'tickLabelFont':        Property.TextOptions({'horizontalalignment': 'right'}),
                                                    'labelFont':            Property.TextOptions({'horizontalalignment': 'right', 'rotation': 'vertical'}),
                    }),
                }

        FigureObject.__init__(self, properties)

        self._plot = plot
        self._traces = []

    def plot(self):
        return self._plot

    def traces(self):
        return self._traces

    def addTrace(self, trace):
        trace.setPlot(self.plot())
        self._traces.append(trace)
        trace.refresh()

    def removeTrace(self, trace):
        self._traces.remove(trace)
        self.refresh()



    def update_bottomAxis(self):
        Util.debug(3, "ScatterPlot.update_bottomAxis", "")
        self.update_axis('bottomAxis', self.plot().axes().get_xaxis())

    def update_leftAxis(self):
        Util.debug(3, "ScatterPlot.update_leftAxis", "")
        self.update_axis('leftAxis', self.plot().axes().get_yaxis())

    def update_axis(self, axisName, axis):
        print "updating axis"

        axisDict = self.getMpl(axisName)

        # Set minimum and maximum for axes
        if axisDict['autoscale']:
            if axisName == 'bottomAxis':
                self.plot().axes().autoscale(axis='x')
            elif axisName == 'leftAxis':
                self.plot().axes().autoscale(axis='y')
        else:
            if axisName == 'bottomAxis':
                self.plot().axes().set_xlim(axisDict['minimum'], axisDict['maximum'])
            elif axisName == 'leftAxis':
                self.plot().axes().set_ylim(axisDict['minimum'], axisDict['maximum'])
            
        # Should we show any ticks
        if axisDict['ticks']:

            # Set major ticks
            axis.set_major_formatter(ticker.FormatStrFormatter(axisDict['tickLabelFormat']))
            
            if axisDict['useTickNumber']:
                # User has defined the number of major tick marks to display
                majorTicksNum = axisDict['majorTicksNumber']
                axis.set_major_locator(ticker.LinearLocator(majorTicksNum))
                
                # The minor ticks option defines how many ticks between each pair of major ticks
                # Therefore, we need to calculate how many total minor ticks there will be
                # There are majorTicksNum-1 sections between the major ticks, and we need to add 1 because of the endpoints
                minorTicksNum = (axisDict['minorTicksNumber'] + 1) * (len(axis.get_major_ticks()) - 1) + 1
                axis.set_minor_locator(ticker.LinearLocator(minorTicksNum))
                axis.set_minor_formatter(ticker.NullFormatter())
            else:
                # User has defined the spacing between major tick marks
                majorTicks = list(numpy.arange(axisDict['minimum'], axisDict['maximum'], axisDict['majorTicksSpacing']))
                if (axisDict['maximum'] - majorTicks[-1]) % axisDict['majorTicksSpacing'] == 0:
                    majorTicks.append(axisDict['maximum'])
                axis.set_major_locator(ticker.FixedLocator(majorTicks))
                
                # We need to calculate the minor tick values
                minorTicksSpacing = float(axisDict['majorTicksSpacing']) / float((axisDict['minorTicksNumber'] + 1))
                minorTicks = list(numpy.arange(axisDict['minimum'], axisDict['maximum'], minorTicksSpacing))
                axis.set_minor_locator(ticker.FixedLocator(minorTicks))
                axis.set_minor_formatter(ticker.NullFormatter())
        else:
            axis.set_major_locator(ticker.NullLocator())
            axis.set_minor_locator(ticker.NullLocator())

        # Set font for tick labels
        if axisDict['tickLabelFont'] != {}:
            setp(axis.get_majorticklabels(), **(axisDict['tickLabelFont']))

        # Set labels
        axis.set_label_text(axisDict['label'], axisDict['labelFont'])

        # Redraw the canvas
        self.plot().redraw()

    def refresh(self):
        print "refreshing scatterplot"

        self.plot().axes().cla()
        self.update_bottomAxis()
        self.update_leftAxis()

        for trace in self.traces():
            trace.refresh()

class PieChart(FigureObject):

    def __init__(self, plot):
        Util.debug(2, "ScatterPlot.init", "Creating Scatter Plot")

        # Add additional properties without deleting the ones defined in Plot()
        properties = {
                }

        FigureObject.__init__(self, properties)

        self._plot = plot

    def refresh(self):
        print "refreshing piechart"

class Plot(FigureObject):
    """
    This class contains general information about a plot inside a figure.

    Information specific to the type of plot that this is (scatter, pie, etc)
    is stored in Plot.plotTypeObject.
    """

    plotTypeClasses = {
            'Scatter Plot': ScatterPlot,
            'Pie Chart':    PieChart,
            }

    def __init__(self, plotName=""):
        Util.debug(2, "Plot.init", "Creating plot")
       
        # Properties
        properties = {
                'name':             Property.String(''),
                'nameFont':         Property.TextOptions({'size': 18, 'verticalalignment': 'baseline'}),
                'backgroundColor':  Property.Color(QColor(255,255,255,255)),
                'plotType':         Property.String('Scatter Plot'),
                     }

        FigureObject.__init__(self, properties)

        # This is the object that contains all the code specific to the type of plot
        self.plotTypeObject = ScatterPlot(self)

        self.set('name', plotName)

        self.mplHandles = {}

        Util.debug(1, "Plot.init", "Created plot " + plotName)

    def __str__(self):
        return "Name: %s" % (self.get('name'))

    def axes(self):
        """
        These are matplotlib axes, which are used for any kind of plot. They are not specific to one plot type (i.e. scatter).
        """
        return self._axes

    def setAxes(self, axes):
        self._axes = axes
        self.refresh()


    def update_name(self):
        Util.debug(3, "Plot.update_name", "")
        try:
            self.axes().texts.remove(self.mplHandles['name'])
            pass
        except:
            pass

        self.mplHandles['name'] = self.axes().set_title(self.getMpl('name'), **(self.getMpl('nameFont')))
        self.redraw()

    def update_nameFont(self):
        Util.debug(3, "Plot.update_nameFont", "")
        self.update_name()


    def update_backgroundColor(self):
        Util.debug(3, "Plot.update_backgroundColor", "")
        self.axes().set_axis_bgcolor(self.getMpl('backgroundColor'))
        self.redraw()


    def refresh(self):
        print "refreshing plot"

        # Clear the axes
        self.axes().cla()

        # Update the general plot options
        self.update_name()
        self.update_backgroundColor()

        # Check if plot type has changed, and if it has, change the plot type object
        if not isinstance(self.plotTypeObject, self.plotTypeClasses[self.get('plotType')]):
            print "changing plot type"
            self.plotTypeObject = self.plotTypeClasses[self.get('plotType')](self)


        # Refresh the plot type object
        "do update"
        self.plotTypeObject.refresh()

        # Finally, redraw the canvas
        self.redraw()


    def redraw(self):
        self.axes().figure.canvas.draw()





