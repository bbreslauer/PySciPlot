from PyQt4.QtGui import QWidget, QAction, QMessageBox

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
        wavesListModel = WavesListModel(self._app.waves())
        self._ui.wavesListView.setModel(wavesListModel)

        # Connect some slots
        self._app.waves().waveAdded.connect(wavesListModel.doReset)
        self._app.waves().waveRemoved.connect(wavesListModel.doReset)
        
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

    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)
        self._app.ui.workspace.addSubWindow(self.window)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionManageWavesDialog")
        self.menuEntry.setShortcut("Ctrl+V")
        self.menuEntry.setText("Manage Waves")
        self.menuEntry.triggered.connect(self.window.show)
        menu = getattr(self._app.ui, "menuData")
        menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):
        self._widget.destroy()
        self.window.destroy()




