from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTableView, QDialog, QMdiSubWindow, QMessageBox, QMenu, QAction, QAbstractItemView, QItemSelectionModel

from Wave import Wave
from AddWaveAction import AddWaveAction
from models.DataTableModel import DataTableModel
from ui.Ui_RenameWaveDialog import Ui_RenameWaveDialog

class DataTableView(QTableView):
    """
    This is the actual view for the DataTableModel.

    Signals that are emitted from this class are:
        test
    """

    # Signals


    def __init__(self, model, parent, nameIn, mainWindow, *args):
        """
        Initialize a view.  Setup the window, title text, row and column headers.

        model is the DataTableModel to use.
        parent is the window parent.
        nameIn is the window title.
        mainWindow is the pysciplot object
        """

        QTableView.__init__(self, parent, *args)
        self.setParent(parent)
        self._mainWindow = mainWindow
        self.setModel(model)
        self.setMinimumSize(600, 300)
        self.setWindowTitle(nameIn)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setSelectionMode(QTableView.ExtendedSelection)
        self.setEditTriggers(QAbstractItemView.AnyKeyPressed | QAbstractItemView.DoubleClicked)
        self.setupColumnHeaderMenu()
        self.horizontalHeader().setMovable(True)
        self.horizontalHeader().sectionMoved.connect(self.doRealColumnMove)

        # Connect signals
        self.model().waves().waveAdded.connect(self.fullReset)
        self.model().waves().waveRemoved.connect(self.fullReset)
    
    def name(self):
        """Return the name of the table."""
        return self.windowTitle()
    
    @staticmethod
    def getName(tableView):
        """Return the name of the given table.  This is a static method."""
        return tableView.windowTitle()
    
    def insertColumn(self, position, wave=0):
        """
        Insert wave into column position, shifting columns with index >= position to the right.  If wave evaluates to False, then a new wave is created.  Returns True if insert succeeded, False otherwise.
        """
        
        if not wave:
            wave = self._mainWindow.waves().insertNewWave(len(self._mainWindow.waves().waves()))
        return self.model().insertColumn(position, wave)

    def insertColumnLeft(self, position, wave=0):
        """Call insertColumn."""
        return self.insertColumn(position, wave)
    
    def insertColumnRight(self, position, wave=0):
        """Call insertColumn with position + 1."""
        return self.insertColumn(position + 1, wave)

    def renameWave(self, currentIndex):
        """
        Create a dialog box to rename a wave.  When the dialog box is filled out and submitted, try to rename the wave.
        """

        currentWave = self.model().waves().waves()[currentIndex]
        
        # Setup dialog box
        renameWaveDialog = QDialog()
        renameWaveSubWindow = QMdiSubWindow()
        renameWaveSubWindow.setWidget(renameWaveDialog)
        renameWaveSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        renameWaveUi = Ui_RenameWaveDialog()
        renameWaveUi.setupUi(renameWaveDialog)
        renameWaveUi.oldWaveName.setText(currentWave.name())
        self._mainWindow.ui.workspace.addSubWindow(renameWaveSubWindow)
        renameWaveDialog.setVisible(True)
        
        def saveRename():
            """Save button pressed.  Do work to save new name."""
            newName = currentWave.validateWaveName(str(renameWaveUi.newWaveNameLineEdit.text()))
            if self._mainWindow.waves().goodWaveName(newName) and currentWave.setName(newName):
                renameWaveSubWindow.close()
            else:
                failedMessage = QMessageBox()
                failedMessage.setText("Unable to rename wave.")
                failedMessage.exec_()
                renameWaveDialog.setVisible(True)
        
        def cancelRename():
            """Cancel button pressed."""
            renameWaveSubWindow.close()
        
        # connect actions
        renameWaveUi.buttonBox.accepted.connect(saveRename)
        renameWaveUi.buttonBox.rejected.connect(cancelRename)
    
    def removeWaveFromTable(self, position):
        """Remove wave from model.  point is the pixel that is clicked on."""
        self.model().removeColumn(self.model().waves().waves()[position])
       
    def addWaveToTable(self, wave, position):
        """Add wave to model at position."""
        if wave:
            # insertColumn will check if waves must be unique, and will fail (and return False)
            # if waves must be unique and this is a duplicate wave
            return self.insertColumn(position, wave)
        return False
    
    def showColumnHeaderMenu(self, point):
        """Display the menu that occurs when right clicking on a column header."""

        logicalIndex = self.horizontalHeader().logicalIndexAt(point)
        visualIndex = self.horizontalHeader().visualIndex(logicalIndex)
        
        self.selectColumn(visualIndex)
        
        def insertColumnLeftHelper():
            self.insertColumnLeft(visualIndex)
        def insertColumnRightHelper():
            self.insertColumnRight(visualIndex)
        def renameWaveHelper():
            self.renameWave(visualIndex)
        def removeWaveFromTableHelper():
            self.removeWaveFromTable(visualIndex)
        def addWaveToTableHelper(wave):
            self.addWaveToTable(wave, visualIndex)
            
        # Get current list of waves for "add wave to table" menu
        self.addWaveMenu.clear()
        for wave in self._mainWindow.waves().waves():
            self.addWaveMenu.addAction(AddWaveAction(wave, self.addWaveMenu))
        
        # Connect actions
        self.insertColumnLeftAction.triggered.connect(insertColumnLeftHelper)
        self.insertColumnRightAction.triggered.connect(insertColumnRightHelper)
        self.renameWaveAction.triggered.connect(renameWaveHelper)
        self.removeWaveFromTableAction.triggered.connect(removeWaveFromTableHelper)
        for waveAction in self.addWaveMenu.actions():
            waveAction.addWaveClicked.connect(addWaveToTableHelper)
        
        self.columnHeaderMenu.exec_(self.mapToGlobal(point))
        
        # Disconnect actions.  We need to do this or else there will be multiple connections
        # when we open the menu again, and the old connections will have strange visualIndex values
        self.insertColumnLeftAction.triggered.disconnect(insertColumnLeftHelper)
        self.insertColumnRightAction.triggered.disconnect(insertColumnRightHelper)
        self.renameWaveAction.triggered.disconnect(renameWaveHelper)
        self.removeWaveFromTableAction.triggered.disconnect(removeWaveFromTableHelper)
        for waveAction in self.addWaveMenu.actions():
            waveAction.addWaveClicked.disconnect(addWaveToTableHelper)

    def setupColumnHeaderMenu(self):
        """Prepare the menu that is displayed when right clicking on a column header."""

        # Set menu as right-click menu
        header = self.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.showColumnHeaderMenu)
        
        self.columnHeaderMenu = QMenu(self)
        
        # Create actions
        self.renameWaveAction = QAction("Rename Wave", self.columnHeaderMenu)
        self.insertColumnLeftAction = QAction("Insert Column to Left", self.columnHeaderMenu)
        self.insertColumnRightAction = QAction("Insert Column to Right", self.columnHeaderMenu)
        self.removeWaveFromTableAction = QAction("Remove Wave from Table", self.columnHeaderMenu)
        
        # Create "add wave to table" menu
        self.addWaveMenu = QMenu("Add Wave to Table", self.columnHeaderMenu)
        
        # Add actions to menu
        self.columnHeaderMenu.addAction(self.addWaveMenu.menuAction())
        self.columnHeaderMenu.addAction(self.insertColumnLeftAction)
        self.columnHeaderMenu.addAction(self.insertColumnRightAction)
        self.columnHeaderMenu.addAction(self.renameWaveAction)
        self.columnHeaderMenu.addAction(self.removeWaveFromTableAction)
        
    # we want to actually move the columns around in the model, not the view
    # to do this, we need to move the columns in the model then wipe the model from the view and add it back in
    # because view.reset() doesn't reset the logical indices of the view
    def doRealColumnMove(self,  logicalIndex,  oldVisualIndex,  newVisualIndex):
        """
        Move column oldVisualIndex to newVisualIndex in the model.

        This method exists because when a column is moved around (for instance, via drag-and-drop), we need the columns to actually move around in the model, not the view.  This is because view.reset() doesn't reset the logical indices of the view.  I expect this to be resolved in a future QT version, but I don't know when.
        """
        self.model().moveColumn(oldVisualIndex, newVisualIndex)

    def fullReset(self):
        """Wipe the model from the view and then add it back to the view.  This makes the view update all the logical indices."""
        tmpModel = self.model()
        self.setModel(DataTableModel())
        self.setModel(tmpModel)
        self.reset()
        return True
    
    def keyPressEvent(self, event):
        """Capture certain types of keypress events and handle them different ways."""
        # When data has been edited, move to the next row in the column and continue editing.
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            currentIndex = self.currentIndex()
            newIndex = self.model().createIndex(currentIndex.row() + 1, currentIndex.column())
            self.setCurrentIndex(newIndex)
            self.edit(newIndex)
            self.setCurrentIndex(newIndex)
        
        # Do something else
        elif event.key() == Qt.Key_Return:
            pass
        else:
            QTableView.keyPressEvent(self, event)

    # Helper function for debugging 
    def printAllHeaders(self,  logicalIndex):
        for i in range(len(self.model().waves)):
            print "vis: " + str(i) + ", log: " + str(self.horizontalHeader().logicalIndex(i)) + ", name: " + self.model().waves[self.horizontalHeader().logicalIndex(i)].getName()
        print
        for i in range(len(self.model().waves)):
            print "log: " + str(i) + ", vis: " + str(self.horizontalHeader().visualIndex(i)) + ", name: " + self.model().waves[i].getName()
        print
    
