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


from PyQt4.QtGui import QWidget, QApplication

from QEditFigureSubWidget import *
from QCartesianPlotAxisWidget import *
from QCartesianPlotWavePairsWidget import *
from QPlotLegendWidget import *
from ui.Ui_CartesianPlotAxis import *
from ui.Ui_ScatterPlotTraces import *
from ui.Ui_BarPlotBars import *
from ui.Ui_PlotLegend import *


class QCartesianPlotTypeWidget(QEditFigureSubWidget):

    def __init__(self, plotOptionsWidget, *args):
        QEditFigureSubWidget.__init__(self, *args)

        self._plotOptionsWidget = plotOptionsWidget

    def initSubWidgets(self):
        # Add the various tabs to this widget
        self.bottomAxis = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        bottomAxisUi = Ui_CartesianPlotAxis()
        bottomAxisUi.setupUi(self.bottomAxis)
        self.bottomAxis.initSubWidgets()
        self.getChild('tabWidget').addTab(self.bottomAxis, 'Bottom Axis')

        self.leftAxis = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        leftAxisUi = Ui_CartesianPlotAxis()
        leftAxisUi.setupUi(self.leftAxis)
        self.leftAxis.initSubWidgets()
        self.getChild('tabWidget').addTab(self.leftAxis, 'Left Axis')

        self.topAxis = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        topAxisUi = Ui_CartesianPlotAxis()
        topAxisUi.setupUi(self.topAxis)
        self.topAxis.initSubWidgets()
        self.getChild('tabWidget').addTab(self.topAxis, 'Top Axis')
        self.getChild('tabWidget').setTabEnabled(2, False)

        self.rightAxis = QCartesianPlotAxisWidget(self.getChild('tabWidget'))
        rightAxisUi = Ui_CartesianPlotAxis()
        rightAxisUi.setupUi(self.rightAxis)
        self.rightAxis.initSubWidgets()
        self.getChild('tabWidget').addTab(self.rightAxis, 'Right Axis')
        self.getChild('tabWidget').setTabEnabled(3, False)

        self.legend = QPlotLegendWidget(self.getChild('tabWidget'))
        legendUi = Ui_PlotLegend()
        legendUi.setupUi(self.legend)
        self.getChild('tabWidget').addTab(self.legend, 'Legend')

        # Some axis options will always be linked together (such as the bottom and top scale types), and so 
        # we should link them in the UI so that the user knows that they are the same.

    def saveUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        bottomAxisUiOptions = self.bottomAxis.getCurrentUi()
        plotTypeObject.set('bottomAxis', bottomAxisUiOptions)

        leftAxisUiOptions = self.leftAxis.getCurrentUi()
        plotTypeObject.set('leftAxis', leftAxisUiOptions)
        
        topAxisUiOptions = self.topAxis.getCurrentUi()
        plotTypeObject.set('topAxis', topAxisUiOptions)

        rightAxisUiOptions = self.rightAxis.getCurrentUi()
        plotTypeObject.set('rightAxis', rightAxisUiOptions)

        legendUiOptions = self.legend.getCurrentUi()
        plotTypeObject.set('legend', legendUiOptions)

        self.wavePairs.saveOptionsToSelectedWavePairs()

    def resetUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        bottomAxisOptions = plotTypeObject.get('bottomAxis')
        self.bottomAxis.setCurrentUi(bottomAxisOptions)

        leftAxisOptions = plotTypeObject.get('leftAxis')
        self.leftAxis.setCurrentUi(leftAxisOptions)

        topAxisOptions = plotTypeObject.get('topAxis')
        self.topAxis.setCurrentUi(topAxisOptions)

        rightAxisOptions = plotTypeObject.get('rightAxis')
        self.rightAxis.setCurrentUi(rightAxisOptions)

        legendOptions = plotTypeObject.get('legend')
        self.legend.setCurrentUi(legendOptions)

        self.wavePairs.resetUi()

    def reload(self):
        self.bottomAxis.initSubWidgets()
        self.leftAxis.initSubWidgets()
        self.topAxis.initSubWidgets()
        self.rightAxis.initSubWidgets()

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



