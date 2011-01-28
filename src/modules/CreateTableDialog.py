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


from PyQt4.QtGui import QWidget, QAction, QMessageBox
from PyQt4.QtCore import Qt

import Util
from Wave import Wave
from gui.SubWindows import SubWindow
from models.WavesListModel import WavesListModel
from modules.Module import Module
from ui.Ui_CreateTableDialog import Ui_CreateTableDialog

class CreateTableDialog(Module):
    """Module to display the Create Table dialog window."""

    def __init__(self):
        Module.__init__(self)

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
        self.resetForm()
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
        if len(waves) == 0:
            warningMessage = QMessageBox()
            warningMessage.setWindowTitle("Problem!")
            warningMessage.setText("You must select at least one wave in order to create a table.")
            warningMessage.setIcon(QMessageBox.Critical)
            warningMessage.setStandardButtons(QMessageBox.Ok)
            warningMessage.setDefaultButton(QMessageBox.Ok)
            result = warningMessage.exec_()
            return False

        names = map(Wave.getName, waves)
        self._app.createTable(waves, tableName)
        self.closeWindow()
        return True

    def resetForm(self):
        Util.setWidgetValue(self._ui.tableName, "Table")
        self._allWavesListModel.doReset()
        self._tableWavesListModel.removeAllWaves()
        self._tableWavesListModel.doReset()

    def load(self):
        self.window = SubWindow(self._app.ui.workspace)

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

