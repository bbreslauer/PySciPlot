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


from PySide.QtGui import QWidget, QAction, QMessageBox, QItemSelection, QDialogButtonBox, QItemSelectionModel
from PySide.QtCore import Qt

import re
from math import *
from numpy import *

import Util
from Wave import Wave
from gui.SubWindows import SubWindow
from modules.Module import Module
from ui.Ui_ManageWavesWidget import Ui_ManageWavesWidget

class ManageWavesWidget(Module):
    """Module to display the Manage Waves dialog window."""

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._widget = QWidget()
        self._ui = Ui_ManageWavesWidget()
        self._ui.setupUi(self._widget)
        
        self.setModels()

        # Connect some slots
        self._ui.copyWaveOriginalWave.activated.connect(self.resetCopyWaveLimits)
        self._ui.createWaveButton.clicked.connect(self.createWave)
        self._ui.functionInsertWaveButton.clicked.connect(self.insertWaveIntoFunction)

        self._ui.modifyWave_selectWave.selectionModel().currentChanged.connect(self.updateModifyWaveUi)
        self._ui.removeWaveButton.clicked.connect(self.removeWave)
        self._ui.resetWaveButton.clicked.connect(self.updateModifyWaveUi)
        self._ui.modifyWaveButton.clicked.connect(self.modifyWave)

        # Make sure selection list and stack are aligned
        self._ui.waveDataSelectionList.setCurrentRow(0)
        self._ui.waveDataStack.setCurrentIndex(0)

        return self._widget

    def setModels(self):
        # Set up model and views
        self._wavesListModel = self._app.model('appWaves')
        self._ui.copyWaveOriginalWave.setModel(self._wavesListModel)
        self._ui.functionInsertWave.setModel(self._wavesListModel)
        self._ui.modifyWave_selectWave.setModel(self._wavesListModel)

    ####
    # Create Wave tab
    ####
    def createWave(self):
        """
        Create the wave, using whatever starting point (basic, copy, function, etc) is necessary.
        """

        # Check if the wave is unique in the application
        if not self._app.waves().goodWaveName(Util.getWidgetValue(self._ui.createWave_waveName)):
            warningMessage = QMessageBox()
            warningMessage.setWindowTitle("Error!")
            warningMessage.setText("The name you chose has already been used. Please enter a new name.")
            warningMessage.setIcon(QMessageBox.Critical)
            warningMessage.setStandardButtons(QMessageBox.Ok)
            warningMessage.setDefaultButton(QMessageBox.Ok)
            result = warningMessage.exec_()
            return False

        wave = Wave(Util.getWidgetValue(self._ui.createWave_waveName), Util.getWidgetValue(self._ui.createWave_dataType))
        
        # Check how the wave should be initially populated
        initialWaveDataTab = self._ui.waveDataStack.currentWidget().objectName()

        if initialWaveDataTab == "basicTab":
            # Basic wave. Need to determine the type
            basicWaveType = Util.getWidgetValue(self._ui.basicWaveType)
            if basicWaveType == "Blank":
                pass
            elif basicWaveType == "Index (starting at 0)":
                basicWaveLength = Util.getWidgetValue(self._ui.basicWaveLength)
                wave.extend(range(0, basicWaveLength))
            elif basicWaveType == "Index (starting at 1)":
                basicWaveLength = Util.getWidgetValue(self._ui.basicWaveLength)
                wave.extend(range(1, basicWaveLength+1))

        elif initialWaveDataTab == "copyTab":
            # Copy the data from another wave
            originalWave = self._ui.copyWaveOriginalWave.model().index(self._ui.copyWaveOriginalWave.currentIndex(), 0).internalPointer()
            startingIndex = Util.getWidgetValue(self._ui.copyWaveStartingIndex)
            endingIndex = Util.getWidgetValue(self._ui.copyWaveEndingIndex)
            wave.extend(originalWave.data(startingIndex, endingIndex))

        elif initialWaveDataTab == "functionTab":
            waveLength = Util.getWidgetValue(self._ui.functionWaveLength)
            functionString = Util.getWidgetValue(self._ui.functionEquation)
            data = self.parseFunction(waveLength, functionString)
            wave.extend(data)
        

        # Add wave to application
        self._app.waves().addWave(wave)

        # Reset certain ui fields
        self._ui.copyWaveOriginalWave.setCurrentIndex(0)
        self._ui.functionInsertWave.setCurrentIndex(0)

    def resetCopyWaveLimits(self, null=None):
        """
        Reset the spin boxes for selecting the data limits to the current wave's max values.
        """
        wave = self._ui.copyWaveOriginalWave.model().index(self._ui.copyWaveOriginalWave.currentIndex(), 0).internalPointer()
        maxIndex = wave.length()
        self._ui.copyWaveStartingIndex.setMaximum(maxIndex)
        self._ui.copyWaveEndingIndex.setMaximum(maxIndex)
        Util.setWidgetValue(self._ui.copyWaveEndingIndex, maxIndex)

    def parseFunction(self, waveLength, functionString):
        """
        Parse the function string into an actual function and return the data
        for the wave. Any python math and numpy functions are allowed.

        Special values:
        w_name - the wave with name 'name'
        s_val  - a special value, see the list below

        s_ values:
            s_index - 0-based row index
            s_oneindex - 1-based row index 
        """

        specialValuesList = Util.uniqueList(re.findall('s_\w*', functionString))
        specialValuesString = str.join(', ', specialValuesList)
        
        wavesList = Util.uniqueList(re.findall('w_\w*', functionString))
        wavesString = str.join(', ', wavesList)
        
        specialValuesAndWavesList = Util.uniqueList(re.findall('[s|w]_\w*', functionString))
        specialValuesAndWavesString = str.join(', ', specialValuesAndWavesList)
        
        # First, let's check if this is a simple function that can be performed completely
        # with built-ins, in which case we don't need to worry about getting any special
        # values and waves
        if len(specialValuesAndWavesList) == 0:
            return eval(functionString)

        # Need to create the lambda string first so that we can expand all
        # the arguments to the lambda before creating the actual anonymous
        # function.
        function = eval('lambda ' + specialValuesAndWavesString + ': eval(\'' + str(functionString) + '\')')
        
        # Determine the length of the smallest wave, so that we don't apply the function past that
        waveLengths = []
        if waveLength > 0:
            waveLengths.append(waveLength)
        for waveName in wavesList:
            waveNameNoPrefix = waveName[2:]
            waveLengths.append(len(self._app.waves().wave(waveNameNoPrefix).data()))
        
        if len(waveLengths) == 0:
            waveLength = 0
        else:
            waveLength = min(waveLengths)

        # Define s_ values
        s_index = range(waveLength)
        s_oneindex = range(1, waveLength + 1)

        # Define waves that are used in the function
        for waveName in wavesList:
            waveNameNoPrefix = waveName[2:]
            exec(str(waveName) + ' = ' + str(self._app.waves().wave(waveNameNoPrefix).data()[:waveLength]))

        # Apply the function
        data = eval('map(function, ' + specialValuesAndWavesString + ')')

        return data

    def insertWaveIntoFunction(self):
        """
        Take the wave from functionInsertWave and insert it into the function definition.
        """

        waveName = self._ui.functionInsertWave.model().index(self._ui.functionInsertWave.currentIndex(), 0).internalPointer().name()
        self._ui.functionEquation.insert("w_" + str(waveName))
        return True


    ####
    # Modify/Remove Wave tab
    ####
    def updateModifyWaveUi(self, *args):
        """
        Update the wave options based on the current wave.  This slot will be
        called whenever the selection has changed.
        """

        if self._ui.modifyWave_selectWave.currentIndex():
            wave = self._wavesListModel.waveByRow(self._ui.modifyWave_selectWave.currentIndex().row())

            if wave:
                Util.setWidgetValue(self._ui.modifyWave_waveName, wave.name())
                Util.setWidgetValue(self._ui.modifyWave_dataType, wave.dataType())

    def modifyWave(self):
        """
        Set the selected wave to have the currently-selected options.
        """

        currentIndex = self._ui.modifyWave_selectWave.currentIndex()
        if currentIndex:
            wave = self._wavesListModel.waveByRow(self._ui.modifyWave_selectWave.currentIndex().row())
            
            # Make sure the user wants to change the wave's name
            if wave.name() != Util.getWidgetValue(self._ui.modifyWave_waveName) and not self._app.waves().goodWaveName(Util.getWidgetValue(self._ui.modifyWave_waveName)):
                warningMessage = QMessageBox()
                warningMessage.setWindowTitle("Error!")
                warningMessage.setText("You are trying to change the wave name, but the one you have chosen has already been used. Please enter a new name.")
                warningMessage.setIcon(QMessageBox.Critical)
                warningMessage.setStandardButtons(QMessageBox.Ok)
                warningMessage.setDefaultButton(QMessageBox.Ok)
                result = warningMessage.exec_()
                return False

            # Make sure the user wants to actually change the data type
            if wave.dataType() != Util.getWidgetValue(self._ui.modifyWave_dataType):
                warningMessage = QMessageBox()
                warningMessage.setWindowTitle("Warning!")
                warningMessage.setText("If you change the data type, then you may lose data if it cannot be properly converted.")
                warningMessage.setInformativeText("Are you sure you want to continue?")
                warningMessage.setIcon(QMessageBox.Warning)
                warningMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                warningMessage.setDefaultButton(QMessageBox.No)
                result = warningMessage.exec_()

                if result != QMessageBox.Yes:
                    return False

            # All warnings have been accepted, so we can continue with actually modifying the wave
            wave.setName(Util.getWidgetValue(self._ui.modifyWave_waveName))
            wave.setDataType(Util.getWidgetValue(self._ui.modifyWave_dataType))

            self._ui.modifyWave_selectWave.setCurrentIndex(currentIndex)

        return True

    def removeWave(self):
        """Remove wave from the list of all waves in the main window."""
        wavesToRemove = []
        
        currentIndex = self._ui.modifyWave_selectWave.currentIndex()
        row = currentIndex.row()
        if currentIndex:
            warningMessage = QMessageBox()
            warningMessage.setWindowTitle("Warning!")
            warningMessage.setText("You are about to delete a wave.")
            warningMessage.setInformativeText("Are you sure you want to continue?")
            warningMessage.setIcon(QMessageBox.Warning)
            warningMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            warningMessage.setDefaultButton(QMessageBox.No)
            result = warningMessage.exec_()

            if result != QMessageBox.Yes:
                return False

            # Determine the next row to select
            newRow = row
            if row >= self._wavesListModel.rowCount() - 1:
                newRow = row - 1
            
            self._app.waves().removeWave(self._wavesListModel.waveNameByRow(row))
            self._ui.modifyWave_selectWave.setCurrentIndex(self._wavesListModel.index(newRow))
            self._ui.modifyWave_selectWave.selectionModel().select(self._wavesListModel.index(newRow), QItemSelectionModel.ClearAndSelect)

    def load(self):
        self.window = SubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionManageWavesWidget")
        self.menuEntry.setText("Manage Waves")
        self.menuEntry.triggered.connect(self.show)
        self.menu = vars(self._app.ui)["menuData"]
        self.menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):
        # Disconnect some slots
        self.menuEntry.triggered.disconnect()

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)

    def reload(self):
        self.setModels()



