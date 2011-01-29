# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
                                                    'majorTicksLabelFont':  Property.TextOptions({'verticalalignment': 'top'}),
                                                    'labelFont':            Property.TextOptions({'verticalalignment': 'top'}),
                                                    }),
                'leftAxis':         Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'horizontalalignment': 'right'}),
                                                    'labelFont':            Property.TextOptions({'horizontalalignment': 'right', 'rotation': 'vertical'}),
                    }),
                }

        FigureObject.__init__(self, properties)

        self._plot = plot
        self._traces = []

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.plot()]), tuple([self.properties, self._traces])])

    def __setstate__(self, state):
        properties = state[0]
        traces = state[1]
        
        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

        for trace in traces:
            self.addTrace(trace)

    def plot(self):
        return self._plot

    def traces(self):
        return self._traces

    def addTrace(self, trace):
        trace.setPlot(self.plot())
        self._traces.append(trace)
        self.refresh()

    def removeTrace(self, trace):
        self._traces.remove(trace)
        trace.removeFromPlot()
        self.refresh()

    def update_bottomAxis(self):
        Util.debug(3, "ScatterPlot.update_bottomAxis", "")
        try:
            self.update_axis('bottomAxis', self.plot().axes().get_xaxis())
        except:
            pass

    def update_leftAxis(self):
        Util.debug(3, "ScatterPlot.update_leftAxis", "")
        try:
            self.update_axis('leftAxis', self.plot().axes().get_yaxis())
        except:
            pass

    def update_axis(self, axisName, axis):
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
        
        if axisDict['majorTicksVisible']:
            # Set the formatter and locator for the major ticks
            axis.set_major_formatter(ticker.FormatStrFormatter(axisDict['majorTicksLabelFormat']))
            if axisDict['useMajorTicksNumber']:
                # User has defined the number of major tick marks to display
                majorTicksNum = axisDict['majorTicksNumber']
                axis.set_major_locator(ticker.LinearLocator(majorTicksNum))
            else:
                # User has defined the spacing between major tick marks
                majorTicks = list(numpy.arange(axisDict['minimum'], axisDict['maximum'], axisDict['majorTicksSpacing']))
                if (axisDict['maximum'] - majorTicks[-1]) % axisDict['majorTicksSpacing'] == 0:
                    majorTicks.append(axisDict['maximum'])
                axis.set_major_locator(ticker.FixedLocator(majorTicks))
                    
            # Set the major tick params
            majorTickParams = {
                        'direction': axisDict['majorTicksDirection'],
                        'length': axisDict['majorTicksLength'],
                        'width': axisDict['majorTicksWidth'],
                        'color': axisDict['majorTicksColor'],
                        'pad': axisDict['majorTicksLabelPadding'],
                    }
            if axisName == 'bottomAxis':
                majorTickParams.update({
                        'bottom': axisDict['majorTicksDisplayPrimary'],
                        'top': axisDict['majorTicksDisplaySecondary'],
                        'labelbottom': axisDict['majorTicksLabelDisplayPrimary'],
                        'labeltop': axisDict['majorTicksLabelDisplaySecondary'],
                    })
            elif axisName == 'leftAxis':
                majorTickParams.update({
                        'left': axisDict['majorTicksDisplayPrimary'],
                        'right': axisDict['majorTicksDisplaySecondary'],
                        'labelleft': axisDict['majorTicksLabelDisplayPrimary'],
                        'labelright': axisDict['majorTicksLabelDisplaySecondary'],
                    })
            axis.set_tick_params(which='major', **majorTickParams)
    
            if axisDict['minorTicksVisible']:
                # Set the formatter and locator for the minor ticks
                axis.set_minor_formatter(ticker.NullFormatter())
                majorTicksSpacing = float(axis.get_majorticklocs()[1]) - float(axis.get_majorticklocs()[0])
                minorTicksBase = float(majorTicksSpacing) / float(axisDict['minorTicksNumber'] + 1)
                axis.set_minor_locator(ticker.MultipleLocator(minorTicksBase))
        
                # Set the minor tick params
                minorTickParams = {
                            'direction': axisDict['minorTicksDirection'],
                            'length': axisDict['minorTicksLength'],
                            'width': axisDict['minorTicksWidth'],
                            'color': axisDict['minorTicksColor'],
                            'pad': axisDict['minorTicksLabelPadding'],
                        }
                if axisName == 'bottomAxis':
                    minorTickParams.update({
                            'bottom': axisDict['minorTicksDisplayPrimary'],
                            'top': axisDict['minorTicksDisplaySecondary'],
                            'labelbottom': axisDict['minorTicksLabelDisplayPrimary'],
                            'labeltop': axisDict['minorTicksLabelDisplaySecondary'],
                        })
                elif axisName == 'leftAxis':
                    minorTickParams.update({
                            'left': axisDict['minorTicksDisplayPrimary'],
                            'right': axisDict['minorTicksDisplaySecondary'],
                            'labelleft': axisDict['minorTicksLabelDisplayPrimary'],
                            'labelright': axisDict['minorTicksLabelDisplaySecondary'],
                        })
                axis.set_tick_params(which='minor', **minorTickParams)
        
            else:
                # minor ticks have been disabled
                axis.set_minor_locator(ticker.NullLocator())
        else:
            # major ticks have been disabled, which implies that the minor ticks have also been disabled
            axis.set_major_locator(ticker.NullLocator())
            axis.set_minor_locator(ticker.NullLocator())


        # Set font for tick labels
        if axisDict['majorTicksLabelFont'] != {}:
            setp(axis.get_majorticklabels(), **(axisDict['majorTicksLabelFont']))

        # Set labels
        axis.set_label_text(axisDict['label'], axisDict['labelFont'])

        # Redraw the canvas
        self.plot().redraw()

    def refresh(self):
        for trace in self.traces():
            trace.refresh()
        
        self.update_bottomAxis()
        self.update_leftAxis()

class PieChart(FigureObject):

    def __init__(self, plot):
        Util.debug(2, "ScatterPlot.init", "Creating Scatter Plot")

        # Add additional properties without deleting the ones defined in Plot()
        properties = {
                }

        FigureObject.__init__(self, properties)

        self._plot = plot
    
    def __reduce__(self):
        return tuple([self.__class__, tuple([self.plot()]), tuple([self.properties])])

    def __setstate__(self, state):
        properties = state[0]

        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

    def refresh(self):
        pass

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
        self._axes = None

        self.mplHandles = {}

        Util.debug(1, "Plot.init", "Created plot " + plotName)

    def __str__(self):
        return "Name: %s" % (self.get('name'))

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.get('name')]), tuple([self.properties, self.plotTypeObject])])

    def __setstate__(self, state):
        properties = state[0]
        self.plotTypeObject = state[1]
        
        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)
        
        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

        self.refresh()

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
        except:
            pass
        
        try:
            self.mplHandles['name'] = self.axes().set_title(self.getMpl('name'), **(self.getMpl('nameFont')))
            self.redraw()
        except:
            pass

    def update_nameFont(self):
        Util.debug(3, "Plot.update_nameFont", "")
        self.update_name()


    def update_backgroundColor(self):
        Util.debug(3, "Plot.update_backgroundColor", "")
        self.axes().set_axis_bgcolor(self.getMpl('backgroundColor'))

        self.redraw()

    def refresh(self):
        try:
            # Clear the axes
            self.axes().cla()
    
            # Check if plot type has changed, and if it has, change the plot type object
            if not isinstance(self.plotTypeObject, self.plotTypeClasses[self.get('plotType')]):
                self.plotTypeObject = self.plotTypeClasses[self.get('plotType')](self)
    
            # Refresh the plot type object. We do this here first because it clears
            # the axes. If we did this after updating the general plot options,
            # then we would lose the update_name call.
            self.plotTypeObject.refresh()
    
            # Update the general plot options
            self.update_name()
            self.update_backgroundColor()
    
            # Finally, redraw the canvas
            self.redraw()
        except:
            pass


    def redraw(self):
        try:
            self.axes().figure.canvas.draw()
        except:
            pass





