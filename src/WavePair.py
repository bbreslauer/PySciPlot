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

import Util, Property

from Wave import *
from FigureObject import *

class WavePair(FigureObject):
    """
    A pair of waves that are plotted against one another in some manner.
    This could be used for a scatter plot, a bar plot, or something else.
    """

    def __init__(self, x=None, y=None, plot=None, properties={}):
        Util.debug(2, "WavePair.init", "Creating a wave pair")

        FigureObject.__init__(self, properties)
        
        self.initializeVariables()
        self.setX(x)
        self.setY(y)
        self.setPlot(plot)

        try:
            self.setLabel(str(self.xName()) + "-" + str(self.yName()))
        except AttributeError:
            # x or y is None, so xName() and yName() don't work.
            self.setLabel("")

        # If a wave is removed from the app, see if this trace held it
        self._app.waves().waveRemoved[Wave].connect(self.deleteIfContainsWave)

    def __reduce__(self):
        return tuple([self.__class__, tuple(), tuple([self.properties, self.xName(), self.yName(), self.label(), self.plot()])])

    def __setstate__(self, state):
        properties = state[0]
        xName = state[1]
        yName = state[2]
        label = state[3]
        plot = state[4]

        self.setX(self._app.waves().wave(xName))
        self.setY(self._app.waves().wave(yName))
        self.setLabel(label)
        self.setPlot(plot)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

        # Connect the waves that were saved in this pickle to the application
        appX = self._app.waves().wave(self.xName())
        if appX:
            self.setX(appX)
        else:
            self._app.waves().addWave(self.x())

        appY = self._app.waves().wave(self.yName())
        if appY:
            self.setY(appY)
        else:
            self._app.waves().addWave(self.y())

        # FIXME IS THIS THE PROPER REFRESH? OR SHOULD IT BE IN THE WAVEPAIR CLASS?
        self.refresh()

    def initializeVariables(self):
        Util.debug(3, "WavePair.initializeVariables", "Initializing variables")
        self._x = None
        self._y = None
        self._plot = None
        self._label = ""

    def setPlot(self, plot):
        self._plot = plot

    def plot(self):
        return self._plot

    def setLabel(self, label):
        self._label = str(label)
        if self.plot() != None:
            self.updatePlotTraceLabel()

    def label(self):
        return self._label

    def setX(self, x):
        Util.debug(2, "WavePair.setX", "Setting x")
        
        # Disconnect previous wave's dataModified signal
        try:
            self._x.dataModified.disconnect(self.updatePlotData)
        except:
            pass

        # Set new wave
        self._x = x

        # Connect new wave's dataModified signal
        try:
            self._x.dataModified.connect(self.updatePlotData)
            self.updatePlotData()
        except:
            # If self._x is Null, then the above will fail
            pass
        
    def setY(self, y):
        Util.debug(2, "WavePair.setY", "Setting y")
        # Disconnect previous wave's dataModified signal
        try:
            self._y.dataModified.disconnect(self.updatePlotData)
        except:
            pass

        # Set new wave
        self._y = y

        # Connect new wave's dataModified signal
        try:
            self._y.dataModified.connect(self.updatePlotData)
            self.updatePlotData()
        except:
            # If self._y is Null, then the above will fail
            pass

    def x(self):
        return self._x
        
    def y(self):
        return self._y

    def xName(self):
        return self._x.name()

    def yName(self):
        return self._y.name()

    def dataSet(self):
        """
        Convert the two waves into a pair of lists that can be plotted by matplotlib.
        """

        xData = Wave.convertToFloatList(self.x())
        yData = Wave.convertToFloatList(self.y())

        # Make sure waves are the same length, or else matplotlib will complain and not plot them
        diffLength = len(xData) - len(yData)
        if diffLength < 0:
            xData.extend([nan] * (- diffLength))
        elif diffLength > 0:
            yData.extend([nan] * diffLength)

        return [xData, yData]

    def refreshLabel(self):
        raise NotImplementedError

    def removeFromPlot(self):
        raise NotImplementedError
        
    def updatePlotData(self):
        raise NotImplementedError

    def refresh(self):
        raise NotImplementedError

    def deleteIfContainsWave(self, wave):
        if wave == self.x() or wave == self.y():
            self.plot().plotTypeObject.removeWavePair(self)


class Trace(WavePair):
    """A pair of waves for use in a scatter plot."""

    mplNames = {
            'lineColor':               'color',
            'lineStyle':               'linestyle',
            'lineWidth':               'linewidth',
            'pointMarker':             'marker',
            'pointMarkerEdgeColor':    'markeredgecolor',
            'pointMarkerEdgeWidth':    'markeredgewidth',
            'pointMarkerFaceColor':    'markerfacecolor',
            'pointMarkerSize':         'markersize',
            }


    def __init__(self, x=None, y=None, plot=None):
        Util.debug(2, "Trace.init", "Creating trace")

        properties = {
            'lineColor':               Property.Color(QColor(255,0,0,255)),
            'lineStyle':               Property.LineStyle('Solid'),
            'lineWidth':               Property.Float(1.0),
            'pointMarker':             Property.PointMarker('Point'),
            'pointMarkerEdgeColor':    Property.Color(QColor(0,0,0,255)),
            'pointMarkerEdgeWidth':    Property.Float(1.0),
            'pointMarkerFaceColor':    Property.Color(QColor(0,0,0,255)),
            'pointMarkerSize':         Property.Float(1.0),
                }

        WavePair.__init__(self, x, y, plot, properties)

    def getFormat(self):
        formatDict = {}
        
        for prop in self.properties.keys():
            formatDict[self.mplNames[prop]] = self.getMpl(prop)
        return formatDict

    def refreshLabel(self):
        if self._line:
            self._line.set_label(self.label())
            self.plot().plotTypeObject.update_legend()

    def removeFromPlot(self):
        # If this trace is not associated with a plot, then don't do anything
        if self.plot() is None:
            return

        # Remove the line if it exists
        try:
            self._line.remove()
        except:
            pass
    
    def updatePlotData(self):
        """Only update the data on the plot. Do not change the format."""
        
        if self._line:
            [x, y] = self.dataSet()
            self._line.set_data(x, y)
            self.plot().redraw()
        else:
            self.refresh()

    def refresh(self):
        [x, y] = self.dataSet()
        
        # If this trace is not associated with a plot, then don't do anything
        if self.plot() is None:
            return

        self.removeFromPlot()

        # If the axes object does not yet exist in the plot object, then
        # we cannot plot anything
        try:
            self._line = self.plot().axes().plot(x, y, label=self.label(), **(self.getFormat()))[0]
            self.plot().plotTypeObject.update_legend()
            self.plot().redraw()
        except:
            return



class Bar(WavePair):
    pass

#class Bar(WavePair):
#    """A bar plot worth of data. NOT a single bar on a plot."""
#
#    mplNames = {
#            }
#
#    def __init__(self, leftWave=None, heightWave=None, plot=None):
#        Util.debug(2, "Bar.init", "Creating bar")
#
#        properties = {
#            'width':        Property.Float(1.0),
#            'bottom':       Property.Float(0.0),
#                }
#
#        FigureObject.__init__(self, properties)
#        
#        self.initializeVariables()
#        self.setLeft(left)
#        self.setHeight(height)
#        self.setPlot(plot)
#
#        try:
#            self.setLabel(str(self.leftName()) + "-" + str(self.heightName()))
#        except AttributeError:
#            # x or y is None, so xName() and yName() don't work.
#            self.setLabel("")
#
#        # If a wave is removed from the app, see if this trace held it
#        self._app.waves().waveRemoved[Wave].connect(self.removeBarIfContainsWave)
#
#        self.getFormat()
#
#    def __reduce__(self):
#        pass
#
#    def __setstate__(self, state):
#        pass
#
#    def initializeVariables(self):
#        Util.debug(3, "Bar.initializeVariables", "Initializing variables")
#        self._left = None
#        self._height = None
#        
#    def setPlot(self, plot):
#        self._plot = plot
#
#    def plot(self):
#        return self._plot
#
#    def setLabel(self, label):
#        self._label = str(label)
#        if self.plot() != None:
#            self.updatePlotBarLabel()
#
#    def label(self):
#        return self._label
#
#    def setLeft(self, left):
#        Util.debug(2, "Bar.setLeft", "Setting left")
#        
#        # Disconnect previous wave's dataModified signal
#        try:
#            self._left.dataModified.disconnect(self.updatePlotData)
#        except:
#            pass
#
#        # Set new wave
#        self._left = left
#
#        # Connect new wave's dataModified signal
#        try:
#            self._left.dataModified.connect(self.updatePlotData)
#            self.updatePlotData()
#        except:
#            # If self._left is Null, then the above will fail
#            pass
#
#    def setHeight(self, height):
#        Util.debug(2, "Bar.setHeight", "Setting height")
#        
#        # Disconnect previous wave's dataModified signal
#        try:
#            self._height.dataModified.disconnect(self.updatePlotData)
#        except:
#            pass
#
#        # Set new wave
#        self._height = height
#
#        # Connect new wave's dataModified signal
#        try:
#            self._height.dataModified.connect(self.updatePlotData)
#            self.updatePlotData()
#        except:
#            # If self._height is Null, then the above will fail
#            pass
#
#    def left(self):
#        return self._left
#
#    def height(self):
#        return self._height
#
#    def leftName(self):
#        return self._left.name()
#
#    def heightName(self):
#        return self._height.name()
#
#    def getFormat(self):
#        formatDict = {}
#        
#        for prop in self.properties.keys():
#            formatDict[prop] = self.getMpl(prop)
#        return formatDict
#
#    def convertDataToBars(self):
#        leftData = Wave.convertToFloatList(self.left())
#        heightData = Wave.convertToFloatList(self.height())
#
#        # Make sure waves are the same length, or else matplotlib will complain and not plot them
#        diffLength = len(leftData) - len(heightData)
#        if diffLength < 0:
#            leftData.extend([nan] * (- diffLength))
#        elif diffLength > 0:
#            heightData.extend([nan] * diffLength)
#
#        return [leftData, heightData]
#
#    def removeFromPlot(self):
#        pass
#
#    def refresh(self):
#        [left, height] = self.convertDataToBars()
#
#        if self.plot() is None:
#            return
#
#        self.removeFromPlot()
#
#        try:
#            self._rects = self.plot().axes().bar(left, height, **(self.getFormat()))
#            self.plot().plotTypeObject.update_legend()
#            self.plot().redraw()
#        except:
#            return
#
#    def updatePlotData(self):
#        self.refresh()
#
#    def updatePlotBarLabel(self):
#        pass
#
#    def removeBarIfContainsWave(self, wave):
#        pass
#
#
