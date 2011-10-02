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
                'bottom':       Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'verticalalignment': 'top'}),
                                                    'labelFont':            Property.TextOptions({'verticalalignment': 'top'}),
                                                    }),
                'left':         Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'horizontalalignment': 'right'}),
                                                    'labelFont':            Property.TextOptions({'horizontalalignment': 'right', 'rotation': 'vertical'}),
                                                    }),
                'top':          Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'verticalalignment': 'bottom'}),
                                                    'labelFont':            Property.TextOptions({'verticalalignment': 'bottom'}),
                                                    'slaveAxisToOther':     Property.Boolean(True),
                                                    'slavedTo':             Property.String('bottom'),
                                                    }),
                'right':        Property.GenericAxis({
                                                    'majorTicksLabelFont':  Property.TextOptions({'horizontalalignment': 'left'}),
                                                    'labelFont':            Property.TextOptions({'horizontalalignment': 'left', 'rotation': 'vertical'}),
                                                    'slaveAxisToOther':     Property.Boolean(True),
                                                    'slavedTo':             Property.String('left'),
                                                    }),
                'legend':           Property.Legend(),
                }

        properties.update(moreProperties)

        FigureObject.__init__(self, properties)

        self._plot = plot
        self._wavePairs = []

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.plot(), self.properties]), tuple([self._wavePairs])])

    def __setstate__(self, state):
        wavePairs = state[0]

        for wavePair in wavePairs:
            self.addWavePair(wavePair)

    def plot(self):
        return self._plot

    def wavePairs(self):
        return self._wavePairs

    def addWavePair(self, wp):
        wp.setPlot(self.plot())
        self._wavePairs.append(wp)
        wp.refresh()

    def removeWavePair(self, wp):
        self._wavePairs.remove(wp)
        wp.removeFromPlot()

    def makePgPlot(self, pgFigure, pgCanvas):
        """
        Create a PyGraphene CartesianPlot with the given figure and canvas.
        """
        return pgp.CartesianPlot(pgFigure, pgCanvas)

    def update_bottom(self):
        Util.debug(3, "ScatterPlot.update_bottom", "")

        if self.plot().pgPlot() != None:
            self.update_axis('bottom')

    def update_left(self):
        Util.debug(3, "ScatterPlot.update_left", "")

        if self.plot().pgPlot() != None:
            self.update_axis('left')

    def update_top(self):
        Util.debug(3, "ScatterPlot.update_top", "")

        if self.plot().pgPlot() != None:
            self.update_axis('top')

    def update_right(self):
        Util.debug(3, "ScatterPlot.update_right", "")

        if self.plot().pgPlot() != None:
            self.update_axis('right')

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
        # Set linear or logarithmic scaling
        axis.setScaling(axisDict['scaleType'], axisDict['majorTicksLogBase'])

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
            
            if axisDict['scaleType'] in ('log', 'symlog'):
                subs = axisDict['majorTicksLogLocations'].split(',')
                subs = map(float, subs)
                axis.setTicksLocator('major', pgticker.LogLocator(axisDict['majorTicksLogBase'], subs), applyToSlaves=True)
            else:  # linear scaling
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
            return

        # Set the tick labels
        if axisDict['majorTicksLabelVisible']:
            if axisDict['majorTicksLabelUseNumeric']:
                axis.setTicksLabeler('major', pgticker.FormatLabeler(axisDict['majorTicksLabelNumericFormat']), applyToSlaves=True)
            elif axisDict['majorTicksLabelUseWave']:
                wave = self._app.waves().wave(str(axisDict['majorTicksLabelWave']))
                data = wave.data()
                axis.setTicksLabeler('major', pgticker.StringLabeler(data), applyToSlaves=True)

            axis.setTicksFont('major', pgfont.Font(**axisDict['majorTicksLabelFont'][0]), applyToSlaves=True)
            axis.setTickLabelProps('major', axisDict['majorTicksLabelFont'][1])
            axis.setTicksLength('major', axisDict['majorTicksLength'], applyToSlaves=True)
            axis.setTicksWidth('major', axisDict['majorTicksWidth'], applyToSlaves=True)
            axis.setTickMarkProps('major', color=axisDict['majorTicksColor'], applyToSlaves=True)
            axis.setTicksDirection('major', axisDict['majorTicksDirection'], applyToSlaves=True)
        
        # Tick labels are not visible
        else:
            axis.setTicksLabeler('major', pgticker.NullLabeler(), applyToSlaves=True)

    def update_axisMinorTicks(self, axis, axisDict):
        ticks = axis.ticks('minor')

        # Set the tick locations
        if axisDict['majorTicksVisible'] and axisDict['minorTicksVisible']:
            ticks.setVisible(True)

            if axisDict['scaleType'] in ('log', 'symlog'):
                subs = axisDict['minorTicksLogLocations'].split(',')
                subs = map(float, subs)
                axis.setTicksLocator('minor', pgticker.LogLocator(axisDict['majorTicksLogBase'], subs), applyToSlaves=True)
            else:
                axis.setTicksLocator('minor', pgticker.LinearLocator(axisDict['minorTicksNumber']), applyToSlaves=True)
            axis.setTicksLength('minor', axisDict['minorTicksLength'], applyToSlaves=True)
            axis.setTicksWidth('minor', axisDict['minorTicksWidth'], applyToSlaves=True)
            axis.setTickMarkProps('minor', color=axisDict['minorTicksColor'], applyToSlaves=True)
            axis.setTicksDirection('minor', axisDict['minorTicksDirection'], applyToSlaves=True)
        
        # Ticks are not visible
        else:
            ticks.setVisible(False)

    def update_axisTicks(self, axis, axisDict):
        self.update_axisMajorTicks(axis, axisDict)
        self.update_axisMinorTicks(axis, axisDict)

    def update_axisLabel(self, axis, axisDict):
        axis.setLabelText(axisDict['label'])
        axis.setLabelFont(pgfont.Font(**axisDict['labelFont'][0]))
        axis.setLabelProps(axisDict['labelFont'][1])

    def update_axisSlaving(self, axis, axisDict):
        if axisDict['slaveAxisToOther']:
            otherAxisName = axisDict['slavedTo']
            other = self.plot().pgPlot().axis(otherAxisName)
            axis.slaveTo(other)
        else:
            axis.unslave()

    def update_axis(self, axisName):
        if axisName in ('bottom', 'left', 'top', 'right'):
            axis = self.plot().pgPlot().axis(axisName)
        else:
            print "Unknown axis: " + str(axisName)
            return
        axisDict = self.getPg(axisName)

        if axisDict['visible']:
            axis.setVisible(True)
            self.update_axisSlaving(axis, axisDict)
            self.update_axisLimits(axis, axisDict)
            self.update_axisScaling(axis, axisDict)
    
            self.update_axisTicks(axis, axisDict)
    
            # Set axis label
            self.update_axisLabel(axis, axisDict)
        else:
            axis.setVisible(False)

        # Redraw the canvas
        self.plot().redraw()

    def refresh(self):
        for wavePair in self.wavePairs():
            wavePair.refresh()

        self.update_bottom()
        self.update_left()
        self.update_top()
        self.update_right()
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
                'backgroundColor':  Property.Color((255,255,255,255)),
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
        return tuple([self.__class__, tuple([self.get('name')]), tuple([self.properties, self.plotTypeObject, self._figure])])

    def __setstate__(self, state):
        properties = state[0]
        self.plotTypeObject = state[1]
        self._figure = state[2]
        
        self.initPgPlot()

        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)
        
        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

        #self.refresh()

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
        try:
            self.pgPlot().setTitle(self.getPg('name'))
            self.pgPlot().setTitle(self.getPg('nameFont')[1], pgfont.Font(**self.getPg('nameFont')[0]))
            self.pgPlot().title().draw()
        except:
            pass

    def update_nameFont(self):
        Util.debug(3, "Plot.update_nameFont", "")
        try:
            self.pgPlot().setTitle(self.getPg('nameFont')[1], pgfont.Font(**self.getPg('nameFont')[0]))
            self.pgPlot().title().draw()
        except:
            pass

    def update_backgroundColor(self):
        Util.debug(3, "Plot.update_backgroundColor", "")
        try:
            self.pgPlot().setColor(self.getPg('backgroundColor'))
            self.redraw()
        except:
            pass

    def refresh(self):
        self.update_name()
        self.update_backgroundColor()
        self.plotTypeObject.refresh()
        self.redraw()

    def redraw(self):
        try:
            self.pgPlot().clear()
            self.pgPlot().draw()
        except:
            pass

