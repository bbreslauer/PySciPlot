import sys, string, signal

from PyQt4.QtGui import QMainWindow, QApplication, QMdiSubWindow, QWidget, QDialog
from PyQt4.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt4.QtCore import Qt

from Wave import Wave
from Waves import Waves
from WavesListModel import WavesListModel
from PlotListModel import PlotListModel
from PlotListEntry import PlotListEntry
from Figure import Figure
from DataTableView import DataTableView
from DataTableModel import DataTableModel
from DialogSubWindow import DialogSubWindow
from ui.MainWindow import Ui_MainWindow
from ui.ManageWavesDialog import Ui_ManageWavesDialog
from ui.EditFigureDialog import Ui_EditFigureDialog


class pysciplot2(QMainWindow):
    """
    This class initializes the PySciPlot program.
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self._waves = Waves()

        # Let the workspace resize when the main window is resized
        self.setCentralWidget(self.ui.workspace)

        # Dialog windows
        self.manageWavesDialogWidgetSubWindow = None
        
        # Make signal/slot connections
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionNew_Table.triggered.connect(self.createDefaultTable)
        self.ui.actionManage_Waves.triggered.connect(self.showManageWavesDialog)
        self.ui.actionEdit_Figure.triggered.connect(self.showEditFigureDialog)
        self.ui.actionShow_Waves.triggered.connect(self.printAllWaves)

        # create default waves
        self.setTestData()
        self.createDefaultTable()
        
    def waves(self):
        return self._waves

    def createDataTableView(self, tableModel):
        """
        Create a table view based on the given model.
        """

        tableView = DataTableView(tableModel, self, "Table", self)
        tableViewSubWindow = QMdiSubWindow()
        tableViewSubWindow.setWidget(tableView)
        tableViewSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.workspace.addSubWindow(tableViewSubWindow)

        tableViewSubWindow.setVisible(True)
        return tableView

    
    def showManageWavesDialog(self):
        """
        Show a dialog to manage waves.  Only one will be displayed at any given time.
        """

        # Check if dialog already exists
        if self.manageWavesDialogWidgetSubWindow != None:
            self.ui.workspace.setActiveSubWindow(self.manageWavesDialogWidgetSubWindow)
            self.manageWavesDialogWidgetSubWindow.show()
            return
        
        # Create enclosing widget and UI
        manageWavesDialogWidget = QWidget()
        manageWavesDialogUi = Ui_ManageWavesDialog()
        manageWavesDialogUi.setupUi(manageWavesDialogWidget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        manageWavesDialogWidget.setLayout(manageWavesDialogUi.horizontalLayout)
        
        # Set up model and view
        wavesListModel = WavesListModel(self._waves)
        manageWavesDialogUi.wavesListView.setModel(wavesListModel)

        # Connect some slots
        self._waves.waveAdded.connect(wavesListModel.doReset)
        self._waves.waveRemoved.connect(wavesListModel.doReset)
        
        # Show window
        self.manageWavesDialogWidgetSubWindow = DialogSubWindow(self.ui.workspace)
        self.manageWavesDialogWidgetSubWindow.setWidget(manageWavesDialogWidget)
        self.ui.workspace.addSubWindow(self.manageWavesDialogWidgetSubWindow)
        self.manageWavesDialogWidgetSubWindow.setVisible(True)
        
        # Define handler functions
        def addWave():
            """Add a wave to the list of all waves in the main window."""

            name = str(manageWavesDialogUi.waveNameLineEdit.text())
            newWave = Wave(name)
            if not self._waves.addWave(newWave):
                failedMessage = QtGui.QMessageBox()
                failedMessage.setText("Name already exists: " + name)
                failedMessage.exec_()
            manageWavesDialogUi.waveNameLineEdit.setText("")
        def removeWaves():
            """Remove waves from the list of all waves in the main window."""
            wavesToRemove = []

            # Get all the waves first then remove them.  Otherwise the indices change as
            # we are removing waves.
            for index in manageWavesDialogUi.wavesListView.selectedIndexes():
                wavesToRemove.append(self._waves.waves()[index.row()])
            for wave in wavesToRemove:
                self._waves.removeWave(wave.name())
        def closeWindow():
            self.manageWavesDialogWidgetSubWindow.close()
            
        # Connect buttons to handler functions
        manageWavesDialogUi.waveNameLineEdit.returnPressed.connect(addWave)
        manageWavesDialogUi.createWaveButton.clicked.connect(addWave)
        manageWavesDialogUi.removeWaveButton.clicked.connect(removeWaves)
        manageWavesDialogUi.closeButton.clicked.connect(closeWindow)

    def showEditFigureDialog(self):
        """Show a dialog to create or edit a figure."""

        # TODO: need to connect all sorts of signals
        # TODO: change editfiguredialog ui to what cat discussed
        # TODO: fix bug when plotting multiple waves

        # Create enclosing widget and UI
        editFigureDialogWidget = QDialog()
        editFigureDialogUi = Ui_EditFigureDialog()
        editFigureDialogUi.setupUi(editFigureDialogWidget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        editFigureDialogWidget.setLayout(editFigureDialogUi.gridLayout)
        
        # populate x and y axis lists
        xListModel = WavesListModel(self._waves)
        yListModel = WavesListModel(self._waves)
        editFigureDialogUi.xAxisListView.setModel(xListModel)
        editFigureDialogUi.yAxisListView.setModel(yListModel)
        
        # prepare plot list
        plotListModel = PlotListModel()
        editFigureDialogUi.plotListView.setModel(plotListModel)
        
        # show window
        editFigureDialogSubWindow = DialogSubWindow(self.ui.workspace)
        editFigureDialogSubWindow.setWidget(editFigureDialogWidget)
        self.ui.workspace.addSubWindow(editFigureDialogSubWindow)
        editFigureDialogSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        editFigureDialogSubWindow.show()
        
        def addPlotToList():
            xAxisIndexList = editFigureDialogUi.xAxisListView.selectedIndexes()
            yAxisIndexList = editFigureDialogUi.yAxisListView.selectedIndexes()
            plotNum = editFigureDialogUi.plotNumLineEdit.text().toInt()[0]
            
            for i in yAxisIndexList:
                xWave = self._waves.waves()[xAxisIndexList[0].row()]
                yWave = self._waves.waves()[i.row()]
                ple = PlotListEntry(xWave, yWave, plotNum)
                plotListModel.addPlotListEntry(ple)

                # Link wave name updates to list reset
                xWave.nameChanged.connect(plotListModel.doReset)
                yWave.nameChanged.connect(plotListModel.doReset)
        
        def makeFigure():
            nRows = editFigureDialogUi.numRowsLineEdit.text().toInt()[0]
            nCols = editFigureDialogUi.numColsLineEdit.text().toInt()[0]
            
            figure = Figure(nRows, nCols)
            
            figureSubWindow = QMdiSubWindow(self.ui.workspace)
            figureSubWindow.resize(450, 450)
            
            canvas = figure.getCanvas()
            canvas.setParent(figureSubWindow)
            figureSubWindow.setWidget(canvas)
            self.ui.workspace.addSubWindow(figureSubWindow)
            figureSubWindow.show()

            for ple in plotListModel.getAllPlotListEntries():
                figure.addPlotData(ple.getPlotNum(), ple.getX(), ple.getY())
            
            figure.makePlots()

            def updatePlots():
                figure.makePlots()

            # link wave updates to plot changes

            #self.connect(self, QtCore.SIGNAL("waveUpdated"), updatePlots)
        
            editFigureDialogSubWindow.close()
        
        def cancelFigure():
            editFigureDialogSubWindow.close()
        
        # Connect actions
        editFigureDialogUi.addPlotButton.clicked.connect(addPlotToList)
        editFigureDialogUi.buttonBox.accepted.connect(makeFigure)
        editFigureDialogUi.buttonBox.rejected.connect(cancelFigure)
        #self.connect(createFigureDialogUi.addPlotButton, QtCore.SIGNAL("clicked()"), addPlotToList)
        #self.connect(createFigureDialogUi.buttonBox, QtCore.SIGNAL("accepted()"), makeFigure)
        #self.connect(createFigureDialogUi.buttonBox, QtCore.SIGNAL("rejected()"), cancelFigure)


    ######################
    # temporary methods, for testing
    ######################
    def createDefaultTable(self):
        dtm = DataTableModel([self._waves.waves()[0], self._waves.waves()[1]], self)
        
        # Connect slots
        self._waves.waveRemoved.connect(dtm.removeColumn)

        return self.createDataTableView(dtm)
        
    def printAllWaves(self):
        print self._waves

    def setTestData(self):
        self._waves.addWave(Wave("Wave1", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], int))
        self._waves.addWave(Wave("Wave2", [0, 1, 4, 9, 4, 1, 0, 1, 4, 9], int))
        self._waves.addWave(Wave("Wave3", [0, 1, 3, 1, 3, 1, 3, 1, 3, 1], int))
        self._waves.addWave(Wave("Wave4", [4, 3, 2, 1, 0, 1, 2, 3, 4, 5], int))








if __name__ == "__main__":
    # check to make sure we are using at least Qt 4.6.1, as there is a bugfix in that version that causes
    # qheaderview logicalindices to refactor when removing a column
    qtVersion = string.split(QT_VERSION_STR, ".")
    if qtVersion < ['4',  '6',  '1']:
        print "This application requires at least Qt version 4.6.1.  You are running " + QT_VERSION_STR + "."
        sys.exit()
    
#    print QT_VERSION_STR
#    print PYQT_VERSION_STR

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = pysciplot2()
    window.show()
    sys.exit(app.exec_())

