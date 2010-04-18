import sys,  string,  signal
from PyQt4 import QtGui, QtCore

#import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
#from matplotlib.figure import Figure


from ui.MainWindow import Ui_MainWindow
from DataTableView import DataTableView
from DataTableModel import DataTableModel
from ui.ManageWavesDialog import Ui_ManageWavesDialog
from DialogSubWindow import DialogSubWindow
from WavesListModel import WavesListModel
from ui.CreateFigureDialog import Ui_CreateFigureDialog
from PlotListModel import PlotListModel
from PlotListEntry import PlotListEntry

from Waves import Waves
from Wave import Wave

from Figure import Figure

# copy/paste of data

# segfaults happen because of qmenu initialization in mainwindow.py
# if no parent is given to qmenu constructor, it works fine
# but if a parent is given (self.menubar), then a segfault occurs about 50% of the time on program exit
#

class pysciplot(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # views and dialogs
        self.manageWavesDialogWidgetSubWindow = None
        
        # Let the workspace resize when the main window is resized
        self.setCentralWidget(self.ui.workspace)
        
        # Make signal/slot connections
        self.connect(self.ui.actionQuit, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.ui.actionNew_Table, QtCore.SIGNAL("triggered()"), self.createDefaultTable)
        self.connect(self.ui.actionManage_Waves, QtCore.SIGNAL("triggered()"), self.showManageWavesDialog)
        self.connect(self.ui.actionCreate_Figure, QtCore.SIGNAL("triggered()"), self.showCreateFigureDialog)
        self.connect(self.ui.actionShow_Waves,  QtCore.SIGNAL("triggered()"),  self.showAllWaves)
        
        
        
        self.waves = Waves([], self)
        self.setTestData()
        print self.waves
        
        self.showCreateFigureDialog()
        self.createDefaultTable()
        
    def showAllWaves(self):
        for wave in self.waves:
            print wave.getName() + ": " + str(wave)

    def createDataTableView(self, tableModel):
        tableView = DataTableView(tableModel, self, "Table")
        tableViewSubWindow = QtGui.QMdiSubWindow()
        tableViewSubWindow.setWidget(tableView)
        tableViewSubWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.workspace.addSubWindow(tableViewSubWindow)
        self.connect(self, QtCore.SIGNAL("waveRenamed"), tableView.fullReset)
        self.connect(self, QtCore.SIGNAL("waveUpdated"), tableView.fullReset)
        self.connect(self, QtCore.SIGNAL("waveRemoved"), tableView.model().checkWaveRemoved)
        self.connect(self, QtCore.SIGNAL("waveRemoved"), tableView.fullReset)
        self.connect(self, QtCore.SIGNAL("columnsRemoved"), tableView.model().checkColumnsRemoved)
        self.connect(self, QtCore.SIGNAL("columnsAdded"), tableView.model().checkColumnsAdded)
        tableViewSubWindow.setVisible(True)
        return tableView
        
    def createDefaultTable(self):
        dtm = DataTableModel([self.waves[0], self.waves[1], self.waves[2], self.waves[3]], self)
        return self.createDataTableView(dtm)
    
    def showManageWavesDialog(self):
        if self.manageWavesDialogWidgetSubWindow != None:
            self.ui.workspace.setActiveSubWindow(self.manageWavesDialogWidgetSubWindow)
            self.manageWavesDialogWidgetSubWindow.show()
            return
        
        # create enclosing widget and UI
        manageWavesDialogWidget = QtGui.QWidget()
        manageWavesDialogUi = Ui_ManageWavesDialog()
        manageWavesDialogUi.setupUi(manageWavesDialogWidget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        manageWavesDialogWidget.setLayout(manageWavesDialogUi.horizontalLayout)
        
        wavesListModel = WavesListModel(self.waves)
        manageWavesDialogUi.wavesListView.setModel(wavesListModel)
        
        # show window
        self.manageWavesDialogWidgetSubWindow = DialogSubWindow(self.ui.workspace)
        self.manageWavesDialogWidgetSubWindow.setWidget(manageWavesDialogWidget)
        self.ui.workspace.addSubWindow(self.manageWavesDialogWidgetSubWindow)
        self.manageWavesDialogWidgetSubWindow.setVisible(True)
        
        # define handler functions
        def addWave():
            name = str(manageWavesDialogUi.waveNameLineEdit.text())
            newWave = Wave(name)
            if self.waves.append(newWave):
                wavesListModel.reset()
            else:
                failedMessage = QtGui.QMessageBox()
                failedMessage.setText("Name already exists: " + name)
                failedMessage.exec_()
            manageWavesDialogUi.waveNameLineEdit.setText("")
        def removeWaves():
            wavesToRemove = []
            for index in manageWavesDialogUi.wavesListView.selectedIndexes():
                wavesToRemove.append(self.waves[index.row()])
            for wave in wavesToRemove:
                self.waves.removeWave(wave)
            wavesListModel.reset()
        def closeWindow():
            self.manageWavesDialogWidgetSubWindow.close()
            
        # connect buttons to handler functions
        self.connect(manageWavesDialogUi.waveNameLineEdit, QtCore.SIGNAL("returnPressed()"), addWave)
        self.connect(manageWavesDialogUi.createWaveButton, QtCore.SIGNAL("clicked()"), addWave)
        self.connect(manageWavesDialogUi.removeWaveButton, QtCore.SIGNAL("clicked()"), removeWaves)
        self.connect(manageWavesDialogUi.closeButton, QtCore.SIGNAL("clicked()"), closeWindow)
        self.connect(self, QtCore.SIGNAL("waveAdded"), wavesListModel.reset)
        self.connect(self, QtCore.SIGNAL("waveRemoved"), wavesListModel.reset)
        self.connect(self, QtCore.SIGNAL("waveRenamed"), wavesListModel.reset)
    
    def showCreateFigureDialog(self):
        # create enclosing widget and UI
        createFigureDialogWidget = QtGui.QDialog()
        createFigureDialogUi = Ui_CreateFigureDialog()
        createFigureDialogUi.setupUi(createFigureDialogWidget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        createFigureDialogWidget.setLayout(createFigureDialogUi.gridLayout)
        
        # populate x and y axis lists
        xListModel = WavesListModel(self.waves)
        yListModel = WavesListModel(self.waves)
        createFigureDialogUi.xAxisListView.setModel(xListModel)
        createFigureDialogUi.yAxisListView.setModel(yListModel)
        
        # prepare plot list
        plotListModel = PlotListModel()
        createFigureDialogUi.plotListView.setModel(plotListModel)
        
        # show window
        createFigureDialogSubWindow = DialogSubWindow(self.ui.workspace)
        createFigureDialogSubWindow.setWidget(createFigureDialogWidget)
        self.ui.workspace.addSubWindow(createFigureDialogSubWindow)
        createFigureDialogSubWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        createFigureDialogSubWindow.show()
        
        def addPlotToList():
            xAxisIndexList = createFigureDialogUi.xAxisListView.selectedIndexes()
            yAxisIndexList = createFigureDialogUi.yAxisListView.selectedIndexes()
            plotNum = createFigureDialogUi.plotNumLineEdit.text().toInt()[0]
            
            for i in yAxisIndexList:
                ple = PlotListEntry(self.waves[xAxisIndexList[0].row()], self.waves[i.row()], plotNum)
                plotListModel.addPlotListEntry(ple)
        
        def makeFigure():
            nRows = createFigureDialogUi.numRowsLineEdit.text().toInt()[0]
            nCols = createFigureDialogUi.numColsLineEdit.text().toInt()[0]
            
            figure = Figure(nRows, nCols)
            
            figureSubWindow = QtGui.QMdiSubWindow(self.ui.workspace)
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
            self.connect(self, QtCore.SIGNAL("waveUpdated"), updatePlots)
        
            createFigureDialogSubWindow.close()
        
        def cancelFigure():
            createFigureDialogSubWindow.close()
        
        # connect actions
        self.connect(createFigureDialogUi.addPlotButton, QtCore.SIGNAL("clicked()"), addPlotToList)
        self.connect(createFigureDialogUi.buttonBox, QtCore.SIGNAL("accepted()"), makeFigure)
        self.connect(createFigureDialogUi.buttonBox, QtCore.SIGNAL("rejected()"), cancelFigure)
        
    def setTestData(self):
        self.waves.append(Wave("Wave1", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.waves.append(Wave("Wave2", [0, 1, 4, 9, 4, 1, 0, 1, 4, 9]))
        self.waves.append(Wave("Wave3", [0, 1, 3, 1, 3, 1, 3, 1, 3, 1]))
        self.waves.append(Wave("Wave4", [4, 3, 2, 1, 0, 1, 2, 3, 4, 5]))

if __name__ == "__main__":
    # check to make sure we are using at least Qt 4.6.1, as there is a bugfix in that version that causes
    # qheaderview logicalindices to refactor when removing a column
    qtVersion = string.split(QtCore.QT_VERSION_STR, ".")
    if qtVersion < ['4',  '6',  '1']:
        print "This application requires at least Qt version 4.6.1.  You are running " + QtCore.QT_VERSION_STR + "."
        sys.exit()
    
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)
    window = pysciplot()
    window.show()
    sys.exit(app.exec_())
    
