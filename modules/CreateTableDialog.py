from PyQt4.QtGui import QWidget, QAction
from PyQt4.QtCore import Qt

import Util
from Wave import Wave
from DialogSubWindow import DialogSubWindow
from models.WavesListModel import WavesListModel
from modules.Module import Module
from ui.Ui_CreateTableDialog import Ui_CreateTableDialog

class CreateTableDialog(Module):
    """Module to display the Create Table dialog window."""

    def __init__(self, app):
        Module.__init__(self, app)

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._widget = QWidget()
        self._ui = Ui_CreateTableDialog()
        self._ui.setupUi(self._widget)
        
        # Set up model and view
        self._allWavesListModel = WavesListModel(self._app.waves())
        self._ui.allWavesListView.setModel(self._allWavesListModel)
        self._tableWavesListModel = WavesListModel()
        self._ui.tableWavesListView.setModel(self._tableWavesListModel)

        # Connect some slots
        self._app.waves().waveAdded.connect(self._allWavesListModel.doReset)
        self._app.waves().waveRemoved[Wave].connect(self._allWavesListModel.doReset)
        self._ui.createTableButton.clicked.connect(self.createTable)
        self._ui.closeWindowButton.clicked.connect(self.closeWindow)
        self._ui.addWaveButton.clicked.connect(self.addWaveToTable)
        self._ui.removeWaveButton.clicked.connect(self.removeWaveFromTable)

    def closeWindow(self):
        self.resetLists()
        self._widget.parent().close()


    def addWaveToTable(self):
        selectedIndexes = self._ui.allWavesListView.selectedIndexes()
        for index in selectedIndexes:
            self._tableWavesListModel.appendRow(self._allWavesListModel.waves().waves()[index.row()])

    def removeWaveFromTable(self):
        selectedIndexes = self._ui.tableWavesListView.selectedIndexes()
        names = []
        for index in selectedIndexes:
            names.append(self._tableWavesListModel.data(index))
        for name in names:
            self._tableWavesListModel.removeWave(name)

    def createTable(self):
        """
        Create the table.
        """

        tableName = Util.getWidgetValue(self._ui.tableName)
        waves = self._tableWavesListModel.waves().waves()
        names = map(Wave.getName, waves)
        self._app.createTable(waves, tableName)
        self.closeWindow()

    def resetLists(self):
        self._allWavesListModel.doReset()
        self._tableWavesListModel.removeAllWaves()
        self._tableWavesListModel.doReset()

    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionNewTableDialog")
        self.menuEntry.setShortcut("Ctrl+T")
        self.menuEntry.setText("New Table")
        self.menuEntry.triggered.connect(self.window.show)
        self.menu = vars(self._app.ui)["menuNew"]
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

