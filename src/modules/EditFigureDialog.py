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


from PyQt4.QtCore import Qt, QObject
from PyQt4.QtGui import QWidget, QAction, QMessageBox

from Wave import *
from Module import *
from Figure import *
from gui.SubWindows import *
from models.FigureListModel import *
from gui.QFigureOptionsWidget import *
from gui.QPlotOptionsWidget import *
from ui.Ui_EditFigureDialog import *
from ui.Ui_FigureOptionsWidget import *
from ui.Ui_PlotOptionsWidget import *


class EditFigureDialog(Module):
    """Module to display the Edit Figure dialog window."""

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        """Create the widget and populate it."""
        
        self._currentFigure = None

        # Create enclosing widget and UI
        self._widget = QWidget()
        self._ui = Ui_EditFigureDialog()
        self._ui.setupUi(self._widget)
        
        # Setup figure list
        self._figureListModel = FigureListModel(self._app.figures())
        self._ui.figureSelector.setModel(self._figureListModel)
        self._ui.figureSelector.currentIndexChanged[int].connect(self.changeCurrentFigure)
        self._app.figures().figureAdded.connect(self._figureListModel.doReset)
        self._app.figures().figureRemoved.connect(self._figureListModel.doReset)
        self._app.figures().figureRenamed.connect(self.updateFigureSelectorBox)

        # Connect signals for buttons at top of widget
        self._ui.addFigureButton.clicked.connect(self.createFigure)
        self._ui.showFigureButton.clicked.connect(self.showFigure)
        self._ui.deleteFigureButton.clicked.connect(self.deleteFigure)

        # Setup figure tab
        self._figureTab = QFigureOptionsWidget(self._widget)
        figureOW = Ui_FigureOptionsWidget()
        figureOW.setupUi(self._figureTab)
        self._figureTab.setUiObject(figureOW)
        self._figureTab.setEditFigureDialogModule(self)
        self._ui.tabWidget.insertTab(0, self._figureTab, "Figure")

        # Setup plot tab
        self._plotTab = QPlotOptionsWidget(self._widget)
        plotOW = Ui_PlotOptionsWidget()
        plotOW.setupUi(self._plotTab)
        self._plotTab.setUiObject(plotOW)
        self._plotTab.setEditFigureDialogModule(self)
        self._plotTab.initPlotSelector()
        self._plotTab.initSubWidgets()
        self._ui.tabWidget.insertTab(1, self._plotTab, "Plot")

        # If the number of rows or columns is changed, then we need to refresh the plot list
        # It's simpler to just always check this when the Apply button is pressed
        figureOW.buttons.button(QDialogButtonBox.Apply).clicked.connect(self._plotTab.refreshPlotSelector)


        # Make sure that the figure tab is initially displayed
        self._ui.tabWidget.setCurrentIndex(0)

    #
    # Handlers for the three buttons at the top of the widget
    #
    def createFigure(self):
        figure = Figure("NewFigure")
        self._app.figures().addFigure(figure)

        # Select figure
        self._ui.figureSelector.setCurrentIndex(self._ui.figureSelector.model().rowCount() - 1)

    def showFigure(self):
        """Display the figure, in case it got hidden."""
        
        if self.currentFigure():
            self.currentFigure().showFigure()

    def deleteFigure(self):
        """
        Delete button has been pressed.  Make sure the user really wants
        to delete the figure.
        """
        
        figure = self.currentFigure()
        
        # Make sure we are on a valid figure
        if not figure:
            return False
        
        # Ask user if they really want to delete the figure
        questionMessage = QMessageBox()
        questionMessage.setIcon(QMessageBox.Question)
        questionMessage.setText("You are about to delete a figure.")
        questionMessage.setInformativeText("Are you sure this is what you want to do?")
        questionMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        questionMessage.setDefaultButton(QMessageBox.No)
        answer = questionMessage.exec_()

        if answer == QMessageBox.Yes:
            figure.hideFigure()
            self._app.figures().removeFigure(figure)

    #
    # Get current items
    #
    def currentFigure(self):
        return self._currentFigure

    def changeCurrentFigure(self, index):
        if index < 0:
            return
        
        self._currentFigure = self._ui.figureSelector.model().getFigure(index)
        self._figureTab.resetUi()
        self._plotTab.setFigure(self._currentFigure)

    # Update figure selector combo boxes
    def updateFigureSelectorBox(self):
        # Figure name may have changed, so we'll reset the figure combo box
        # But keep the same figure selected
        figure = self.currentFigure()

        # We are not actually changing the current figure, so we will disconnect this signal for the moment
        self._ui.figureSelector.currentIndexChanged[int].disconnect(self.changeCurrentFigure)

        currentFigureIndex = self._ui.figureSelector.currentIndex()
        self._ui.figureSelector.model().doReset()
        self._ui.figureSelector.setCurrentIndex(currentFigureIndex)
        
        self._ui.figureSelector.currentIndexChanged[int].connect(self.changeCurrentFigure)



    """Module-required methods"""
    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu

    def load(self):
        self.window = SubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionEditFiguresDialog")
        self.menuEntry.setShortcut("Ctrl+F")
        self.menuEntry.setText("Edit Figures")
        self.menuEntry.triggered.connect(self.window.show)
        self.menu = vars(self._app.ui)["menuPlot"]
        self.menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):
        # Disconnect some slots
        self._app.figures().figureAdded.disconnect(self._figureListModel.doReset)
        self._app.figures().figureRemoved.disconnect(self._figureListModel.doReset)
        self._ui.plotSelector.currentIndexChanged.disconnect(self.plotUi_refreshTraceList)
        self._app.waves().waveAdded.disconnect(self._wavesModel.doReset)
        self._app.waves().waveRemoved[Wave].disconnect(self._wavesModel.doReset)
        self.menuEntry.triggered.disconnect()

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)


