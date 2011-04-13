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

    # Signals
    traceRemovedFromPlot = pyqtSignal(Trace)

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
                'topAxis':          Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'verticalalignment': 'bottom'}),
                                                    'labelFont':            Property.TextOptions({'verticalalignment': 'top'}),
                                                    }),
                'rightAxis':        Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'horizontalalignment': 'left'}),
                                                    'labelFont':            Property.TextOptions({'horizontalalignment': 'left', 'rotation': 'vertical'}),
                                                    }),
                'legend':           Property.Legend(),
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
        self.traceRemovedFromPlot.emit(trace)
        self.refresh()

    def update_bottomAxis(self):
        Util.debug(3, "ScatterPlot.update_bottomAxis", "")

        if self.plot().axes() != None:
            self.update_axis('bottomAxis', self.plot().axes().get_xaxis())

    def update_leftAxis(self):
        Util.debug(3, "ScatterPlot.update_leftAxis", "")

        if self.plot().axes() != None:
            self.update_axis('leftAxis', self.plot().axes().get_yaxis())

    def update_topAxis(self):
        pass

    def update_rightAxis(self):
        pass

    def update_legend(self):
        Util.debug(1, "ScatterPlot.update_legend", "")

        if self.get('legend').get('loc') == 'none' or self.plot() == None or self.plot().axes() == None:
            return
        
        self.plot().axes().legend(**(self.getMpl('legend')))
        self.plot().redraw()



    def update_axisLimits(self, axisName, axisDict):
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

    def update_axisScaling(self, axisName, axisDict):
        # Set linear or logarithmic scaling
        if axisName == 'bottomAxis':
            self.plot().axes().set_xscale(axisDict['scaleType'])
        elif axisName == 'leftAxis':
            self.plot().axes().set_yscale(axisDict['scaleType'])

    def update_axisMajorTicks(self, axisName, axisDict, axis):
        
        minimum, maximum = axis.get_view_interval()

        # Set the formatter and locator for the major ticks
        if axisDict['majorTicksLabelUseWave'] == True:
            wave = self._app.waves().getWaveByName(str(axisDict['majorTicksLabelWave']))
            data = wave.data()
            majorFormatter = ticker.FixedFormatter(data)
        elif axisDict['scaleType'] in ('log', 'symlog'):
            majorFormatter = ticker.LogFormatter(10.0, False)
        else:
            # Just revert to a normal scale with linear formatting
            majorFormatter = ticker.FormatStrFormatter(axisDict['majorTicksLabelNumericFormat'])
        
        axis.set_major_formatter(majorFormatter)

        majorTickPositions = []
        
        if axisDict['useMajorTicksWaveValues']:
            wave = self._app.waves().getWaveByName(str(axisDict['majorTicksWaveValues']))
            majorTickPositions = wave.data()
        elif axisDict['useMajorTicksNumber']:
            if axisDict['useMajorTicksAnchor']:
                # spacing = (max - min) / (num - 1) if both max and min have tick marks
                # spacing = (max - min) / (num)     if exactly one of max and min has tick marks
                # spacing = (max - min) / (num)     if neither max nor min have tick marks

                majorTicksNumber = axisDict['majorTicksNumber']
                anchor = axisDict['majorTicksAnchor']
                if ((float(minimum) - float(anchor)) % ((float(maximum) - float(minimum)) / (majorTicksNumber - 1))) == 0 and ((float(maximum) - float(anchor)) % ((float(maximum) - float(minimum)) / (majorTicksNumber - 1))) == 0:
                    majorTickPositions = list(numpy.linspace(minimum, maximum, majorTicksNumber, True))
                else:
                    spacing = (float(maximum) - float(minimum)) / majorTicksNumber
                    firstTick = anchor + int((float(minimum) - float(anchor)) / float(spacing) - 1) * float(spacing)
                    majorTickPositions = list(numpy.arange(firstTick, maximum, spacing))
                    majorTickPositions.append(majorTickPositions[-1] + spacing)
            else:
                majorTickPositions = list(numpy.linspace(minimum, maximum, axisDict['majorTicksNumber'], True))
        else:
            if axisDict['useMajorTicksAnchor']:
                firstTick = axisDict['majorTicksAnchor'] + int((float(minimum) - float(axisDict['majorTicksAnchor'])) / float(axisDict['majorTicksSpacing']) - 1) * float(axisDict['majorTicksSpacing'])
            else:
                firstTick = minimum
            
            majorTickPositions = list(numpy.arange(firstTick, maximum, axisDict['majorTicksSpacing']))
            majorTickPositions.append(majorTickPositions[-1] + axisDict['majorTicksSpacing'])
            
        # Now place the ticks on the plot
        if axisDict['scaleType'] == 'linear':
            axis.set_major_locator(ticker.FixedLocator(majorTickPositions))
        else:
            axis.set_major_locator(ticker.LogLocator(base=axisDict['majorTicksLogBase']))

                
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
                    'bottom': axisDict['majorTicksVisible'],
                    'top': axisDict['majorTicksVisible'],
                    'labelbottom': axisDict['majorTicksLabelVisible'],
                    'labeltop': False,
                })
        elif axisName == 'leftAxis':
            majorTickParams.update({
                    'left': axisDict['majorTicksVisible'],
                    'right': axisDict['majorTicksVisible'],
                    'labelleft': axisDict['majorTicksLabelVisible'],
                    'labelright': False,
                })
        axis.set_tick_params(which='major', **majorTickParams)

        # Set font for major tick labels
        if axisDict['majorTicksLabelFont'] != {}:
            setp(axis.get_majorticklabels(), **(axisDict['majorTicksLabelFont']))

    def update_axisMinorTicks(self, axisName, axisDict, axis):
        # Set the formatter and locator for the minor ticks
        if axisDict['scaleType'] == 'linear':
            axis.set_minor_formatter(ticker.NullFormatter())
            sortedMajorTickLocs = axis.get_majorticklocs()
            sortedMajorTickLocs.sort()
            #majorTicksSpacing = float(axis.get_majorticklocs()[1]) - float(axis.get_majorticklocs()[0])
            majorTicksSpacing = float(sortedMajorTickLocs[1]) - float(sortedMajorTickLocs[0])
            minorTicksBase = float(majorTicksSpacing) / float(axisDict['minorTicksNumber'] + 1)
            minorTicks = [float(sortedMajorTickLocs[0])]
            #while minorTicks[-1] <= axis.get_view_interval()[1]:
            while minorTicks[-1] < sortedMajorTickLocs[-1]:
                # this creates the minor tick locations starting at the lowest major tick
                # and increasing to the end of the view interval
                minorTicks.append(float(minorTicks[-1]) + float(minorTicksBase))
            axis.set_minor_locator(ticker.FixedLocator(minorTicks))
        else:
            # this needs to be worked on
            subs = axisDict['minorTicksLogLocations'].split(',')
            subs = map(int, subs)
            axis.set_minor_locator(ticker.LogLocator(base=axisDict['majorTicksLogBase'], subs=subs))

        # Set the minor tick params
        minorTickParams = {
                    'direction': axisDict['minorTicksDirection'],
                    'length': axisDict['minorTicksLength'],
                    'width': axisDict['minorTicksWidth'],
                    'color': axisDict['minorTicksColor'],
                }
        if axisName == 'bottomAxis':
            minorTickParams.update({
                    'bottom': axisDict['minorTicksVisible'],
                    'top': axisDict['minorTicksVisible'],
                })
        elif axisName == 'leftAxis':
            minorTickParams.update({
                    'left': axisDict['minorTicksVisible'],
                    'right': axisDict['minorTicksVisible'],
                })
        axis.set_tick_params(which='minor', **minorTickParams)

    def update_axisTicks(self, axisName, axisDict, axis):
        if axisDict['majorTicksVisible']:
            self.update_axisMajorTicks(axisName, axisDict, axis)
    
            if axisDict['minorTicksVisible']:
                self.update_axisMinorTicks(axisName, axisDict, axis)
            else:
                # minor ticks have been disabled
                axis.set_minor_locator(ticker.NullLocator())
        else:
            # major ticks have been disabled, which implies that the minor ticks have also been disabled
            axis.set_major_locator(ticker.NullLocator())
            axis.set_minor_locator(ticker.NullLocator())

    def update_axis(self, axisName, axis):
        axisDict = self.getMpl(axisName)

        self.update_axisLimits(axisName, axisDict)
        self.update_axisScaling(axisName, axisDict)
        
        self.update_axisTicks(axisName, axisDict, axis)

        # Set axis label
        axis.set_label_text(axisDict['label'], axisDict['labelFont'])

        # Redraw the canvas
        self.plot().redraw()

    def refresh(self):
        for trace in self.traces():
            trace.refresh()
        
        self.update_bottomAxis()
        self.update_leftAxis()
        self.update_legend()

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





