from PyQt4.QtGui import QWidget, QAction
from PyQt4.QtCore import Qt

import re
from math import *
from numpy import *

import Util
from Wave import Wave
from DialogSubWindow import DialogSubWindow
from models.WavesListModel import WavesListModel
from modules.Module import Module
from ui.Ui_CreateWaveDialog import Ui_CreateWaveDialog

class CreateWaveDialog(Module):
    """Module to display the Create Wave dialog window."""

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._widget = QWidget()
        self._ui = Ui_CreateWaveDialog()
        self._ui.setupUi(self._widget)
        
        # Set up model and view
        self._wavesListModel = WavesListModel(self._app.waves())
        self._ui.copyWaveOriginalWave.setModel(self._wavesListModel)
        self._ui.functionInsertWave.setModel(self._wavesListModel)

        # Connect some slots
        self._app.waves().waveAdded.connect(self._wavesListModel.doReset)
        self._app.waves().waveRemoved[Wave].connect(self._wavesListModel.doReset)
        self._ui.copyWaveOriginalWave.activated.connect(self.resetCopyWaveLimits)
        self._ui.createWaveButton.clicked.connect(self.createWave)
        self._ui.closeWindowButton.clicked.connect(self.closeWindow)
        self._ui.functionInsertWaveButton.clicked.connect(self.insertWaveIntoFunction)

        # Make sure selection list and stack are aligned
        self._ui.waveDataSelectionList.setCurrentRow(0)
        self._ui.waveDataStack.setCurrentIndex(0)

    def closeWindow(self):
        self._widget.parent().close()


    def createWave(self):
        """
        Create the wave, using whatever starting point (basic, copy, function, etc) is necessary.
        """

        # Check if the wave is unique in the application
        if not self._app.waves().goodWaveName(Util.getWidgetValue(self._ui.waveName)):
            warningMessage = QMessageBox()
            warningMessage.setWindowTitle("Error!")
            warningMessage.setText("The name you chose has already been used. Please enter a new name.")
            warningMessage.setIcon(QMessageBox.Critical)
            warningMessage.setStandardButtons(QMessageBox.Ok)
            warningMessage.setDefaultButton(QMessageBox.Ok)
            result = warningMessage.exec_()
            return False

        wave = Wave(Util.getWidgetValue(self._ui.waveName), Util.getWidgetValue(self._ui.dataType))
        
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
            waveLengths.append(len(self._app.waves().getWaveByName(waveNameNoPrefix).data()))
        
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
            exec(str(waveName) + ' = ' + str(self._app.waves().getWaveByName(waveNameNoPrefix).data()[:waveLength]))

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



    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionCreateWaveDialog")
        self.menuEntry.setShortcut("Ctrl+W")
        self.menuEntry.setText("Create Waves")
        self.menuEntry.triggered.connect(self.window.show)
        self.menu = vars(self._app.ui)["menuData"]
        self.menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):
        # Disconnect some slots
        self._app.waves().waveAdded.disconnect(self._wavesListModel.doReset)
        self._app.waves().waveRemoved[Wave].disconnect(self._wavesListModel.doReset)
        self.menuEntry.triggered.disconnect()

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)






