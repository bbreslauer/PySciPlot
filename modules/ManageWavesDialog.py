from PyQt4.QtGui import QWidget

from Wave import Wave
from models.WavesListModel import WavesListModel
from modules.Module import Module
from ui.Ui_ManageWavesDialog import Ui_ManageWavesDialog

class ManageWavesDialog(Module):
    """Module to display the Manage Waves dialog window."""

    def __init__(self, app):
        self._widget = QWidget()
        self._app = app
        self.buildWidget()

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._ui = Ui_ManageWavesDialog()
        self._ui.setupUi(self._widget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        self._widget.setLayout(self._ui.horizontalLayout)

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
            newWave = Wave(name)
            if not self._app.waves().addWave(newWave):
                failedMessage = QtGui.QMessageBox()
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

    def getMenuNameToAddTo(self):
        return "menuData"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionManageWavesDialog")
        menu.setShortcut("Ctrl+V")
        menu.setText("Manage Waves")
        return menu


