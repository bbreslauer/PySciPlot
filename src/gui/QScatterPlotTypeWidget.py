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
from QScatterPlotAxisWidget import *
from QScatterPlotTracesWidget import *
from QScatterPlotLegendWidget import *
from ui.Ui_ScatterPlotAxis import *
from ui.Ui_ScatterPlotTraces import *
from ui.Ui_ScatterPlotLegend import *

class QScatterPlotTypeWidget(QEditFigureSubWidget):

    def __init__(self, plotOptionsWidget, *args):
        QEditFigureSubWidget.__init__(self, *args)

        self._plotOptionsWidget = plotOptionsWidget

    def initSubWidgets(self):
        # Add the various tabs to this widget
        self.bottomAxis = QScatterPlotAxisWidget(self.getChild('tabWidget'))
        bottomAxisUi = Ui_ScatterPlotAxis()
        bottomAxisUi.setupUi(self.bottomAxis)
        self.getChild('tabWidget').addTab(self.bottomAxis, 'Bottom Axis')

        self.leftAxis = QScatterPlotAxisWidget(self.getChild('tabWidget'))
        leftAxisUi = Ui_ScatterPlotAxis()
        leftAxisUi.setupUi(self.leftAxis)
        self.getChild('tabWidget').addTab(self.leftAxis, 'Left Axis')

        self.traces = QScatterPlotTracesWidget(self._plotOptionsWidget, self.getChild('tabWidget'))
        tracesUi = Ui_ScatterPlotTraces()
        tracesUi.setupUi(self.traces)
        self.traces.initSubWidgets()
        self.getChild('tabWidget').addTab(self.traces, 'Traces')

        self.legend = QScatterPlotLegendWidget(self.getChild('tabWidget'))
        legendUi = Ui_ScatterPlotLegend()
        legendUi.setupUi(self.legend)
        self.getChild('tabWidget').addTab(self.legend, 'Legend')

    def saveUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        self.traces.saveOptionsToSelectedTraces()
        
        bottomAxisUiOptions = self.bottomAxis.getCurrentUi()
        plotTypeObject.set('bottomAxis', bottomAxisUiOptions)

        leftAxisUiOptions = self.leftAxis.getCurrentUi()
        plotTypeObject.set('leftAxis', leftAxisUiOptions)

        legendUiOptions = self.legend.getCurrentUi()
        plotTypeObject.set('legend', legendUiOptions)

    def resetUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        bottomAxisOptions = plotTypeObject.get('bottomAxis')
        self.bottomAxis.setCurrentUi(bottomAxisOptions)

        leftAxisOptions = plotTypeObject.get('leftAxis')
        self.leftAxis.setCurrentUi(leftAxisOptions)

        legendOptions = plotTypeObject.get('legend')
        self.legend.setCurrentUi(legendOptions)

        self.traces.resetUi()

