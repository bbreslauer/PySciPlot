import sys,  string,  signal
from PyQt4 import QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure


from MainWindow import Ui_MainWindow
from DataTableView import DataTableView
from DataTableModel import DataTableModel
from ManageWavesDialog import Ui_ManageWavesDialog
from ManageTablesDialog import Ui_ManageTablesDialog
from DialogSubWindow import DialogSubWindow
from WavesListModel import WavesListModel
from CreatePlotDialog import Ui_CreatePlotDialog

from Waves import Waves
from Wave import Wave
from Plot import Plot
from SubPlot import SubPlot

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
        self.manageTablesDialogWidgetSubWindow = None
        
        # Let the workspace resize when the main window is resized
        self.setCentralWidget(self.ui.workspace)
        
        # Make signal/slot connections
        self.connect(self.ui.actionQuit, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.ui.actionNew_Table, QtCore.SIGNAL("triggered()"), self.createDefaultTable)
        self.connect(self.ui.actionManage_Waves, QtCore.SIGNAL("triggered()"), self.showManageWavesDialog)
        self.connect(self.ui.actionManage_Tables, QtCore.SIGNAL("triggered()"), self.showManageTablesDialog)
        self.connect(self.ui.actionCreate_Plot, QtCore.SIGNAL("triggered()"), self.showCreatePlotDialog)
        self.connect(self.ui.actionShow_Waves,  QtCore.SIGNAL("triggered()"),  self.showAllWaves)
        
        self.waves = Waves([], self)
        self.setTestData()
        print self.waves
        
        self.showCreatePlotDialog()
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
    
    def showCreatePlotDialog(self):
        # create enclosing widget and UI
        createPlotDialogWidget = QtGui.QDialog()
        createPlotDialogUi = Ui_CreatePlotDialog()
        createPlotDialogUi.setupUi(createPlotDialogWidget)
        
        
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        createPlotDialogWidget.setLayout(createPlotDialogUi.gridLayout)
        
        # populate x and y axis lists
        xListModel = WavesListModel(self.waves)
        yListModel = WavesListModel(self.waves)
        createPlotDialogUi.xAxisListView.setModel(xListModel)
        createPlotDialogUi.yAxisListView.setModel(yListModel)
        
        # show window
        createPlotDialogSubWindow = DialogSubWindow(self.ui.workspace)
        createPlotDialogSubWindow.setWidget(createPlotDialogWidget)
        self.ui.workspace.addSubWindow(createPlotDialogSubWindow)
        createPlotDialogSubWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        createPlotDialogSubWindow.show()
        
        def makePlot():
            xAxisIndexList = createPlotDialogUi.xAxisListView.selectedIndexes()
            yAxisIndexList = createPlotDialogUi.yAxisListView.selectedIndexes()
            
#            x = self.waves[xAxisIndexList[0].row()]
#            y = self.waves[yAxisIndexList[0].row()]
#            y = Waves()
#            for i in xAxisIndexList:
#                y.append(self.waves[i.row()])
            x = self.waves[0]
            y = self.waves[1]
            
            plotSubWindow = QtGui.QMdiSubWindow(self.ui.workspace)
            plotSubWindow.resize(450, 450)
            
            plot = Plot(self, plotSubWindow)
            
            # prepare plot
            plot1 = SubPlot(self)
            plot1.setXWave(x)
            plot1.setYWave(y)
            
            plot.addSubPlot(plot1)
            
            plot.buildScene()
            
            plotSubWindow.setWidget(plot.getPlotView())
            self.ui.workspace.addSubWindow(plotSubWindow)
            plotSubWindow.show()
            
            createPlotDialogSubWindow.close()
        
        def cancelPlot():
            createPlotDialogSubWindow.close()
            
        def makePlot2():
            plotSubWindow = QtGui.QMdiSubWindow(self.ui.workspace)
            plotSubWindow.resize(450, 450)
            
            fig = Figure((5.0, 4.0), dpi=100)
            canvas = FigureCanvas(fig)
            canvas.setParent(plotSubWindow)
            
            x = self.waves[0].convertToFloatList()
            y = self.waves[1].convertToFloatList()
            
            axes1 = fig.add_subplot(221)
            axes2 = fig.add_subplot(222)
            axes3 = fig.add_subplot(223)
            
            axes1.clear()
            axes1.scatter(x, y)
            
            axes2.clear()
            axes2.scatter(x, y)
            
            axes3.clear()
            axes3.scatter(x, y)
            
            canvas.draw()

            plotSubWindow.setWidget(canvas)
            self.ui.workspace.addSubWindow(plotSubWindow)
            plotSubWindow.show()
            
            

            
            
        #makePlot()
        
        # connect actions
        self.connect(createPlotDialogUi.buttonBox, QtCore.SIGNAL("accepted()"), makePlot)
        self.connect(createPlotDialogUi.buttonBox, QtCore.SIGNAL("rejected()"), cancelPlot)
    
    def showManageTablesDialog(self):
        if self.manageTablesDialogWidgetSubWindow != None:
            self.ui.workspace.setActiveSubWindow(self.manageTablesDialogWidgetSubWindow)
            self.manageTablesDialogWidgetSubWindow.show()
            return
        
        # create enclosing widget and UI
        manageTablesDialogWidget = QtGui.QWidget()
        manageTablesDialogUi = Ui_ManageTablesDialog()
        manageTablesDialogUi.setupUi(manageTablesDialogWidget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        manageTablesDialogWidget.setLayout(manageTablesDialogUi.gridLayout)
        
#        wavesListModel = WavesListModel(self.waves)
#        manageTablesDialogUi.wavesListView.setModel(wavesListModel)
        
        # show window
        self.manageTablesDialogWidgetSubWindow = DialogSubWindow(self.ui.workspace)
        self.manageTablesDialogWidgetSubWindow.setWidget(manageTablesDialogWidget)
        self.ui.workspace.addSubWindow(self.manageTablesDialogWidgetSubWindow)
        self.manageTablesDialogWidgetSubWindow.setVisible(True)
        
    def setTestData(self):
        self.waves.append(Wave("Wave1", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.waves.append(Wave("Wave2", [0, 1, 4, 9, 4, 1, 0, 1, 4, 9]))
        self.waves.append(Wave("Wave3", [0, 1, 8, 27]))
        self.waves.append(Wave("Wave4", [0, -1,  -4,  -9]))

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
#    for each in app.topLevelWidgets():
#        print each.objectName()
    sys.exit(app.exec_())
    
