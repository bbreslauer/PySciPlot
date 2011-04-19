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


import string, os, re, time, pickle


from PyQt4.QtGui import QMainWindow, QApplication, QMdiSubWindow, QWidget, QDialog, QMessageBox, QAction, QFileDialog, QDialogButtonBox, QStandardItemModel, QStandardItem
from PyQt4.QtCore import Qt, QVariant, QFile

import matplotlib
matplotlib.use('Qt4Agg')

import Util
import Save
import Load
import config
from Wave import Wave
from Waves import Waves
from Figure import Figure
from Figures import Figures
from gui.QDataTableView import QDataTableView
from gui.SubWindows import SubWindow
from gui.SubWindows import DataTableSubWindow
from Preferences import Preferences
from models.FigureListModel import FigureListModel
from models.WavesListModel import WavesListModel
from models.DataTableModel import DataTableModel
from ui.Ui_MainWindow import Ui_MainWindow
from ui.Ui_SaveFigureOptionsDialog import Ui_SaveFigureOptionsDialog
import modules
from modules import *


class Pysciplot(QMainWindow):
    """
    This class initializes the PySciPlot program.
    """

    def __init__(self):
        QMainWindow.__init__(self)
        Util.debug(2, "App", "Setting up UI")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def setup(self):
        """
        Setup the application.
        """

        # Variables
        Util.debug(2, "App", "Initializing variables")
        self._version = 1
        self._waves = Waves()
        self._figures = Figures()
        self._models = {}
        self._loadedModules = {}
        self.projectDir = "" # current project directory
        self.setCurrentProject("")
        self._storedSettings = {}   # this is a dict with widgetName: list pairs
                                    # where each list has [setting-name, setting-value] pairs
                                    # setting-value is a dict with (property-name: Property) pairs

        # Let the workspace resize when the main window is resized
        self.setCentralWidget(self.ui.workspace)

        # Load Preferences
        Util.debug(2, "App", "Loading Preferences from file")
        self.preferences = Preferences("~/.pysciplotrc")
        
        # Create application-wide models
        self._models['appWaves'] = WavesListModel(self.waves().waves())

        # Make signal/slot connections
        Util.debug(2, "App", "Connecting signals and slots")
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionNew_Table.triggered.connect(self.createDefaultTable)
        self.ui.actionNew_Project.triggered.connect(self.newProjectSlot)
        self.ui.actionLoad_Project.triggered.connect(self.loadProjectSlot)
        self.ui.actionSave_Project.triggered.connect(self.saveProject)
        self.ui.actionSave_Project_As.triggered.connect(self.saveProjectAs)
        self.ui.actionSave_Current_Figure.triggered.connect(self.saveCurrentFigure)
        self.ui.actionPreferences.triggered.connect(self.preferences.showDialog)

        self.waves().waveAdded.connect(self.model('appWaves').appendRow)
        self.waves().allWavesRemoved.connect(self.model('appWaves').removeAllWaves)

        self.ui.actionShow_Waves.triggered.connect(self.printAllWaves)
        self.ui.actionShow_Figures.triggered.connect(self.printAllFigures)

        # create default waves
        self.setTestData()
        self.createDefaultTable()

        Util.debug(2, "App", "Loading modules")
        for moduleName in modules.__all__:
            module = eval(moduleName + "." + moduleName + "()")
            module.load()
            self._loadedModules[moduleName] = module

        #Load.loadProjectFromFile(self, "/home/ben/test.psp")
        
    def waves(self):
        """
        Return the app's Waves object.  NOT A LIST OF WAVES.
        """
        return self._waves

    def figures(self):
        """
        Return the app's Figures object.  NOT A LIST OF FIGURES.
        """
        return self._figures

    def storedSettings(self):
        """
        Return the storedSettings dict.
        """
        return self._storedSettings
    
    def models(self):
        """
        Return the models dict.
        """
        return self._models

    def model(self, name):
        """
        Return a specific model from the models dict.
        """
        return self._models[name]

    def createTable(self, waves=[], tableName="Table"):
        """
        Create a table.
        """

        Util.debug(2, "App.createTable", "Creating a table")
        model = DataTableModel(waves, self)

        # Connect slots
        self.waves().waveRemoved[Wave].connect(model.removeWave)
        self.waves().allWavesRemoved.connect(model.removeAllWaves)

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

        tableViewSubWindow = DataTableSubWindow(self.ui.workspace)
        tableView = QDataTableView(tableModel, tableName, tableViewSubWindow)
        tableViewSubWindow.setWidget(tableView)
        tableViewSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        tableViewSubWindow.resize(600, 300)
        self.ui.workspace.addSubWindow(tableViewSubWindow)

        tableViewSubWindow.setVisible(True)

        return tableViewSubWindow

    def saveProjectAs(self):
        """
        Save the current project to a file which will be selected by the user.
        """

        Util.debug(2, "App.saveProjectAs", "Saving project as")
        
        fileName = str(QFileDialog.getSaveFileName(self.ui.workspace, "Save Project", self.projectDirectory(), "PySciPlot Project (*.psp);;All Files (*.*)"))

        Save.writeProjectToFile(self, fileName)

    def saveProject(self):
        """
        Save the current project to a file.  If project has previously been saved, use
        that location.
        """

        Util.debug(2, "App.saveProject", "Saving project")
        if self.currentProjectFile != "" and QFile.exists(self.currentProjectFile):
            Save.writeProjectToFile(self, self.currentProjectFile)
        else:
            self.saveProjectAs()

        
    def loadProjectSlot(self):
        """
        Slot to pick up menu selection and run loadProject.  Required because of different parameters.
        """
        self.loadProject()

    def loadProject(self, fileName="", confirmReset=True):
        """
        Load a project from a file which will be selected by the user.
        """

        Util.debug(2, "App.loadProject", "Loading project from file " + str(fileName))
        
        # Reset app to a clean slate
        self.resetToDefaults(confirmReset)
        
        # Now load the project
        if fileName == "":
            fileDialog = QFileDialog(self.ui.workspace, "Load Project")
            fileDialog.setNameFilter("PySciPlot Project (*.psp);;All Files (*.*)")
            fileDialog.setDefaultSuffix("psp")
            fileDialog.setConfirmOverwrite(False)
            fileDialog.setDirectory(self.projectDirectory())
            fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
            fileDialog.exec_()
            fileName = str(fileDialog.selectedFiles()[0])
    
        Load.loadProjectFromFile(self, fileName)
        
    def newProjectSlot(self):
        """
        Slot to pick up menu selection and create a new project.  Required because of different parameters.
        """
        Util.debug(2, "App.newProject", "Creating new project")        
        self.resetToDefaults(True)

    def resetToDefaults(self, confirm=True):
        """
        Reset the application to the defaults.  At the very least,
        this will delete all waves, tables, and figures.

        Before resetting, this will ask the user if they want to save
        the current project.
        """
        
        Util.debug(2, "App.resetToDefaults", "Resetting application to defaults")
        
        if confirm:
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
        Util.debug(3, "App.setCurrentProject", "Setting current project title")
        self.currentProjectFile = fileName
        if fileName != "":
            self.setWindowTitle("PySciPlot - " + fileName)
        else:
            self.setWindowTitle("PySciPlot")

    def projectDirectory(self):
        if os.path.isdir(self.projectDir):
            return self.projectDir
        return self.preferences.getInternal('projectDirectory')

    def saveCurrentFigure(self):
        """
        Save the current figure to a file.

        First we make sure that the active window has a figure in it.
        Then we ask the user for certain options to be set.
        Then we ask for the file to save the figure to.
        Then we save the file.
        """

        Util.debug(2, "App.saveCurrentFigure", "Saving current Figure")

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
        fileName = QFileDialog.getSaveFileName(self.ui.workspace, "Save Figure", self.projectDirectory())

        # Save the figure to the file
        currentWindow.widget().figure.savefig(str(fileName), dpi=dpi, orientation=orientation)


    ######################
    # temporary methods, for testing
    ######################
    def createDefaultTable(self):
        return self.createTable(self._waves.waves().values())

    def printAllWaves(self):
        print self._waves
        #print self.storedSettings()

    def printAllFigures(self):
        print self._figures

    def setTestData(self):
        self._waves.addWave(Wave("Wave1", "Integer", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self._waves.addWave(Wave("Wave2", "Integer", [0, 1, 4, 9, 4, 1, 0, 1, 4, 9]))
        self._waves.addWave(Wave("Wave3", "Integer", [0, 1, 3, 1, 3, 1, 3, 1, 3, 1]))
        self._waves.addWave(Wave("Wave4", "Integer", [4, 3, 2, 1, 0, 1, 2, 3, 4, 5]))
        #self._waves.addWave(Wave("Wave5", "Integer", range(4194304)))

