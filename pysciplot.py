#!/home/ben/usr/local/bin/python

import sys, string, signal

from PyQt4.QtGui import QMainWindow, QApplication, QMdiSubWindow, QWidget, QDialog, QMessageBox, QAction, QFileDialog
from PyQt4.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt4.QtCore import Qt

from Wave import Wave
from Waves import Waves
from Figure import Figure
from Figures import Figures
from ModuleHandler import ModuleHandler
from models.FigureListModel import FigureListModel
from models.WavesListModel import WavesListModel
from TraceListEntry import TraceListEntry
from DataTableView import DataTableView
from models.DataTableModel import DataTableModel
from DialogSubWindow import DialogSubWindow
from ui.Ui_MainWindow import Ui_MainWindow


class pysciplot(QMainWindow):
    """
    This class initializes the PySciPlot program.
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self._waves = Waves()
        self._figures = Figures()
        self._windows = {}
        self._loadedModules = {}

        # Create the module handler, so that we can import modules
        self.moduleHandler = ModuleHandler()

        # Let the workspace resize when the main window is resized
        self.setCentralWidget(self.ui.workspace)

        # Dialog windows
        self.manageWavesDialogWidgetSubWindow = None
        
        # Make signal/slot connections
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionNew_Table.triggered.connect(self.createDefaultTable)
        self.ui.actionShow_Waves.triggered.connect(self.printAllWaves)
        self.ui.actionShow_Figures.triggered.connect(self.printAllFigures)
        self.ui.actionSave_Project_As.triggered.connect(self.saveProjectAs)

        # create default waves
        self.setTestData()
        self.createDefaultTable()

        self.loadModule("ManageWavesDialog")
        self.loadModule("EditFigureDialog")
        
    def waves(self):
        return self._waves

    def figures(self):
        return self._figures

    def loadModule(self, moduleName):
        """
        Import the module named moduleName.
        """
        
        # Import module
        moduleImport = __import__("modules." + moduleName)
        module = eval("moduleImport." + str(moduleName) + "." + str(moduleName) + "(self)")

        # Initialize the module
        # No parameters are required because the module can access everything
        # through the 'self' parameter in the __init__.
        module.load()

        # Add to loaded modules list
        self._loadedModules[moduleName] = module


    def unloadModule(self, moduleName):
        """
        Unload a module.
        """

        # Unload the module
        self._loadedModules[moduleName].unload()

        # Remove it from the loaded modules list
        self._loadedModules.pop(moduleName)

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

    def saveProjectAs(self):
        """
        Save the current project to a file which will be selected by the user.
        """

        fileName = QFileDialog.getSaveFileName(self.ui.workspace, "Save Project", "/")

    def saveProject(self):
        """
        Save the current project to a file.  If project has previously been saved, use
        that location.
        """
        pass

    def loadProject(self):
        pass

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

    def printAllFigures(self):
        print self._figures

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
    window = pysciplot()
    window.show()
    sys.exit(app.exec_())

