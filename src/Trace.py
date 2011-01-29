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


from PyQt4.QtGui import QColor, QApplication

import Util, Property

from Wave import *
from FigureObject import *

class Trace(FigureObject):
    """An x-y pair of data."""
                            
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
        
        self._app = QApplication.instance().window

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

        FigureObject.__init__(self, properties)

        self.initializeVariables()
        self.setX(x)
        self.setY(y)
        self.setPlot(plot)

        # If a wave is removed from the app, see if this trace held it
        self._app.waves().waveRemoved[Wave].connect(self.removeTraceIfContainsWave)

        self.getFormat()

    def __reduce__(self):
        #return tuple([self.__class__, tuple([self.x(), self.y(), self.plot()]), tuple([self.properties])])
        return tuple([self.__class__, tuple(), tuple([self.properties, self.xName(), self.yName(), self.plot()])])

    def __setstate__(self, state):
        properties = state[0]
        xName = state[1]
        yName = state[2]
        plot = state[3]

        self.setX(self._app.waves().getWaveByName(xName))
        self.setY(self._app.waves().getWaveByName(yName))
        self.setPlot(plot)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(True)

        self.setMultiple(properties)

        for (key, value) in properties.items():
            self.properties[key].blockSignals(False)

        # Connect the waves that were saved in this pickle to the application
        appX = self._app.waves().getWaveByName(self.xName())
        if appX:
            self.setX(appX)
        else:
            self._app.waves().addWave(self.x())

        appY = self._app.waves().getWaveByName(self.yName())
        if appY:
            self.setY(appY)
        else:
            self._app.waves().addWave(self.y())

        self.plot().refresh()

    def initializeVariables(self):
        Util.debug(3, "Trace.initializeVariables", "Initializing variables")
        self._x = None
        self._y = None
        
    def setPlot(self, plot):
        self._plot = plot

    def plot(self):
        return self._plot
    
    def setX(self, x):
        Util.debug(2, "Trace.setX", "Setting x trace")
        
        # Disconnect previous wave's dataModified signal
        try:
            self._x.dataModified.disconnect(self.refresh)
        except:
            pass

        # Set new wave
        self._x = x

        # Connect new wave's dataModified signal
        try:
            self._x.dataModified.connect(self.refresh)
        except:
            pass
        
    def setY(self, y):
        Util.debug(2, "Trace.setY", "Setting y trace")
        # Disconnect previous wave's dataModified signal
        try:
            self._y.dataModified.disconnect(self.refresh)
        except:
            pass

        # Set new wave
        self._y = y

        # Connect new wave's dataModified signal
        try:
            self._y.dataModified.connect(self.refresh)
        except:
            pass
    
    def x(self):
        return self._x
        
    def y(self):
        return self._y

    def xName(self):
        return self._x.name()

    def yName(self):
        return self._y.name()

    def getFormat(self):
        formatDict = {}
        
        for prop in self.properties.keys():
            formatDict[self.mplNames[prop]] = self.getMpl(prop)
        return formatDict

    def convertDataToFloat(self):
        xData = Wave.convertToFloatList(self.x())
        yData = Wave.convertToFloatList(self.y())

        # Make sure waves are the same length, or else matplotlib will complain and not plot them
        diffLength = len(xData) - len(yData)
        if diffLength < 0:
            xData.extend([nan] * (- diffLength))
        elif diffLength > 0:
            yData.extend([nan] * diffLength)

        return [xData, yData]

    def removeFromPlot(self):
        # If this trace is not associated with a plot, then don't do anything
        if self.plot() is None:
            return

        # Remove the line if it exists
        try:
            self._line.remove()
        except:
            pass

    def refresh(self):
        [x, y] = self.convertDataToFloat()
        
        # If this trace is not associated with a plot, then don't do anything
        if self.plot() is None:
            return

        self.removeFromPlot()

        # If the axes object does not yet exist in the plot object, then
        # we cannot plot anything
        try:
            self._line = self.plot().axes().plot(x, y, **(self.getFormat()))[0]
            self.plot().redraw()
        except:
            return
        

    def removeTraceIfContainsWave(self, wave):
        if wave == self.x() or wave == self.y():
            self.plot().plotTypeObject.removeTrace(self)
        
