from PyQt4.QtGui import QAction, QMenu, QWidget, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, QBrush, QColor, QComboBox, QMessageBox

import os, csv, array, struct

import Util
from Wave import Wave
from Module import Module
from DialogSubWindow import DialogSubWindow
from ui.Ui_ImportBinary import Ui_ImportBinary

class ImportBinary(Module):
    """Module to import data from a binary file."""

    dataTypes = {   'Signed Integer (1)':     { 'dtype': 'Integer', 'char': 'b', 'numbytes': 1 },
                    'Unsigned Integer (1)':   { 'dtype': 'Integer', 'char': 'B', 'numbytes': 1 },
                    'Short (2)':              { 'dtype': 'Integer', 'char': 'h', 'numbytes': 2 },
                    'Unsigned Short (2)':     { 'dtype': 'Integer', 'char': 'H', 'numbytes': 2 },
                    'Integer (4)':            { 'dtype': 'Integer', 'char': 'i', 'numbytes': 4 },
                    'Unsigned Integer (4)':   { 'dtype': 'Integer', 'char': 'I', 'numbytes': 4 },
                    'Long (8)':               { 'dtype': 'Integer', 'char': 'l', 'numbytes': 8 },
                    'Unsigned Long (8)':      { 'dtype': 'Integer', 'char': 'L', 'numbytes': 8 },
                    'Float (4)':              { 'dtype': 'Decimal', 'char': 'f', 'numbytes': 4 },
                    'Double (8)':             { 'dtype': 'Decimal', 'char': 'd', 'numbytes': 8 },
                }

    byteOrders = {  'Native': '@',
                    'Big Endian': '>',
                    'Little Endian': '<',
                    'Network': '!',
                 }

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        self._widget = QWidget()
        self._ui = Ui_ImportBinary()
        self._ui.setupUi(self._widget)

        # Connect button signals
        self._ui.fileNameButton.clicked.connect(self.fileSelector)
        self._ui.importDataButton.clicked.connect(self.importData)

    def fileSelector(self):
        """Button-lineedit link"""
        directory = os.path.dirname(Util.getWidgetValue(self._ui.fileName))
        if not os.path.isdir(directory):
            directory = self._app.preferences.getInternal('projectDirectory')

        fileName = str(QFileDialog.getOpenFileName(self._app.ui.workspace, "Select Data File", directory, "Binary (*.bin *.dat);;All Files(*.*)"))

        if fileName != "":
            return Util.setWidgetValue(self._ui.fileName, fileName)
        return False


    def importData(self):
        """Import data into the application as waves."""
        
        # Check if the proposed wave name is acceptable
        validatedWaveName = Wave.validateWaveName(Util.getWidgetValue(self._ui.waveName))
        if not self._app.waves().goodWaveName(validatedWaveName):
            badWaveNameMessage = QMessageBox()
            badWaveNameMessage.setText("Wave name is not allowed or already in use.  Please change the wave name.")
            badWaveNameMessage.exec_()
            return False

        # Get data type and size
        uiDataType = Util.getWidgetValue(self._ui.dataType)
        uiByteOrder = Util.getWidgetValue(self._ui.byteOrder)
        dataType = self.dataTypes[uiDataType]['dtype']
        dataTypeChar = self.dataTypes[uiDataType]['char']
        numBytes = self.dataTypes[uiDataType]['numbytes']
        byteOrder = self.byteOrders[uiByteOrder]

        # Load data
        fileName = Util.getWidgetValue(self._ui.fileName)
        if os.path.isfile(fileName):
            data = []
            wave = Wave(str(validatedWaveName), dataType)
            self._app.waves().addWave(wave)

            fh = open(fileName, 'rb')
            binDatum = fh.read(numBytes)
            while binDatum != "":
                try:
                    datum = struct.unpack(byteOrder + dataTypeChar, binDatum)
                    wave.push(datum[0])
                except:
                    pass
                binDatum = fh.read(numBytes)

            




#            data = array.array(dataTypeChar)
#            numDataPoints = os.path.getsize(fileName) / data.itemsize
#            fh = open(fileName, 'rb')
#            data.fromfile(fh, numDataPoints)
#
#            wave = Wave(str(validatedWaveName), dataType)
#            wave.replaceData(data)
#            self._app.waves().addWave(wave)

        # Close window
        self.window.hide()







    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionImportBinary")
        self.menuEntry.setShortcut("Ctrl+B")
        self.menuEntry.setText("Import Binary Data")
        self.menuEntry.triggered.connect(self.window.show)
        
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



