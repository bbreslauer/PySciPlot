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


from PySide.QtGui import QAction, QMenu, QWidget, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, QBrush, QColor, QComboBox
#from PySide.QtCore import QStringList

import os, csv

import Util
from Wave import Wave
from Module import Module
from gui.SubWindows import SubWindow
from ui.Ui_ImportCSV import Ui_ImportCSV

class ImportCSV(Module):
    """Module to import data as CSV (or TSV, etc)."""

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        self._widget = QWidget()
        self._ui = Ui_ImportCSV()
        self._ui.setupUi(self._widget)

        # Connect button signals
        self._ui.csvFileNameButton.clicked.connect(self.csvFileSelector)
        self._ui.loadDataButton.clicked.connect(self.loadData)
        self._ui.importDataButton.clicked.connect(self.importData)
        self._ui.data.cellChanged.connect(self.handleDataChange)

    def csvFileSelector(self):
        """Button-lineedit link"""
        directory = os.path.dirname(Util.getWidgetValue(self._ui.csvFileName))
        if not os.path.isdir(directory):
            directory = self._app.preferences.getInternal('projectDirectory')

        csvFile = str(QFileDialog.getOpenFileName(self._app.ui.workspace, "Select Data File", directory, "Comma Separated Values (*.csv);;All Files(*)")[0])

        if csvFile != "":
            return Util.setWidgetValue(self._ui.csvFileName, csvFile)
        return False

    def loadData(self):
        """Load data into the widget for viewing before importing into the application."""
        
        # Block the cellChanged signal, because all the cells are going to be changed and we
        # are dealing with that in this method.
        self._ui.data.blockSignals(True)

        dataTable = self._ui.data

        self.clearTable()

        # Get data from file
        csvFile = Util.getWidgetValue(self._ui.csvFileName)
        if os.path.isfile(csvFile):
            
            rows = []
            delimiterText = Util.getWidgetValue(self._ui.delimiterButtonGroup)
            if delimiterText == "Comma":
                rows = csv.reader(open(csvFile), dialect="excel", delimiter=",")
            elif delimiterText == "Tab":
                rows = csv.reader(open(csvFile), dialect="excel-tab")
            elif delimiterText == "Other":
                rows = csv.reader(open(csvFile), dialect="excel", delimiter=Util.getWidgetValue(self._ui.otherDelimiter))
            else:
                rows = csv.reader(open(csvFile), dialect="excel", delimiter=",")

            for rownum, row in enumerate(rows):
                # Make sure the cells exist to enter the data into
                dataTable.insertRow(rownum)
                if len(row) > dataTable.columnCount():
                    for i in range(dataTable.columnCount(), len(row)):
                        dataTable.insertColumn(dataTable.columnCount())
                # Add this row to the table
                for colnum, item in enumerate(row):
                    dataTable.setItem(rownum, colnum, QTableWidgetItem(item))
        
        # Hide the QT default column header, since we cannot edit it easily
        dataTable.horizontalHeader().hide()

        # Add a row for setting the data type of each wave
        dataTable.insertRow(0)
        defaultType = Util.getWidgetValue(self._ui.defaultDataType)
        for col in range(dataTable.columnCount()):
            typeBox = QComboBox()
            typeBox.addItem("Integer")
            typeBox.addItem("Decimal")
            typeBox.addItem("String")
            Util.setWidgetValue(typeBox, defaultType)
            dataTable.setCellWidget(0, col, typeBox)

        # Potential wave names
        waveNamePrefix = Util.getWidgetValue(self._ui.waveNamePrefix)
        tempWaveNames = []
        if Util.getWidgetValue(self._ui.useWaveNamePrefix):
            tempWaveNames = self._app.waves().findGoodWaveNames(dataTable.columnCount(), waveNamePrefix)
        else:
            tempWaveNames = self._app.waves().findGoodWaveNames(dataTable.columnCount())

        # Wave names can either be generated or taken from the first row in the file
        if not Util.getWidgetValue(self._ui.firstRowWaveNames):
            # Generate headers
            dataTable.insertRow(1)
            
            # PyQt does not have QList support yet, so this is a hack to get around that
            for col,name in enumerate(tempWaveNames):
                dataTable.setItem(1, col, QTableWidgetItem(name))
        else:
            # Use the first row of data, but check to see if there is text for each column
            # and if there is no text for a column, add in a tempWaveName entry
            for col in range(dataTable.columnCount()):
                if not dataTable.item(1, col) or str(dataTable.item(1, col).text()).strip() == "":
                    dataTable.setItem(1, col, QTableWidgetItem(tempWaveNames.pop(0)))
                else:
                    # For the names that came from the file, add the prefix specified by the user
                    if Util.getWidgetValue(self._ui.useWaveNamePrefix):
                        dataTable.item(1, col).setText(str(waveNamePrefix) + dataTable.item(1, col).text())


        # Edit the name so that it could be valid (no spaces, etc). But it might
        # still be a duplicate.
        self.validateWaveNames()

        # Adjust the row headers so that they number correctly with the wave names in the first row
        #rowLabels = QStringList("Type")
        rowLabels = ["Type"]
        rowLabels.append("Name")
        for row in range(1, dataTable.rowCount()):
            rowLabels.append(str(row))
        dataTable.setVerticalHeaderLabels(rowLabels)

        # Verify that all wave names are acceptable for the app's waves object
        self.verifyGoodWaveNames()

        self._ui.data.blockSignals(False)

        # Resize rows and columns
        dataTable.resizeRowsToContents()
        dataTable.resizeColumnsToContents()

    def clearTable(self):
        dataTable = self._ui.data

        # Reset table to be empty
        for i in range(dataTable.rowCount()):
            dataTable.removeRow(0)
        for i in range(dataTable.columnCount()):
            dataTable.removeColumn(0)

    def validateWaveNames(self):
        """
        Run Wave.validateWaveName on all potential wave names.
        """

        dataTable = self._ui.data

        for col in range(dataTable.columnCount()):
            if dataTable.item(1, col):
                dataTable.setItem(1, col, QTableWidgetItem(Wave.validateWaveName(str(dataTable.item(1, col).text()))))

    def verifyGoodWaveNames(self):
        """
        Verify that all the wave names provided will be acceptable in the application's waves object.
        If there are any conflicts, then disable importing and mark the offending names.
        """
        
        dataTable = self._ui.data
        
        allNamesAreGood = True
        importWaveNames = []

        for col in range(dataTable.columnCount()):
            if dataTable.item(1, col):
                name = str(dataTable.item(1, col).text())
                if name in importWaveNames or not self._app.waves().goodWaveName(name):
                    # Bad name, highlight
                    dataTable.item(1, col).setBackground(QBrush(QColor('red')))
                    allNamesAreGood = False
                else:
                    # Good name
                    dataTable.item(1, col).setBackground(QBrush(QColor('lightgreen')))
                importWaveNames.append(name)

        # Disable the import button
        if allNamesAreGood:
            self._ui.importDataButton.setEnabled(True)
        else:
            self._ui.importDataButton.setEnabled(False)

        return allNamesAreGood

    def handleDataChange(self, row, column):
        """
        If data in a cell is changed, then this method will be called.

        Currently, if a name cell is edited, then we re-verify the wave names.
        """

        if row == 1:
            self.verifyGoodWaveNames()

    def importData(self):
        """Import data into the application as waves."""
        
        dataTable = self._ui.data
        
        # Loop through all waves
        for col in range(dataTable.columnCount()):
            dataType = Util.getWidgetValue(dataTable.cellWidget(0, col))
            wave = Wave(str(dataTable.item(1, col).text()), dataType)
            for row in range(2, dataTable.rowCount()):
                if dataTable.item(row, col):
                    wave.push(str(dataTable.item(row, col).text()))
                else:
                    wave.push('')
            self._app.waves().addWave(wave)

        # Close window
        self.clearTable()
        self.window.hide()


    def load(self):
        self.window = SubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionImportCSV")
        self.menuEntry.setShortcut("Ctrl+I")
        self.menuEntry.setText("Import CSV Data")
        self.menuEntry.triggered.connect(self.show)
        
        # Check if menu already exists
        if "menuImport" not in vars(self._app.ui).keys():
            self._app.ui.menuImport = QMenu(self._app.ui.menuFile)
            self._app.ui.menuImport.setObjectName("menuImport")
            self._app.ui.menuImport.setTitle(QApplication.translate("MainWindow", "Import", None, QApplication.UnicodeUTF8))
            self._app.ui.menuFile.addAction(self._app.ui.menuImport.menuAction())
        
        self.menu = vars(self._app.ui)["menuImport"]
        self.menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)

    def setDefaults(self):
        for child in self._widget.children():
            print child
            del child
        self._ui.setupUi(self._widget)

