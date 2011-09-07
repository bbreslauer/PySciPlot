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


from PySide.QtGui import QColor

from numpy import nan
from matplotlib.axes import Axes
from matplotlib import ticker
from matplotlib.artist import setp
from matplotlib.font_manager import FontProperties
import numpy

from pygraphene import plot as pgp
from pygraphene import font as pgfont
from pygraphene import ticker as pgticker

import Util, Property
from Waves import Waves
from Wave import Wave
from WavePair import *
from FigureObject import *

class CartesianPlot(FigureObject):
    """
    A generic Cartesian plot, to be used for scatter, bar, and other types.
    Basically any type that plots two series against one another.
    """
    
    # Signals
    wavePairRemovedFromPlot = Signal(WavePair)

    def __init__(self, plot, moreProperties={}):
        Util.debug(2, "CartesianPlot.init", "Creating Cartesian Plot")

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

        properties.update(moreProperties)

        FigureObject.__init__(self, properties)

        self._plot = plot
        self._wavePairs = []

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.plot()]), tuple([self.properties, self._wavePairs])])

    def __setstate__(self, state):
        properties = state[0]
        wavePairs = state[1]
        
        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

        for wavePair in wavePairs:
            self.addWavePair(wavePair)

    def plot(self):
        return self._plot

    def wavePairs(self):
        return self._wavePairs

    def addWavePair(self, wp):
        wp.setPlot(self.plot())
        self._wavePairs.append(wp)

    def removeWavePair(self, wp):
        self._wavePairs.remove(wp)
        wp.removeFromPlot()
        #self.wavePairRemovedFromPlot.emit(wp)
        #self.plot().refresh()

    def makePgPlot(self, pgFigure, pgCanvas):
        """
        Create a PyGraphene CartesianPlot with the given figure and canvas.
        """
        return pgp.CartesianPlot(pgFigure, pgCanvas)

    def update_bottomAxis(self):
        Util.debug(3, "ScatterPlot.update_bottomAxis", "")

        if self.plot().pgPlot() != None:
            self.update_axis('bottomAxis')
            #self.update_axis('bottomAxis', self.plot().axes().get_xaxis())

    def update_leftAxis(self):
        Util.debug(3, "ScatterPlot.update_leftAxis", "")

        if self.plot().pgPlot() != None:
            self.update_axis('leftAxis')
#            self.update_axis('leftAxis', self.plot().axes().get_yaxis())

    def update_topAxis(self):
        pass

    def update_rightAxis(self):
        pass

    def update_legend(self):
        Util.debug(1, "ScatterPlot.update_legend", "")
#
#        if self.get('legend').get('loc') == 'none' or self.plot() == None or self.plot().axes() == None:
#            return
#        
#        # We need to apply the font dict to the Text instances themselves, since
#        # Legend only accepts a FontProperties object
#        legendOptions = self.getMpl('legend')
#        font = legendOptions['font']
#        titleFont = legendOptions['titleFont']
#        del legendOptions['font']
#        del legendOptions['titleFont']
#
#        self.plot().axes().legend(**legendOptions)
#
#        setp(self.plot().axes().get_legend().get_texts(), **font)
#        setp(self.plot().axes().get_legend().get_title(), **titleFont)
#
#        self.plot().redraw()

    def update_axisScaling(self, axis, axisDict):
        # TODO NOT IMPLEMENTED IN PYGRAPHENE
        pass
#        # Set linear or logarithmic scaling
#        if axisName == 'bottomAxis':
#            self.plot().axes().set_xscale(axisDict['scaleType'])
#        elif axisName == 'leftAxis':
#            self.plot().axes().set_yscale(axisDict['scaleType'])

#    def update_axisMajorTicks(self, axisName, axisDict, axis):
#        
#        minimum, maximum = axis.get_view_interval()
#
#        # Set the formatter and locator for the major ticks
#        if axisDict['majorTicksLabelUseWave'] == True:
#            wave = self._app.waves().wave(str(axisDict['majorTicksLabelWave']))
#            data = wave.data()
#            majorFormatter = ticker.FixedFormatter(data)
#        elif axisDict['scaleType'] in ('log', 'symlog'):
#            majorFormatter = ticker.LogFormatter(10.0, False)
#        else:
#            # Just revert to a normal scale with linear formatting
#            majorFormatter = ticker.FormatStrFormatter(axisDict['majorTicksLabelNumericFormat'])
#        
#        axis.set_major_formatter(majorFormatter)
#
#        majorTickPositions = []
#        
#        if axisDict['useMajorTicksWaveValues']:
#            wave = self._app.waves().wave(str(axisDict['majorTicksWaveValues']))
#            data = Util.uniqueList(wave.data())
#            data.sort()
#            majorTickPositions = data
#        elif axisDict['useMajorTicksNumber']:
#            majorTicksNumber = axisDict['majorTicksNumber']
#
#            if axisDict['useMajorTicksAnchor']:
#                anchor = axisDict['majorTicksAnchor']
#                spacing = (float(maximum) - float(minimum)) / (majorTicksNumber - 1)
#
#                # firstTick is the closest would-be tick to the smallest tick which is off the visible axis
#                # lastTick  is the closest would-be tick to the largest  tick which is off the visible axis
#                firstTick = float(minimum) - float(spacing) + ((float(anchor) - float(minimum)) % float(spacing))
#                lastTick  = float(maximum) + float(spacing) - ((float(maximum) - float(anchor)) % float(spacing))
#                
#                if (float(minimum) - float(anchor)) % float(spacing) == 0 or \
#                   (float(maximum) - float(anchor)) % float(spacing) == 0:
#                    # The anchor is located at the min or max of the viewing window (or a spacing multiple thereof)
#                    # and so the number of major ticks visible will be equal to majorTicksNumber, since firstTick
#                    # and lastTick are not within the viewing window
#                    majorTickPositions = Util.subdivideList([firstTick, lastTick], majorTicksNumber)
#                else:
#                    # FIXME
#                    # This produces 1 less than the user's desired number of ticks. However, if we do not subtract 1,
#                    # then the spacing gets screwed up and the anchor no longer has a tick mark. See issue #37.
#                    majorTickPositions = Util.subdivideList([firstTick, lastTick], majorTicksNumber-1)
#            else:
#                # no anchor
#                # We need to account for the two endpoints, which is why we subtract 2 from the majorTicksNumber
#                majorTickPositions = Util.subdivideList([minimum, maximum], majorTicksNumber-2)
#        else:
#            # Using spacing
#            if axisDict['useMajorTicksAnchor']:
#                firstTick = axisDict['majorTicksAnchor'] + int((float(minimum) - float(axisDict['majorTicksAnchor'])) / float(axisDict['majorTicksSpacing']) - 1) * float(axisDict['majorTicksSpacing'])
#            else:
#                firstTick = minimum
#            
#            majorTickPositions = list(numpy.arange(firstTick, maximum, axisDict['majorTicksSpacing']))
#            majorTickPositions.append(majorTickPositions[-1] + axisDict['majorTicksSpacing'])
#            
#        # Now place the ticks on the plot
#        if axisDict['scaleType'] == 'linear':
#            axis.set_major_locator(ticker.FixedLocator(majorTickPositions))
#        else:
#            subs = axisDict['majorTicksLogLocations'].split(',')
#            subs = map(int, subs)
#            axis.set_major_locator(ticker.LogLocator(base=axisDict['majorTicksLogBase'], subs=subs))
#
#                
#        # Set the major tick params
#        majorTickParams = {
#                    'direction': axisDict['majorTicksDirection'],
#                    'length': axisDict['majorTicksLength'],
#                    'width': axisDict['majorTicksWidth'],
#                    'color': axisDict['majorTicksColor'],
#                    'pad': axisDict['majorTicksLabelPadding'],
#                }
#        if axisName == 'bottomAxis':
#            majorTickParams.update({
#                    'bottom': axisDict['majorTicksVisible'],
#                    'top': axisDict['majorTicksVisible'],
#                    'labelbottom': axisDict['majorTicksLabelVisible'],
#                    'labeltop': False,
#                })
#        elif axisName == 'leftAxis':
#            majorTickParams.update({
#                    'left': axisDict['majorTicksVisible'],
#                    'right': axisDict['majorTicksVisible'],
#                    'labelleft': axisDict['majorTicksLabelVisible'],
#                    'labelright': False,
#                })
#        axis.set_tick_params(which='major', **majorTickParams)
#
#        # Set font for major tick labels
#        if axisDict['majorTicksLabelFont'] != {}:
#            setp(axis.get_majorticklabels(), **(axisDict['majorTicksLabelFont']))

#    def update_axisMinorTicks(self, axisName, axisDict, axis):
#        # Set the formatter and locator for the minor ticks
#        if axisDict['scaleType'] == 'linear':
#            axis.set_minor_formatter(ticker.NullFormatter())
#            sortedMajorTickLocs = axis.get_majorticklocs()
#            sortedMajorTickLocs.sort()
#            minorTicks = Util.subdivideList(sortedMajorTickLocs, float(axisDict['minorTicksNumber']))
#            axis.set_minor_locator(ticker.FixedLocator(minorTicks))
#        else:
#            # this needs to be worked on
#            subs = axisDict['minorTicksLogLocations'].split(',')
#            subs = map(int, subs)
#            axis.set_minor_locator(ticker.LogLocator(base=axisDict['majorTicksLogBase'], subs=subs))
#
#        # Set the minor tick params
#        minorTickParams = {
#                    'direction': axisDict['minorTicksDirection'],
#                    'length': axisDict['minorTicksLength'],
#                    'width': axisDict['minorTicksWidth'],
#                    'color': axisDict['minorTicksColor'],
#                }
#        if axisName == 'bottomAxis':
#            minorTickParams.update({
#                    'bottom': axisDict['minorTicksVisible'],
#                    'top': axisDict['minorTicksVisible'],
#                })
#        elif axisName == 'leftAxis':
#            minorTickParams.update({
#                    'left': axisDict['minorTicksVisible'],
#                    'right': axisDict['minorTicksVisible'],
#                })
#        axis.set_tick_params(which='minor', **minorTickParams)

    def update_axisLimits(self, axis, axisDict):
        # Set minimum and maximum for axes
        if axisDict['autoscale']:
            axis.autoscale()
        else:
            axis.setDataRange(axisDict['minimum'], axisDict['maximum'])

    def update_axisMajorTicks(self, axis, axisDict):
        ticks = axis.ticks('major')

        # Set the tick locations
        if axisDict['majorTicksVisible']:
            ticks.setVisible(True)
            
            if axisDict['useMajorTicksNumber']:
                axis.setTicksLocator('major', pgticker.LinearLocator(axisDict['majorTicksNumber']), applyToSlaves=True)
            elif axisDict['useMajorTicksWaveValues']:
                wave = self._app.waves().wave(str(axisDict['majorTicksWaveValues']))
                data = Util.uniqueList(wave.data())
                data.sort()
                axis.setTicksLocator('major', pgticker.FixedLocator(data), applyToSlaves=True)
            elif axisDict['useMajorTicksSpacing']:
                anchor = None
                if axisDict['useMajorTicksAnchor']:
                    anchor = axisDict['majorTicksAnchor']
                axis.setTicksLocator('major', pgticker.SpacedLocator(axisDict['majorTicksSpacing'], anchor), applyToSlaves=True)

        # Ticks are not visible
        else:
            ticks.setVisible(False)

        # Set the tick labels
        if axisDict['majorTicksLabelVisible']:
            if axisDict['majorTicksLabelUseNumeric']:
                axis.setTicksLabeler('major', pgticker.FormatLabeler(axisDict['majorTicksLabelNumericFormat']), applyToSlaves=True)
            elif axisDict['majorTicksLabelUseWave']:
                wave = self._app.waves().wave(str(axisDict['majorTicksLabelWave']))
                data = wave.data()
                axis.setTicksLabeler('major', pgticker.StringLabeler(data), applyToSlaves=True)
        
        # Tick labels are not visible
        else:
            axis.setTicksLabeler('major', pgticker.NullLabeler(), applyToSlaves=True)

    def update_axisMinorTicks(self, axis, axisDict):
        pass

    #def update_axisTicks(self, axisName, axisDict, axis):
    def update_axisTicks(self, axis, axisDict):
        self.update_axisMajorTicks(axis, axisDict)
        self.update_axisMinorTicks(axis, axisDict)
#        if axisDict['majorTicksVisible']:
#            self.update_axisMajorTicks(axis, axisDict)
#    
#            if axisDict['minorTicksVisible']:
#                self.update_axisMinorTicks(axis, axisDict)
#            else:
#                # minor ticks have been disabled
#                axis.set_minor_locator(ticker.NullLocator())
#        else:
#            # major ticks have been disabled, which implies that the minor ticks have also been disabled
#            axis.set_major_locator(ticker.NullLocator())
#            axis.set_minor_locator(ticker.NullLocator())

    def update_axisLabel(self, axis, axisDict):
        axis.setLabelText(axisDict['label'])
        axis.setLabelFont(pgfont.Font(**axisDict['labelFont']))

    def update_axis(self, axisName):
        if axisName == 'bottomAxis':
            axis = self.plot().pgPlot().axis('bottom')
        elif axisName == 'leftAxis':
            axis = self.plot().pgPlot().axis('left')
        else:
            print "Unknown axis: " + str(axisName)
            return
        axisDict = self.getPg(axisName)

        self.update_axisLimits(axis, axisDict)
        self.update_axisScaling(axis, axisDict)

        #self.update_axisTicks(axisName, axisDict, axis)
        self.update_axisTicks(axis, axisDict)

        # Set axis label
        self.update_axisLabel(axis, axisDict)
        #axis.set_label_text(axisDict['label'], axisDict['labelFont'])

        # Redraw the canvas
        self.plot().redraw()

    def refresh(self):
        for wavePair in self.wavePairs():
            wavePair.refresh()

        self.update_bottomAxis()
        self.update_leftAxis()
        self.update_legend()

class ScatterPlot(CartesianPlot):
    
    def __init__(self, plot, moreProperties={}):
        Util.debug(2, "ScatterPlot.init", "Creating Scatter Plot")

        CartesianPlot.__init__(self, plot, moreProperties)

class BarPlot(CartesianPlot):

    def __init__(self, plot, moreProperties={}):
        Util.debug(2, "BarPlot.init", "Creating Bar Plot")

        properties = {
                'orientation': Property.String('vertical'),
                }

        properties.update(moreProperties)

        CartesianPlot.__init__(self, plot, properties)

class PieChart(FigureObject):

    def __init__(self, plot, moreProperties={}):
        Util.debug(2, "PieChart.init", "Creating Pie Chart")

        # Add additional properties without deleting the ones defined in Plot()
        properties = {
                }

        FigureObject.__init__(self, properties, moreProperties)

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
            'Bar Chart':    BarPlot,
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
        self._pgPlot = None
        self._figure = None

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

    def addFigure(self, figure):
        self._figure = figure

    def figure(self):
        return self._figure

    def initPgPlot(self):
        self._pgPlot = self.plotTypeObject.makePgPlot(self.figure().pgFigure(), self.figure().pgFigure().canvas())

    def pgPlot(self):
        """
        Return the PyGraphene plot.
        """
        return self._pgPlot

    def update_name(self):
        Util.debug(3, "Plot.update_name", "")
        self.pgPlot().setTitle(self.getPg('name'), pgfont.Font(**self.getPg('nameFont')))
        self.pgPlot().title().draw()

    def update_nameFont(self):
        Util.debug(3, "Plot.update_nameFont", "")
        self.pgPlot().setTitle(font=pgfont.Font(**self.getPg('nameFont')))
        self.pgPlot().title().draw()

    def update_backgroundColor(self):
        Util.debug(3, "Plot.update_backgroundColor", "")
        self.pgPlot().setColor(self.getPg('backgroundColor'))
        self.redraw()

    def refresh(self):
        self.redraw()

    def redraw(self):
        try:
            self.pgPlot().draw()
        except:
            pass

