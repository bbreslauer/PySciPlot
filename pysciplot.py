#!/usr/bin/python

import sys, string, signal, os, re, time

from PyQt4.QtGui import QMainWindow, QApplication, QMdiSubWindow, QWidget, QDialog, QMessageBox, QAction, QFileDialog, QDialogButtonBox, QStandardItemModel, QStandardItem
from PyQt4.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt4.QtCore import Qt, QVariant, QFile

import Util, Save, Load
from Wave import Wave
from Waves import Waves
from Figure import Figure
from Figures import Figures
from TraceListEntry import TraceListEntry
from DataTableView import DataTableView
from DialogSubWindow import DialogSubWindow
from Gui import DataTableSubWindow
from Preferences import Preferences
from models.FigureListModel import FigureListModel
from models.WavesListModel import WavesListModel
from models.DataTableModel import DataTableModel
from ui.Ui_MainWindow import Ui_MainWindow
from ui.Ui_ModulesLoadingDialog import Ui_ModulesLoadingDialog
from ui.Ui_SaveFigureOptionsDialog import Ui_SaveFigureOptionsDialog


class pysciplot(QMainWindow):
    """
    This class initializes the PySciPlot program.
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # Variables
        self._version = 1
        self._waves = Waves()
        self._figures = Figures()
        self._loadedModules = {}
        self.cwd = "" # current working directory
        self.setCurrentProject("")

        # Let the workspace resize when the main window is resized
        self.setCentralWidget(self.ui.workspace)

        # Create modules loading/unloading window
        self.createModulesLoadingDialog()

        # Load Preferences
        self.preferences = Preferences(self, "~/.pysciplotrc")
        
        # Make signal/slot connections
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionNew_Table.triggered.connect(self.createDefaultTable)
        self.ui.actionNew_Project.triggered.connect(self.resetToDefaults)
        self.ui.actionLoad_Project.triggered.connect(self.loadProject)
        self.ui.actionSave_Project.triggered.connect(self.saveProject)
        self.ui.actionSave_Project_As.triggered.connect(self.saveProjectAs)
        self.ui.actionSave_Current_Figure.triggered.connect(self.saveCurrentFigure)
        self.ui.actionPreferences.triggered.connect(self.preferences.showDialog)
        
        self.ui.actionShow_Waves.triggered.connect(self.printAllWaves)
        self.ui.actionShow_CWD.triggered.connect(self.printCWD)
        self.ui.actionShow_Figures.triggered.connect(self.printAllFigures)

        # create default waves
        self.setTestData()
        #self.createDefaultTable()

        self.loadModule("ManageWavesDialog")
        self.loadModule("EditFigureDialog")
        self.loadModule("ImportCSV")

        #Load.loadProjectFromFile(self, "/home/ben/test.psp")
        
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

    def createTable(self, waves=[], tableName="Table"):
        """
        Create a table.
        """

        model = DataTableModel(waves, self)

        # Connect slots
        self._waves.waveRemoved.connect(model.removeColumn)

        return self.createDataTableView(model, tableName)

    def createDefaultTable(self):
        # Create new wave to put into this table
        wave = Wave(self.waves().findGoodWaveName())
        self._waves.addWave(wave)

        return self.createTable([wave])

    def createDataTableView(self, tableModel, tableName="Table"):
        """
        Create a table view based on the given model.
        """

        tableView = DataTableView(tableModel, self, tableName, self)
        tableViewSubWindow = DataTableSubWindow()
        tableViewSubWindow.setWidget(tableView)
        tableViewSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.workspace.addSubWindow(tableViewSubWindow)

        tableViewSubWindow.setVisible(True)
        return tableViewSubWindow

    def createModulesLoadingDialog(self):
        """
        Create a window for loading and unloading modules.

        Check States:
            0 = unchecked
            1 = partially checked (unused here)
            2 = checked
        """
        
        widget = QWidget()
        ui = Ui_ModulesLoadingDialog()
        ui.setupUi(widget)

        # Set list view's model
        model = QStandardItemModel()
        ui.modulesList.setModel(model)

        # Create window for this dialog
        self.modulesLoadingDialog = DialogSubWindow(self.ui.workspace)
        self.ui.workspace.addSubWindow(self.modulesLoadingDialog)
        self.modulesLoadingDialog.setWidget(widget)
        widget.setParent(self.modulesLoadingDialog)

        # Define handler functions
        def resetModuleList():
            """Reset the list of modules to the current state."""
            model.clear()

            moduleNames = []
    
            # Get list of all modules
            for fileName in os.listdir(os.getcwd() + "/modules/"):
                if re.search("\.py$", fileName) and not re.match("Module|__init__", fileName):
                    moduleNames.append(fileName.partition('.')[0])
            
            moduleNames.sort()
    
            loadedModules = self._loadedModules.keys()
             
            for moduleName in moduleNames:
                item = QStandardItem(moduleName)
                item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                model.appendRow(item)
                if moduleName in loadedModules:
                    item.setData(2, Qt.CheckStateRole)
                else:
                    item.setData(0, Qt.CheckStateRole)


        def closeModuleList():
            """Reset module list and then hide the list."""
            self.modulesLoadingDialog.hide()

        def showModuleList():
            """Show the list."""
            resetModuleList()
            self.modulesLoadingDialog.show()

        def updateModules():
            """Load and unload modules as necessary."""
            loadedModules = self._loadedModules.keys()
            for row in range(0, model.rowCount()):
                if model.item(row).text() in loadedModules and model.item(row).checkState() == Qt.Unchecked:
                    self.unloadModule(str(model.item(row).text()))
                elif model.item(row).text() not in loadedModules and model.item(row).checkState() == Qt.Checked:
                    self.loadModule(str(model.item(row).text()))

        # Connect buttons to handler functions
        ui.buttons.button(QDialogButtonBox.Reset).clicked.connect(resetModuleList)
        ui.buttons.button(QDialogButtonBox.Cancel).clicked.connect(closeModuleList)
        ui.buttons.button(QDialogButtonBox.Apply).clicked.connect(updateModules)
        self.ui.actionModules.triggered.connect(showModuleList)

        # Hide dialog box
        closeModuleList()

    def saveProjectAs(self):
        """
        Save the current project to a file which will be selected by the user.
        """

        fileDialog = QFileDialog(self.ui.workspace, "Save Project")
        fileDialog.setNameFilter("PySciPlot Project (*.psp);;All Files (*.*)")
        fileDialog.setDefaultSuffix("psp")
        fileDialog.setConfirmOverwrite(True)
        fileDialog.setDirectory(Util.fileDialogDirectory(self))
        fileDialog.exec_()
        fileName = str(fileDialog.selectedFiles()[0])

        if fileName != "":
            # Save current working directory
            self.cwd = os.path.dirname(fileName)

        Save.writeProjectToFile(self, fileName)


    def saveProject(self):
        """
        Save the current project to a file.  If project has previously been saved, use
        that location.
        """

        if self.currentProjectFile != "" and QFile.exists(self.currentProjectFile):
            Save.writeProjectToFile(self, self.currentProjectFile)
        else:
            self.saveProjectAs()

        


    def loadProject(self):
        """
        Load a project from a file which will be selected by the user.
        """

        # Reset app to a clean slate
        self.resetToDefaults()

        # Now load the project
        fileDialog = QFileDialog(self.ui.workspace, "Load Project")
        fileDialog.setNameFilter("PySciPlot Project (*.psp);;All Files (*.*)")
        fileDialog.setDefaultSuffix("psp")
        fileDialog.setConfirmOverwrite(False)
        fileDialog.setDirectory(Util.fileDialogDirectory(self))
        fileDialog.exec_()
        fileName = str(fileDialog.selectedFiles()[0])

        if fileName != "":
            # Save current working directory
            self.cwd = os.path.dirname(fileName)

        Load.loadProjectFromFile(self, fileName)

    def resetToDefaults(self):
        """
        Reset the application to the defaults.  At the very least,
        this will delete all waves, tables, and figures.

        Before resetting, this will ask the user if they want to save
        the current project.
        """
        
        # Check to see if we want to save the current project
        saveProjectMessage = QMessageBox()
        saveProjectMessage.setText("You are about to load another project.")
        saveProjectMessage.setInformativeText("Do you want to save your current project?")
        saveProjectMessage.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        saveProjectResponse = saveProjectMessage.exec_()
        if saveProjectResponse == QMessageBox.Save:
            self.saveProject()
        elif saveProjectResponse == QMessageBox.Cancel:
            return

        # Now reset to a clean slate
        subWindows = self.ui.workspace.subWindowList()

        for window in subWindows:
            if type(window).__name__ in ["DataTableSubWindow", "FigureSubWindow"]:
                window.setAttribute(Qt.WA_DeleteOnClose)
                window.close()
            else:
                window.setVisible(False)

        self._waves.removeAllWaves()
        self._figures.removeAllFigures()
        self.setCurrentProject("")

    def setCurrentProject(self, fileName):
        self.currentProjectFile = fileName
        if fileName != "":
            self.setWindowTitle("PySciPlot - " + fileName)
        else:
            self.setWindowTitle("PySciPlot")



    def saveCurrentFigure(self):
        """
        Save the current figure to a file.

        First we make sure that the active window has a figure in it.
        Then we ask the user for certain options to be set.
        Then we ask for the file to save the figure to.
        Then we save the file.
        """

        currentWindow = self.ui.workspace.activeSubWindow()

        # Check if the active window has a figure in it
        if type(currentWindow).__name__ != "FigureSubWindow":
            notFigureMessage = QMessageBox()
            notFigureMessage.setText("The active window is not a figure, so you cannot save it as a figure.")
            notFigureMessage.exec_()
            return False
        
        # Ask user for user-configurable options
        figureOptionsDialog = QDialog()
        figureOptionsUi = Ui_SaveFigureOptionsDialog()
        figureOptionsUi.setupUi(figureOptionsDialog)
        figureOptionsSubWindow = self.ui.workspace.addSubWindow(figureOptionsDialog)
        figureOptionsResult = figureOptionsDialog.exec_()
        figureOptionsSubWindow.close()
        
        dpi = 100
        orientation = "Landscape"

        if figureOptionsResult == QDialog.Accepted:
            dpi = Util.getWidgetValue(figureOptionsUi.dpi)
            orientation = Util.getWidgetValue(figureOptionsUi.orientation)
        else:
            return False
        
        # As user for the filename to save to
        fileName = QFileDialog.getSaveFileName(self.ui.workspace, "Save Figure", Util.fileDialogDirectory(self))

        if fileName != "":
            # Save current working directory
            self.cwd = os.path.dirname(str(fileName))
        
        # Save the figure to the file
        currentWindow.widget().figure.savefig(str(fileName), dpi=dpi, orientation=orientation)


    ######################
    # temporary methods, for testing
    ######################
#    def createDefaultTable(self):
#        return self.createTable([self._waves.waves()[0], self._waves.waves()[1]])
        
    def printAllWaves(self):
        print self._waves

    def printAllFigures(self):
        print self._figures

    def printCWD(self):
        print self.cwd

    def setTestData(self):
        self._waves.addWave(Wave("Wave1", "Integer", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self._waves.addWave(Wave("Wave2", "Integer", [0, 1, 4, 9, 4, 1, 0, 1, 4, 9]))
        self._waves.addWave(Wave("Wave3", "Integer", [0, 1, 3, 1, 3, 1, 3, 1, 3, 1]))
        self._waves.addWave(Wave("Wave4", "Integer", [4, 3, 2, 1, 0, 1, 2, 3, 4, 5]))




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

