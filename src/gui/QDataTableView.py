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


from PyQt4.QtCore import Qt, QModelIndex, pyqtSignal
from PyQt4.QtGui import QTableView, QAbstractItemView, QMenu, QAction, QDialog, QMessageBox, QApplication

import Util
from Wave import Wave
from gui.SubWindows import SubWindow
from ui.Ui_RenameWaveDialog import Ui_RenameWaveDialog

class AddWaveAction(QAction):
    """
    This class is an action for adding a wave to a table.  It encapsulates the wave in an action.
    
    Signals that are emitted from this class are:
        addWaveClicked - emitted when the menu item attached to this class is clicked
    """

    # Signals
    addWaveClicked = pyqtSignal(Wave)

    def __init__(self, wave, parent):
        QAction.__init__(self, wave.name(), parent)
        self._wave = wave
        self.triggered.connect(self.addingWave)
    
    def addingWave(self):
        """Convert from a triggered signal to a addWaveClicked signal."""
        self.addWaveClicked.emit(self._wave)

class QDataTableView(QTableView):
    """
    This is an actual table of waves.
    """

    def __init__(self, model=None, title="Table", *args):
        """
        Initialize the view.

        model is the DataTableModel to use.
        title is the window title.
        """

        QTableView.__init__(self, *args)
        self._app = QApplication.instance().window

        if model is None:
            model = DataTableModel()
        self.setModel(model)
        self.setWindowTitle(title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setSelectionMode(QAbstractItemView.ContiguousSelection) # contiguous instead of extended so that we can easily insert/delete cells more easily.  See note below.
        self.setEditTriggers(QAbstractItemView.AnyKeyPressed | QAbstractItemView.SelectedClicked | QAbstractItemView.DoubleClicked)
        self.horizontalHeader().setMovable(True)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showCellContextMenu)
        
        self.verticalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.verticalHeader().customContextMenuRequested.connect(self.showVerticalHeaderMenu)
        
        self.setupHorizontalHeaderMenu()

    def name(self):
        """Return the name of the table."""
        return self.windowTitle()

    def renameWave(self, wave):
        """
        Create a dialog box to rename a wave.  When the dialog box is filled out and submitted, try to rename the wave.
        """

        # Setup dialog box
        renameWaveDialog = QDialog(self)
        renameWaveUi = Ui_RenameWaveDialog()
        renameWaveUi.setupUi(renameWaveDialog)
        renameWaveUi.oldWaveName.setText(wave.name())
        renameWaveDialog.setVisible(True)
        
        def saveRename():
            """Save button pressed.  Do work to save new name."""
            newName = wave.validateWaveName(str(renameWaveUi.newWaveNameLineEdit.text()))
            if str(renameWaveUi.newWaveNameLineEdit.text()) == "":
                failedMessage = QMessageBox(renameWaveDialog)
                failedMessage.setText("Cannot use a blank name.")
                failedMessage.exec_()
                renameWaveDialog.setVisible(True)
            elif self._app.waves().goodWaveName(newName) and wave.setName(newName):
                renameWaveDialog.close()
            else:
                failedMessage = QMessageBox()
                failedMessage.setText("Unable to rename wave.")
                failedMessage.exec_()
                renameWaveDialog.setVisible(True)
        
        def cancelRename():
            """Cancel button pressed."""
            renameWaveDialog.close()
        
        # connect actions
        renameWaveUi.buttons.accepted.connect(saveRename)
        renameWaveUi.buttons.rejected.connect(cancelRename)

    def removeWave(self, wave):
        self.model().removeColumn(wave)
        
    def addWave(self, wave, visualIndex):
        if self.model().addColumn(wave):
            # The wave was added (i.e. it did not already exist in the table)
            # We need to move the newly added column from the end to where the user clicked
            self.horizontalHeader().moveSection(self.model().columnCount() - 1, visualIndex + 1)

    def insertCells(self):
        """Insert cells into waves based on selected cells in this table."""

        # Sort by rows, so that we start at the top of the waves
        # This is the reason we only do contiguous selections, because
        # tracking which cells to insert into is really difficult otherwise
        selectedCells = self.selectedIndexes()
        selectedCells.sort(None, QModelIndex.row, False)

        for cell in selectedCells:
            try:
                cell.internalPointer().insert(cell.row(), "")
            except:
                # The cell did not exist (i.e. the wave does not extend this far)
                # but another wave does, so do not fail completely
                pass

    def deleteCells(self):
        """Delete cells from waves based on selected cells in this table."""

        # Sort by rows, inverted, so that we start by deleting at the
        # bottom of the waves, and don't screw up index values along
        # the way
        selectedCells = self.selectedIndexes()
        selectedCells.sort(None, QModelIndex.row, True)

        for cell in selectedCells:
            try:
                cell.internalPointer().pop(cell.row())
            except:
                # The cell did not exist (i.e. the wave does not extend this far)
                # but another wave does, so do not fail completely
                pass
    
    def showCellContextMenu(self, point):
        """Display the menu that occurs when right clicking on a table cell."""
        
        clickedCell = self.indexAt(point)

        if not clickedCell.isValid():
            # User clicked on a part of the table without a cell
            return False

        cellMenu = QMenu(self)
        insertCellAction = QAction("Insert Cells", cellMenu)
        deleteCellAction = QAction("Delete Cells", cellMenu)
        
        cellMenu.addAction(insertCellAction)
        cellMenu.addAction(deleteCellAction)

        # Connect signals
        insertCellAction.triggered.connect(self.insertCells)
        deleteCellAction.triggered.connect(self.deleteCells)

        # Display menu
        cellMenu.exec_(self.mapToGlobal(point))

        # Disconnect signals
        insertCellAction.triggered.disconnect(self.insertCells)
        deleteCellAction.triggered.disconnect(self.deleteCells)

    def showVerticalHeaderMenu(self, point):
        """Display the menu that occurs when right clicking on a vertical header."""

        rowMenu = QMenu(self)
        insertRowAction = QAction("Insert Rows", rowMenu)
        deleteRowAction = QAction("Delete Rows", rowMenu)
        
        rowMenu.addAction(insertRowAction)
        rowMenu.addAction(deleteRowAction)

        # Connect signals
        insertRowAction.triggered.connect(self.insertCells)
        deleteRowAction.triggered.connect(self.deleteCells)

        # Display menu
        rowMenu.exec_(self.mapToGlobal(point))

        # Disconnect signals
        insertRowAction.triggered.disconnect(self.insertCells)
        deleteRowAction.triggered.disconnect(self.deleteCells)

    def setupHorizontalHeaderMenu(self):
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(self.showHorizontalHeaderMenu)

        self.horizontalHeaderMenu = QMenu(self.horizontalHeader())
        
        # Create actions
        self.renameWaveAction = QAction("Rename Wave", self.horizontalHeaderMenu)
        self.removeWaveAction = QAction("Remove Wave", self.horizontalHeaderMenu)
        self.addWaveMenu = QMenu("Add Wave", self.horizontalHeaderMenu)

        # Add actions to menu
        self.horizontalHeaderMenu.addAction(self.addWaveMenu.menuAction())
        self.horizontalHeaderMenu.addAction(self.renameWaveAction)
        self.horizontalHeaderMenu.addAction(self.removeWaveAction)


    def showHorizontalHeaderMenu(self, point):
        """Display the menu that occurs when right clicking on a column header."""

        logicalIndex = self.horizontalHeader().logicalIndexAt(point)
        visualIndex = self.horizontalHeader().visualIndex(logicalIndex)
        
        self.selectColumn(visualIndex)

        #print "l: " + str(logicalIndex)
        #print "v: " + str(visualIndex)
        selectedWave = self.model().waves().waves()[logicalIndex]
        
        # Create helper functions, defined for this specific menu location
        def renameWaveHelper():
            self.renameWave(selectedWave)
        def removeWaveHelper():
            self.removeWave(selectedWave)
        def addWaveHelper(wave):
            self.addWave(wave, visualIndex)
        def addNewWaveHelper():
            wave = Wave(self._app.waves().findGoodWaveName())
            self._app.waves().addWave(wave)
            self.addWave(wave, visualIndex)


        self.addWaveMenu.clear()
        
        # Add "New Wave" entry
        newWaveAction = QAction("New Wave", self.addWaveMenu)
        self.addWaveMenu.addAction(newWaveAction)
        newWaveAction.triggered.connect(addNewWaveHelper)
        
        # Get current list of waves for "add wave to table" menu
        for wave in self._app.waves().waves():
            waveAction = AddWaveAction(wave, self.addWaveMenu)
            self.addWaveMenu.addAction(waveAction)
            waveAction.addWaveClicked.connect(addWaveHelper)

        # Connect actions
        self.renameWaveAction.triggered.connect(renameWaveHelper)
        self.removeWaveAction.triggered.connect(removeWaveHelper)
        
        self.horizontalHeaderMenu.exec_(self.mapToGlobal(point))

        # Disconnect actions.  We need to do this or else there will be multiple connections
        # when we open the menu again, and the old connections will have strange visualIndex values
        self.renameWaveAction.triggered.disconnect(renameWaveHelper)
        self.removeWaveAction.triggered.disconnect(removeWaveHelper)
        for waveAction in self.addWaveMenu.actions():
            try:
                waveAction.addWaveClicked.disconnect(addWaveHelper)
            except:
                waveAction.triggered.disconnect(addNewWaveHelper)
   
    def reset(self):
        QTableView.reset(self)
        self.resizeRowsToContents()
        self.resizeColumnsToContents()

    def keyPressEvent(self, event):
        """Capture certain types of keypress events and handle them different ways."""
        # When data has been edited, move to the next row in the column and continue editing.
        currentIndex = self.currentIndex()

        #print "row: " + str(currentIndex.row()) + ", col: " + str(currentIndex.column())
        
        if currentIndex.isValid():
            if self.state() == QAbstractItemView.EditingState:
                if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                    Util.debug(3, "DataTableView.keyPressEvent", "Enter key pressed in table")
                    newIndex = self.model().createIndex(currentIndex.row() + 1, currentIndex.column())
                    self.setCurrentIndex(newIndex)
                    self.edit(newIndex)
                    self.setCurrentIndex(newIndex)
                    return
                elif event.key() == Qt.Key_Up:
                    Util.debug(3, "DataTableView.keyPressEvent", "Up key pressed in table")
                    newIndex = self.model().createIndex(currentIndex.row() - 1, currentIndex.column())
                    #print "nrow: " + str(newIndex.row()) + ", ncol: " + str(newIndex.column())
                    #self.setCurrentIndex(newIndex)
                    self.setState(QAbstractItemView.NoState)
                elif event.key() == Qt.Key_Down:
                    Util.debug(3, "DataTableView.keyPressEvent", "Down key pressed in table")
                    newIndex = self.model().createIndex(currentIndex.row() + 1, currentIndex.column())
                    #print "nrow: " + str(newIndex.row()) + ", ncol: " + str(newIndex.column())
                    #self.setCurrentIndex(newIndex)
                    self.setState(QAbstractItemView.NoState)
        
        # Nothing found, so resort to default behavior
        QTableView.keyPressEvent(self, event)

