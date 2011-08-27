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


from PySide.QtGui import QWidget, QMenu, QAction, QApplication

import Util
import copy
from Wave import *
from WavePair import *
from Delegates import WavePairListDelegate
from models.WavePairListModel import *
from QEditFigureSubWidget import *

class QCartesianPlotWavePairsWidget(QEditFigureSubWidget):

    properties = WavePair.mplNames.keys()

    def __init__(self, plotOptionsWidget, *args):
        QEditFigureSubWidget.__init__(self, *args)

        self._plotOptionsWidget = plotOptionsWidget

    def initSubWidgets(self):
        self.setModels()

    def setModels(self):
        # Setup X and Y lists
        self._wavesModel = self._app.model('appWaves')
        self.getChild('xAxisListView').setModel(self._wavesModel)
        
        self.getChild('yAxisListView').setModel(self._wavesModel)
        
        # Setup WavePair list
        wavePairListModel = WavePairListModel()
        self.getChild('wavePairTableView').setModel(wavePairListModel)
        self.setupWavePairListMenu()
        wavePairListDelegate = WavePairListDelegate(self._wavesModel)
        self.getChild('wavePairTableView').setItemDelegate(wavePairListDelegate)

        self.getChild('wavePairTableView').selectionModel().currentChanged.connect(self.selectedWavePairChanged)

    def setupWavePairListMenu(self):
        
        self.wavePairListMenu = QMenu(self.getChild('wavePairTableView'))

        self.deleteWavePairFromWavePairListAction = QAction("Delete WavePair", self.wavePairListMenu)
        self.wavePairListMenu.addAction(self.deleteWavePairFromWavePairListAction)

    def addWavePairsToPlot(self, wavePairType):
        # This is the scatter plot, which holds the WavePairs.  the plot object does not hold the WavePairs
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject

        xAxisList = self.getChild('xAxisListView').selectedIndexes()
        yAxisList = self.getChild('yAxisListView').selectedIndexes()

        for x in xAxisList:
            for y in yAxisList:
                xWave = self._wavesModel.waveByRow(x.row())
                yWave = self._wavesModel.waveByRow(y.row())
                wavePair = wavePairType(xWave, yWave)
                plotTypeObject.addWavePair(wavePair)
                self.saveOptionsToWavePair(wavePair)

        self.refreshWavePairList()

    def refreshWavePairList(self, *args):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject

        # Clear plot list model
        wavePairListModel = self.getChild('wavePairTableView').model()
        wavePairListModel.clearData()
            
        for wavePair in plotTypeObject.wavePairs():
            wavePairListModel.addWavePair(wavePair)

        self.getChild('wavePairTableView').resizeRowsToContents()
        self.getChild('wavePairTableView').resizeColumnsToContents()

        wavePairListModel.doReset()

        self.getChild('wavePairTableView').selectRow(wavePairListModel.rowCount() - 1)
        
    def showWavePairListMenu(self, point):
        """Display the menu that occurs when right clicking on a WavePair entry."""

        index = self.getChild('wavePairTableView').indexAt(point)
        
        if index.row() < 0:
            return False
        
        def deleteWavePairHelper():
            self.deleteWavePairFromPlot(index.internalPointer())

        # Connect actions
        self.deleteWavePairFromWavePairListAction.triggered.connect(deleteWavePairHelper)

        self.wavePairListMenu.exec_(self.getChild('wavePairTableView').mapToGlobal(point))
        
        # Disconnect actions, so that we don't have multiple connections when
        # the menu is opened again.
        self.deleteWavePairFromWavePairListAction.triggered.disconnect(deleteWavePairHelper)

    def deleteSelectedWavePairs(self):
        """Delete all the WavePairs that are selected from the plot."""

        indexes = self.getChild('wavePairTableView').selectedIndexes()

        # Get the WavePairs corresponding to the indexes. However, each index
        # corresponds to a cell, not a row, so we need to remove duplicate WavePair
        # entries from the indexes list so as not to attempt to delete them multiple times.
        wavePairs = Util.uniqueList(map(lambda x: x.internalPointer(), indexes))

        for wavePair in wavePairs:
            self.deleteWavePairFromPlot(wavePair)

    def deleteWavePairFromPlot(self, wavePair):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        plotTypeObject.removeWavePair(wavePair)
        self.refreshWavePairList()

    def saveOptionsToWavePair(self, wavePair):
        wavePair.setMultiple(self.getCurrentUi())

    def saveOptionsToSelectedWavePairs(self):
        indexes = self.getChild('wavePairTableView').selectedIndexes()
        
        wavePairs = set()  # We use a set because each row has two selected indexes, and 
                        # we want to don't want to double-count rows
        for index in indexes:
            wavePairs.add(index.internalPointer())

        for wavePair in wavePairs:
            self.saveOptionsToWavePair(wavePair)

    def setUiToWavePair(self, wavePair):
        self.setCurrentUi(wavePair.properties)

    def selectedWavePairChanged(self, newIndex, oldIndex):
        self.setUiToWavePair(newIndex.internalPointer())

    def saveUi(self):
        self.saveOptionsToSelectedWavePairs()

    def resetUi(self):
        
        # disconnect only if the signal is connected
        try:
            self._plotOptionsWidget.currentPlot().plotTypeObject.wavePairRemovedFromPlot.disconnect()
        except:
            pass
        
        self._plotOptionsWidget.currentPlot().plotTypeObject.wavePairRemovedFromPlot.connect(self.getChild('wavePairTableView').model().removeWavePair)

        self.refreshWavePairList()



class QScatterPlotTracesWidget(QCartesianPlotWavePairsWidget):

    properties = Trace.mplNames.keys()

    def __init__(self, plotOptionsWidget, *args):
        QCartesianPlotWavePairsWidget.__init__(self, plotOptionsWidget, *args)

    def initSubWidgets(self):
        self.getChild('lineColor').initButtonColor()
        self.getChild('pointMarkerFaceColor').initButtonColor()
        self.getChild('pointMarkerEdgeColor').initButtonColor()

        QCartesianPlotWavePairsWidget.initSubWidgets(self)

    def addWavePairsToPlot(self):
        QCartesianPlotWavePairsWidget.addWavePairsToPlot(self, Trace)


class QBarPlotBarsWidget(QCartesianPlotWavePairsWidget):

    # We need to deal with the special orientation property, which belongs to the entire plot,
    # but is chosen in this widget. This involves reimplementing the init, saveOptionsToWavePair,
    # and setUiToWavePair methods, so that we don't try to save or load orientation from each
    # individual WavePair.

    properties = Bar.verticalMplNames.keys()
    properties.append('orientation')

    def __init__(self, plotOptionsWidget, *args):
        QCartesianPlotWavePairsWidget.__init__(self, plotOptionsWidget, *args)

    def initSubWidgets(self):
        self.getChild('fillColor').initButtonColor()
        self.getChild('edgeColor').initButtonColor()

        QCartesianPlotWavePairsWidget.initSubWidgets(self)

    def addWavePairsToPlot(self):
        QCartesianPlotWavePairsWidget.addWavePairsToPlot(self, Bar)

    def saveOptionsToWavePair(self, wavePair):
        """Reimplementing this to override the default action for the orientation property."""

        currentUi = self.getCurrentUi()
        orientation = currentUi.pop('orientation', 'vertical')

        # Set orientation for entire plot
        wavePair.plot().plotTypeObject.set('orientation', orientation)

        # Default action
        wavePair.setMultiple(currentUi)

    def setUiToWavePair(self, wavePair):
        """Reimplementing this to override the default action for the orientation property."""

        properties = copy.deepcopy(wavePair.properties)
        properties.update({'orientation': wavePair.plot().plotTypeObject.get('orientation')})
        self.setCurrentUi(properties)

