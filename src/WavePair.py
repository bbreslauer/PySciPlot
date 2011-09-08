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

import Util, Property

from Wave import *
from FigureObject import *

from pygraphene import datapair as pgdp

class WavePair(FigureObject):
    """
    A pair of waves that are plotted against one another in some manner.
    This could be used for a scatter plot, a bar plot, or something else.
    """
    
    mplNames = {}

    def __init__(self, x=None, y=None, plot=None, properties={}):
        Util.debug(2, "WavePair.init", "Creating a wave pair")

        FigureObject.__init__(self, properties)

        self._line = None
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
            self.refreshLabel()

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
    
    pgLineProps = {
            'lineColor': 'color',
            'lineStyle': 'style',
            'lineWidth': 'width',
            }

    pgMarkerProps = {
            'pointMarker':             'marker',
            'pointMarkerEdgeColor':    'color',
            'pointMarkerEdgeWidth':    'width',
            'pointMarkerFaceColor':    'fillcolor',
            'pointMarkerSize':         'size',
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

    def getLineProps(self):
        propDict = {}

        for prop in self.pgLineProps.keys():
            propDict[self.pgLineProps[prop]] = self.getPg(prop)
        if propDict['style'] == 'none':
            propDict['visible'] = False
        else:
            propDict['visible'] = True
        return propDict

    def getMarkerProps(self):
        propDict = {}

        for prop in self.pgMarkerProps.keys():
            propDict[self.pgMarkerProps[prop]] = self.getPg(prop)
        if propDict['marker'] == 'none':
            propDict['visible'] = False
        else:
            propDict['visible'] = True
        return propDict

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
            self.plot().pgPlot().removeDataPair(self._line)
        except:
            pass
    
    def updatePlotData(self):
        """Only update the data on the plot. Do not change the format."""
        pass

        if self._line:
            [x, y] = self.dataSet()
            self._line.setX(x)
            self._line.setY(y)
            self.plot().redraw()
        else:
            self.refresh()

    def refresh(self):
        # If this trace is not associated with a plot, then don't do anything
        if self.plot() is None:
            return

        [x, y] = self.dataSet()
        pgPlot = self.plot().pgPlot()

        # Create a new DataPair if none exists. Otherwise, modify the current one.
        if self._line is None:
            self._line = pgdp.DataPair(pgPlot.canvas(), x, y, '', pgPlot.axis('bottom'), pgPlot.axis('left'), lineProps=self.getLineProps(), markerProps=self.getMarkerProps())
            pgPlot.addDataPair(self._line)
        else:
            self._line.setX(x)
            self._line.setY(y)
            self._line.setXAxis(pgPlot.axis('bottom'))
            self._line.setYAxis(pgPlot.axis('left'))
            self._line.setLineProps(**self.getLineProps())
            self._line.setMarkerProps(**self.getMarkerProps())

        self.plot().redraw()


class Bar(WavePair):
    pass
#class Bar(WavePair):
#    """A bar plot worth of data. NOT a single bar on a plot."""
#
#    verticalMplNames = {
#            'barThickness':     'width',
#            'barOffset':        'bottom',
#            'fillColor':        'color',
#            'edgeColor':        'edgecolor',
#            'edgeWidth':        'linewidth',
#            'align':            'align',
#            }
#
#    horizontalMplNames = {
#            'barThickness':     'height',
#            'barOffset':        'left',
#            'fillColor':        'color',
#            'edgeColor':        'edgecolor',
#            'edgeWidth':        'linewidth',
#            'align':            'align',
#            }
#
#    def __init__(self, x=None, y=None, plot=None):
#        Util.debug(2, "Bar.init", "Creating bar")
#
#        properties = {
#            'barThickness':     Property.Float(1.0),
#            'barOffset':        Property.Float(0.0),
#            'fillColor':        Property.Color(QColor(0,0,255,255)),
#            'edgeColor':        Property.Color(QColor(0,0,0,255)),
#            'edgeWidth':        Property.Float(0.0),
#            'align':            Property.String('edge'),
#                }
#
#        WavePair.__init__(self, x, y, plot, properties)
#
#    def getFormat(self):
#        formatDict = {}
#        
#        if self.plot().plotTypeObject.get('orientation') == 'vertical':
#            for prop in self.properties.keys():
#                formatDict[self.verticalMplNames[prop]] = self.getMpl(prop)
#        elif self.plot().plotTypeObject.get('orientation') == 'horizontal':
#            for prop in self.properties.keys():
#                formatDict[self.horizontalMplNames[prop]] = self.getMpl(prop)
#        return formatDict
#
#    def refreshLabel(self):
#        if self._rects:
#            self._rects[0].set_label(self.label())
#            self.plot().plotTypeObject.update_legend()
#
#    def removeFromPlot(self):
#        # If this trace is not associated with a plot, then don't do anything
#        if self.plot() is None:
#            return
#
#        # Remove the line if it exists
#        try:
#            for rect in self._rects:
#                rect.remove()
#        except:
#            pass
#
#    def refresh(self):
#        [base, extent] = self.dataSet()
#
#        if self.plot() is None:
#            return
#
#        self.removeFromPlot()
#
#        try:
#            if self.plot().plotTypeObject.get('orientation') == 'vertical':
#                self._rects = self.plot().axes().bar(base, extent, label=self.label(), **(self.getFormat()))
#            elif self.plot().plotTypeObject.get('orientation') == 'horizontal':
#                self._rects = self.plot().axes().barh(base, extent, label=self.label(), **(self.getFormat()))
#            self.plot().plotTypeObject.update_legend()
#            self.plot().redraw()
#        except:
#            return
#
#    def updatePlotData(self):
#        # FIXME
#        self.refresh()
#




