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


from PySide.QtGui import QWidget, QApplication

from QEditFigureSubWidget import *
from QCartesianPlotAxisWidget import *
from QCartesianPlotWavePairsWidget import *
from QPlotLegendWidget import *
from ui.Ui_CartesianPlotAxis import *
from ui.Ui_ScatterPlotTraces import *
from ui.Ui_BarPlotBars import *
from ui.Ui_PlotLegend import *

import Util

class QCartesianPlotTypeWidget(QEditFigureSubWidget):

    def __init__(self, plotOptionsWidget, *args):
        QEditFigureSubWidget.__init__(self, *args)

        self._plotOptionsWidget = plotOptionsWidget

    def initSubWidgets(self):
        # Add the various tabs to this widget
        self.bottom = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        bottomAxisUi = Ui_CartesianPlotAxis()
        bottomAxisUi.setupUi(self.bottom)
        self.bottom.initSubWidgets()
        self.getChild('tabWidget').addTab(self.bottom, 'Bottom Axis')

        self.left = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        leftAxisUi = Ui_CartesianPlotAxis()
        leftAxisUi.setupUi(self.left)
        self.left.initSubWidgets()
        self.getChild('tabWidget').addTab(self.left, 'Left Axis')
        Util.setWidgetValue(self.left.getChild('slavedTo'), 'left')

        self.top = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        topAxisUi = Ui_CartesianPlotAxis()
        topAxisUi.setupUi(self.top)
        self.top.initSubWidgets()
        self.getChild('tabWidget').addTab(self.top, 'Top Axis')
        Util.setWidgetValue(self.top.getChild('slaveAxisToOther'), True)

        self.right = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        rightAxisUi = Ui_CartesianPlotAxis()
        rightAxisUi.setupUi(self.right)
        self.right.initSubWidgets()
        self.getChild('tabWidget').addTab(self.right, 'Right Axis')
        Util.setWidgetValue(self.right.getChild('slavedTo'), 'left')
        Util.setWidgetValue(self.right.getChild('slaveAxisToOther'), True)

        self.legend = QPlotLegendWidget(self.getChild('tabWidget'))
        legendUi = Ui_PlotLegend()
        legendUi.setupUi(self.legend)
        self.getChild('tabWidget').addTab(self.legend, 'Legend')

        # Some axis options will always be linked together (such as the bottom and top scale types), and so 
        # we should link them in the UI so that the user knows that they are the same.

    def saveUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        bottomAxisUiOptions = self.bottom.getCurrentUi()
        plotTypeObject.set('bottom', bottomAxisUiOptions)

        leftAxisUiOptions = self.left.getCurrentUi()
        plotTypeObject.set('left', leftAxisUiOptions)
        
        topAxisUiOptions = self.top.getCurrentUi()
        plotTypeObject.set('top', topAxisUiOptions)

        rightAxisUiOptions = self.right.getCurrentUi()
        plotTypeObject.set('right', rightAxisUiOptions)

        legendUiOptions = self.legend.getCurrentUi()
        plotTypeObject.set('legend', legendUiOptions)

        self.wavePairs.saveOptionsToSelectedWavePairs()

    def resetUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        bottomAxisOptions = plotTypeObject.get('bottom')
        self.bottom.setCurrentUi(bottomAxisOptions)

        leftAxisOptions = plotTypeObject.get('left')
        self.left.setCurrentUi(leftAxisOptions)

        topAxisOptions = plotTypeObject.get('top')
        self.top.setCurrentUi(topAxisOptions)

        rightAxisOptions = plotTypeObject.get('right')
        self.right.setCurrentUi(rightAxisOptions)

        legendOptions = plotTypeObject.get('legend')
        self.legend.setCurrentUi(legendOptions)

        self.wavePairs.resetUi()

    def reload(self):
        self.bottom.initSubWidgets()
        self.left.initSubWidgets()
        self.top.initSubWidgets()
        self.right.initSubWidgets()

        self.wavePairs.initSubWidgets()


class QScatterPlotTypeWidget(QCartesianPlotTypeWidget):

    def __init__(self, plotOptionsWidget, *args):
        QCartesianPlotTypeWidget.__init__(self, plotOptionsWidget, *args)

    def initSubWidgets(self):
        QCartesianPlotTypeWidget.initSubWidgets(self)

        self.wavePairs = QScatterPlotTracesWidget(self._plotOptionsWidget, self.getChild('tabWidget'))
        tracesUi = Ui_ScatterPlotTraces()
        tracesUi.setupUi(self.wavePairs)
        self.wavePairs.initSubWidgets()
        self.getChild('tabWidget').insertTab(4, self.wavePairs, 'Traces')

class QBarPlotTypeWidget(QCartesianPlotTypeWidget):

    def __init__(self, plotOptionsWidget, *args):
        QCartesianPlotTypeWidget.__init__(self, plotOptionsWidget, *args)

    def initSubWidgets(self):
        QCartesianPlotTypeWidget.initSubWidgets(self)

        self.wavePairs = QBarPlotBarsWidget(self._plotOptionsWidget, self.getChild('tabWidget'))
        barsUi = Ui_BarPlotBars()
        barsUi.setupUi(self.wavePairs)
        self.wavePairs.initSubWidgets()
        self.getChild('tabWidget').insertTab(4, self.wavePairs, 'Bars')



