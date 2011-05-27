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


from PyQt4.QtGui import QWidget, QApplication, QDialogButtonBox

from QEditFigureSubWidget import *
from QCartesianPlotTypeWidget import *
from models.PlotListModel import *
from ui.Ui_PlotTypeWidget import *
from ui.Ui_StoredSettingsWidget import *
from gui.QStoredSettingsWidget import *
from gui.SubWindows import SubWindow

class QPlotOptionsWidget(QEditFigureSubWidget):

    properties = (
                'name',
                'nameFont',
                'backgroundColor',
                'plotType',
            )

    def __init__(self, *args):
        QEditFigureSubWidget.__init__(self, *args)
        self._currentPlot = None
    
    def currentPlot(self):
        return self._currentPlot

    def initPlotSelector(self):
        self._plotListModel = PlotListModel()
        plotSelector = self.getChild('plotSelector')
        plotSelector.setModel(self._plotListModel)

    def initSubWidgets(self):
        # Add all the plot widgets to the stack
        self.scatterPlotWidget = QCartesianPlotTypeWidget(self, self.getChild('plotTypeStack'))
        scatterPlotWidgetUi = Ui_PlotTypeWidget()
        scatterPlotWidgetUi.setupUi(self.scatterPlotWidget)
        self.scatterPlotWidget.initSubWidgets()
        self.getChild('plotTypeStack').addWidget(self.scatterPlotWidget)
        self.getChild('plotType').addItem('Scatter Plot')

        #self.barPlotWidget = QEditFigureSubWidget(self.getChild('plotTypeStack'))
        self.barPlotWidget = QCartesianPlotTypeWidget(self, self.getChild('plotTypeStack'))
        barPlotWidgetUi = Ui_PlotTypeWidget()
        barPlotWidgetUi.setupUi(self.barPlotWidget)
        self.barPlotWidget.initSubWidgets()
        self.getChild('plotTypeStack').addWidget(self.barPlotWidget)
        self.getChild('plotType').addItem('Bar Chart')

        self.piePlotWidget = QEditFigureSubWidget(self.getChild('plotTypeStack'))
        piePlotWidgetUi = Ui_PlotTypeWidget()
        piePlotWidgetUi.setupUi(self.piePlotWidget)
        self.getChild('plotTypeStack').addWidget(self.piePlotWidget)
        self.getChild('plotType').addItem('Pie Chart')

        self.getChild('plotType').setCurrentRow(0)

    def changeCurrentPlot(self, index):
        if index < 0:
            return

        self._currentPlot = self._plotListModel.getPlot(index)
        self.getChild('plotSelector').setCurrentIndex(index)
        self.resetUi()
        self.getChild('plotTypeStack').currentWidget().resetUi() # Reset the plot type widget's ui

    def setFigure(self, figure, index=0):
        """
        Set the figure whose plots should be displayed.
        """

        if not figure:
            return

        self._plotListModel.setFigure(figure)
        self._plotListModel.doReset()

        if index >= figure.numPlots():
            index = 0
        
        self.changeCurrentPlot(index)
    
    def refreshPlotSelector(self):
        """
        Refresh the plot selector.  Intended to be used if the number of
        plots on a figure changes, so that we can make sure that the combo box
        is still valid.
        """
        self.setFigure(self._editFigureDialogModule.currentFigure(), self.getChild('plotSelector').currentIndex())

    def saveUi(self):
        """Save the UI data to the current Plot object."""
        
        self.currentPlot().setMultiple(self.getCurrentUi())

    def resetUi(self):
        """
        Set the UI to the current Plot's settings.
        
        Any unknown widget types will be discarded.
        """
        
        self.setCurrentUi(self.currentPlot().properties)

        # Change the plot type widget that is shown based on the type of plot
        # that is currently selected (scatter, pie, etc)
        self.getChild('plotTypeStack').setCurrentIndex(self.getChild('plotType').currentRow())


    def applyClicked(self):
        self.saveUi()
        self.refreshPlotSelector()

    def reload(self):
        self.scatterPlotWidget.reload()


