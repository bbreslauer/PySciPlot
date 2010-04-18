from PyQt4.QtCore import Qt, SIGNAL
from PyQt4 import QtGui
from ui.RenameWaveDialog import Ui_RenameWaveDialog
from Wave import Wave
from AddWaveAction import AddWaveAction
from DataTableViewHeader import DataTableViewHeader
from DataTableModel import DataTableModel

class DataTableView(QtGui.QTableView):
    def __init__(self, model, parent, nameIn, *args):
        QtGui.QTableView.__init__(self, parent, *args)
        self.setParent(parent)
        self.setModel(model)
        self.setMinimumSize(600, 300)
        self.name = nameIn
        self.setWindowTitle(nameIn)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setSelectionMode(QtGui.QTableView.ExtendedSelection)
        self.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)
        self.mainWindow = parent
        self.setupColumnHeaderMenu()
        self.horizontalHeader().setMovable(True)
        self.connect(self.horizontalHeader(), SIGNAL("sectionClicked(int)"),  self.printAllHeaders)
        self.connect(self.horizontalHeader(), SIGNAL("sectionMoved(int, int, int)"), self.doRealColumnMove)
        self.connect(self.model(), SIGNAL("dataChanged(PyQt_PyObject, PyQt_PyObject)"), self.dataChanged)
    
    def getName(self):
        return self.name
    
    @staticmethod
    def getNameStatic(tableView):
        return tableView.name
    
    # returns True if insert succeeded, False otherwise
    def insertColumnLeft(self, currentVisualIndex, wave=0):
        if (wave == 0):
            name = self.mainWindow.waves.findGoodWaveName()
            wave = Wave(name)
            if self.mainWindow.waves.append(wave):
                return self.model().insertColumn(currentVisualIndex,  wave)
        else:
            return self.model().insertColumn(currentVisualIndex,  wave)
        return False
        
    def insertColumnRight(self, currentVisualIndex, wave=0):
        if (wave == 0):
            name = self.mainWindow.waves.findGoodWaveName()
            wave = Wave(name)
            if self.mainWindow.waves.append(wave):
                return self.model().insertColumn(currentVisualIndex + 1,  wave)
        else:
            return self.model().insertColumn(currentVisualIndex + 1,  wave)
        return False
    
    def renameWave(self, currentIndex):
        for i in range(0, 5):
            print self.model().headerData(i, Qt.Horizontal, Qt.DisplayRole).toString()
        currentWave = self.model().waves[currentIndex]
        renameWaveDialog = QtGui.QDialog()
        
        renameWaveSubWindow = QtGui.QMdiSubWindow()
        renameWaveSubWindow.setWidget(renameWaveDialog)
        renameWaveSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        
        renameWaveUi = Ui_RenameWaveDialog()
        renameWaveUi.setupUi(renameWaveDialog)
        renameWaveUi.oldWaveName.setText(currentWave.getName())
        self.mainWindow.ui.workspace.addSubWindow(renameWaveSubWindow)
        renameWaveDialog.setVisible(True)
        
        def saveRename():
            newName = str(renameWaveUi.newWaveNameLineEdit.text())
            if currentWave.rename(newName, self.mainWindow):
                renameWaveSubWindow.close()
                self.mainWindow.emit(SIGNAL("waveRenamed"))
            else:
                failedMessage = QtGui.QMessageBox()
                failedMessage.setText("Unable to rename wave.")
                failedMessage.exec_()
                renameWaveDialog.setVisible(True)
        
        def cancelRename():
            renameWaveSubWindow.close()
        
        # connect actions
        self.connect(renameWaveUi.buttonBox, SIGNAL("accepted()"), saveRename)
        self.connect(renameWaveUi.buttonBox, SIGNAL("rejected()"), cancelRename)
    
    def removeWaveFromTable(self, point):
        column = self.horizontalHeader().visualIndex(self.indexAt(point).column())
        self.model().removeColumn(self.model().waves[column])
        self.fullReset()
        
    def addWaveToTable(self, name, visualIndex):
        wave = self.mainWindow.waves.getWaveByName(name)
        if wave and not self.model().waves.getWaveByName(name):
            self.insertColumnRight(visualIndex, wave)
    
    def showColumnHeaderMenu(self, point):
        logicalIndex = self.horizontalHeader().logicalIndexAt(point)
        visualIndex = self.horizontalHeader().visualIndex(logicalIndex)
        print "lI: " + str(logicalIndex)
        print "vI: " + str(visualIndex)
        
        self.selectColumn(visualIndex)
        
        def insertColumnLeftHelper():
            self.insertColumnLeft(visualIndex)
        def insertColumnRightHelper():
            self.insertColumnRight(visualIndex)
        def renameWaveHelper():
            self.renameWave(logicalIndex)
        def removeWaveFromTableHelper():
            self.removeWaveFromTable(point)
        def removeWaveFromProjectHelper():
            self.removeWaveFromProject(logicalIndex)
        def addWaveToTableHelper(name):
            self.addWaveToTable(name, visualIndex)
            
        # get current list of waves for "add wave to table" menu
        self.addWaveMenu.clear()
        for wave in self.mainWindow.waves:
            self.addWaveMenu.addAction(AddWaveAction(wave.getName(), self.addWaveMenu))
        
        # connect actions
        self.connect(self.insertColumnLeftAction, SIGNAL("triggered()"), insertColumnLeftHelper)
        self.connect(self.insertColumnRightAction, SIGNAL("triggered()"), insertColumnRightHelper)
        self.connect(self.renameWaveAction, SIGNAL("triggered()"), renameWaveHelper)
        self.connect(self.removeWaveFromTableAction, SIGNAL("triggered()"), removeWaveFromTableHelper)
        self.connect(self.removeWaveFromProjectAction, SIGNAL("triggered()"), removeWaveFromProjectHelper)
        for waveAction in self.addWaveMenu.actions():
            self.connect(waveAction, SIGNAL("addWaveClicked"), addWaveToTableHelper)
        
        self.columnHeaderMenu.exec_(self.mapToGlobal(point))
        
        # disconnect actions.  we need to do this or else there will be multiple connections
        # when we open the menu again, and the old connections will have strange visualIndex values
        self.disconnect(self.insertColumnLeftAction, SIGNAL("triggered()"), insertColumnLeftHelper)
        self.disconnect(self.insertColumnRightAction, SIGNAL("triggered()"), insertColumnRightHelper)
        self.disconnect(self.renameWaveAction, SIGNAL("triggered()"), renameWaveHelper)
        self.disconnect(self.removeWaveFromTableAction, SIGNAL("triggered()"), removeWaveFromTableHelper)
        self.disconnect(self.removeWaveFromProjectAction, SIGNAL("triggered()"), removeWaveFromProjectHelper)
        for waveAction in self.addWaveMenu.actions():
            self.disconnect(waveAction, SIGNAL("addWaveClicked"), addWaveToTableHelper)
        

    def setupColumnHeaderMenu(self):
        header = self.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.connect(header, SIGNAL("customContextMenuRequested(QPoint)"), self.showColumnHeaderMenu)
        
        self.columnHeaderMenu = QtGui.QMenu(self)
        
        # create actions
        self.renameWaveAction = QtGui.QAction("Rename Wave", self.columnHeaderMenu)
        self.insertColumnLeftAction = QtGui.QAction("Insert Column to Left", self.columnHeaderMenu)
        self.insertColumnRightAction = QtGui.QAction("Insert Column to Right", self.columnHeaderMenu)
        self.removeWaveFromTableAction = QtGui.QAction("Remove Wave from Table", self.columnHeaderMenu)
        self.removeWaveFromProjectAction = QtGui.QAction("Remove Wave from Project", self.columnHeaderMenu)
        
        # create "add wave to table" menu
        self.addWaveMenu = QtGui.QMenu("Add Wave to Table", self.columnHeaderMenu)
        
        # add actions to menu
        self.columnHeaderMenu.addAction(self.addWaveMenu.menuAction())
        self.columnHeaderMenu.addAction(self.insertColumnLeftAction)
        self.columnHeaderMenu.addAction(self.insertColumnRightAction)
        self.columnHeaderMenu.addAction(self.renameWaveAction)
        self.columnHeaderMenu.addAction(self.removeWaveFromTableAction)
        self.columnHeaderMenu.addAction(self.removeWaveFromProjectAction)
        
    # we want to actually move the columns around in the model, not the view
    # to do this, we need to move the columns in the model then wipe the model from the view and add it back in
    # because view.reset() doesn't reset the logical indices of the view
    def doRealColumnMove(self,  logicalIndex,  oldVisualIndex,  newVisualIndex):
        self.model().moveColumn(oldVisualIndex, newVisualIndex)
        self.fullReset()

    def fullReset(self):
        print "fullReset"
        tmpModel = self.model()
        self.setModel(DataTableModel())
        self.setModel(tmpModel)
        self.reset()
        return True
    
    # move to next row in column and continue editing
    def dataChanged(self,  topLeft,  bottomRight):
        ind = self.model().createIndex(topLeft.row() + 1, topLeft.column())
        self.setCurrentIndex(ind)
        self.edit(ind)
        
#    # catch specific key press events
#    def keyPressEvent(self, event):
#        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
#            print "asdf"
#        else:
#            QtGui.QTableView.keyPressEvent(self, event)
        
        
    def printAllHeaders(self,  logicalIndex):
        for i in range(len(self.model().waves)):
            print "vis: " + str(i) + ", log: " + str(self.horizontalHeader().logicalIndex(i)) + ", name: " + self.model().waves[self.horizontalHeader().logicalIndex(i)].getName()
        print
        for i in range(len(self.model().waves)):
            print "log: " + str(i) + ", vis: " + str(self.horizontalHeader().visualIndex(i)) + ", name: " + self.model().waves[i].getName()
        print
    
