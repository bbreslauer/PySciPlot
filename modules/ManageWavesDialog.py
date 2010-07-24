from PyQt4.QtGui import QWidget, QAction, QMessageBox, QItemSelection, QDialogButtonBox
from PyQt4.QtCore import Qt

import Util
from Wave import Wave
from DialogSubWindow import DialogSubWindow
from models.WavesListModel import WavesListModel
from modules.Module import Module
from ui.Ui_ManageWavesDialog import Ui_ManageWavesDialog

class ManageWavesDialog(Module):
    """Module to display the Manage Waves dialog window."""

    def __init__(self, app):
        Module.__init__(self, app)

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._widget = QWidget()
        self._ui = Ui_ManageWavesDialog()
        self._ui.setupUi(self._widget)
        
        # Set up model and view
        self._wavesListModel = WavesListModel(self._app.waves())
        self._ui.wavesListView.setModel(self._wavesListModel)

        # Connect some slots
        self._app.waves().waveAdded.connect(self._wavesListModel.doReset)
        self._app.waves().waveRemoved.connect(self._wavesListModel.doReset)
        self._ui.wavesListView.selectionModel().currentChanged.connect(self.updateWaveOptionsUi)
        self._ui.waveOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.updateWaveOptionsUi)
        self._ui.waveOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.applyWaveOptions)
        
        # Define handler functions
        def addWave():
            """Add a wave to the list of all waves in the main window."""

            name = str(self._ui.waveNameLineEdit.text())
            if Wave.validateWaveName(name) == "":
                failedMessage = QMessageBox()
                failedMessage.setText("Name cannot be blank")
                failedMessage.exec_()
            else:
                newWave = Wave(name)
                newWave.setDataType(Util.getWidgetValue(self._ui.dataType))
                if not self._app.waves().addWave(newWave):
                    failedMessage = QMessageBox()
                    failedMessage.setText("Name already exists: " + name)
                    failedMessage.exec_()
            self._ui.waveNameLineEdit.setText("")
        def removeWaves():
            """Remove waves from the list of all waves in the main window."""
            wavesToRemove = []

            # Get all the waves first then remove them.  Otherwise the indices change as
            # we are removing waves.
            for index in self._ui.wavesListView.selectedIndexes():
                wavesToRemove.append(self._app.waves().waves()[index.row()])
            for wave in wavesToRemove:
                self._app.waves().removeWave(wave.name())
        def closeWindow():
            self._widget.parent().close()
            
        # Connect buttons to handler functions
        self._ui.waveNameLineEdit.returnPressed.connect(addWave)
        self._ui.createWaveButton.clicked.connect(addWave)
        self._ui.removeWaveButton.clicked.connect(removeWaves)
        self._ui.closeButton.clicked.connect(closeWindow)

        return self._widget

    def updateWaveOptionsUi(self, *args):
        """
        Update the wave options based on the current wave.  This slot will be
        called whenever the selection has changed.
        """

        if self._ui.wavesListView.currentIndex():
            waveDataType = self._app.waves().getWaveByName(str(self._ui.wavesListView.currentIndex().data().toString())).dataType()
            Util.setWidgetValue(self._ui.dataType, waveDataType)

    def applyWaveOptions(self):
        """
        Set the selected waves to have the currently-selected options.
        """

        # Make sure user wants to actually change the data type
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

        if self._ui.wavesListView.selectedIndexes():
            for index in self._ui.wavesListView.selectedIndexes():
                wave = self._app.waves().getWaveByName(str(index.data().toString()))
                wave.setDataType(Util.getWidgetValue(self._ui.dataType))

        return True



    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionManageWavesDialog")
        self.menuEntry.setShortcut("Ctrl+V")
        self.menuEntry.setText("Manage Waves")
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
        self._app.waves().waveRemoved.disconnect(self._wavesListModel.doReset)
        self.menuEntry.triggered.disconnect()

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)




