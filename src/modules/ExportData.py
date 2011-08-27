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


from PySide.QtGui import QWidget, QAction, QFileDialog, QMessageBox

import os, csv

import Util
from Module import Module
from models.WavesListModel import WavesListModel
from gui.SubWindows import SubWindow
from ui.Ui_ExportData import Ui_ExportData

class ExportData(Module):
    """Module to export data in any format."""

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        self._widget = QWidget()
        self._ui = Ui_ExportData()
        self._ui.setupUi(self._widget)

        self.setModels()

        # Connect button signals
        self._ui.fileNameButton.clicked.connect(self.fileSelector)
        self._ui.addWaveButton.clicked.connect(self.addWave)
        self._ui.removeWaveButton.clicked.connect(self.removeWave)
        self._ui.exportDataButton.clicked.connect(self.exportData)

    def setModels(self):
        # Set up model and view
        self._allWavesListModel = self._app.model('appWaves')
        self._ui.allWavesListView.setModel(self._allWavesListModel)
        self._fileWavesListModel = WavesListModel([])
        self._ui.fileWavesListView.setModel(self._fileWavesListModel)

    def fileSelector(self):
        """Button-lineedit link"""
        directory = os.path.dirname(Util.getWidgetValue(self._ui.fileName))
        if not os.path.isdir(directory):
            directory = self._app.preferences.getInternal('projectDirectory')

        fileName = str(QFileDialog.getOpenFileName(self._app.ui.workspace, "Select Data File", directory, "All Files(*)")[0])

        if fileName != "":
            return Util.setWidgetValue(self._ui.fileName, fileName)
        return False

    def addWave(self):
        selectedIndexes = self._ui.allWavesListView.selectedIndexes()
        for index in selectedIndexes:
            self._fileWavesListModel.appendRow(self._allWavesListModel.waveNameByRow(index.row()))

    def removeWave(self):
        selectedIndexes = self._ui.fileWavesListView.selectedIndexes()
        selectedRows = map(lambda x:x.row(), selectedIndexes)
        selectedRows.sort()
        selectedRows.reverse()
        for row in selectedRows:
            self._fileWavesListModel.removeRow(row)

    def exportData(self):
        fileName = Util.getWidgetValue(self._ui.fileName)

        if os.path.exists(fileName):
            if os.path.isfile(fileName):
                # Ask about overwriting
                warningMessage = QMessageBox()
                warningMessage.setWindowTitle("Warning!")
                warningMessage.setText("The filename you have chosen - " + str(fileName) + " - already exists.")
                warningMessage.setInformativeText("Do you want to overwrite the file?")
                warningMessage.setIcon(QMessageBox.Warning)
                warningMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                warningMessage.setDefaultButton(QMessageBox.No)
                result = warningMessage.exec_()

                if result != QMessageBox.Yes:
                    return False
            else:
                # Do not try to overwrite a directory or link
                return False
        
        # Get waves
        waveNames = self._ui.fileWavesListView.model().orderedWaveNames()
        
        with open(fileName, 'w') as fileHandle:
            if Util.getWidgetValue(self._ui.outputType) == 'Delimited':
                delimiterText = Util.getWidgetValue(self._ui.delimiterButtonGroup)
                if delimiterText == 'Comma':
                    fileWriter = csv.writer(fileHandle, dialect="excel", delimiter=",")
                elif delimiterText == 'Tab':
                    fileWriter = csv.writer(fileHandle, dialect="excel-tab")
                elif delimiterText == 'Other':
                    fileWriter = csv.writer(fileHandle, dialect="excel", delimiter=Util.getWidgetValue(self._ui.delimitedOtherDelimiter))
                else:
                    fileWriter = csv.writer(fileHandle, dialect="excel", delimiter=",")
    
                dataDirection = Util.getWidgetValue(self._ui.dataDirectionButtonGroup)
                
                rows = []
                for waveName in waveNames:
                    wave = self._app.waves().wave(waveName)
                    row = wave.data()
                    row.insert(0, wave.name())
                    rows.append(row)

                if dataDirection == "Rows":
                    fileWriter.writerows(rows)
                elif dataDirection == "Columns":
                    # Transpose the rows into columns
                    columns = map(lambda *row: ['' if elem is None else elem for elem in row], *rows)
                    fileWriter.writerows(columns)

    def load(self):
        self.window = SubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionExportData")
        self.menuEntry.setShortcut("Ctrl+E")
        self.menuEntry.setText("Export Data")
        self.menuEntry.triggered.connect(self.show)

        # Check if menu already exists
        if "menuExport" not in vars(self._app.ui).keys():
            self._app.ui.menuExport = QMenu(self._app.ui.menuFile)
            self._app.ui.menuExport.setObjectName("menuExport")
            self._app.ui.menuExport.setTitle(QApplication.translate("MainWindow", "Export", None, QApplication.UnicodeUTF8))
            self._app.ui.menuFile.addAction(self._app.ui.menuExport.menuAction())
        
        self.menu = vars(self._app.ui)["menuExport"]
        self.menu.addAction(self.menuEntry)
        
        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)

    def reload(self):
        self.setModels()

