# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ben/programming/pysciplot-mpl/MainWindow.ui'
#
# Created: Fri Apr 16 22:40:58 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.workspace = QtGui.QMdiArea(self.centralwidget)
        self.workspace.setGeometry(QtCore.QRect(0, 0, 800, 555))
        self.workspace.setObjectName("workspace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtGui.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuPlot = QtGui.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionNew_Table = QtGui.QAction(MainWindow)
        self.actionNew_Table.setObjectName("actionNew_Table")
        self.actionManage_Waves = QtGui.QAction(MainWindow)
        self.actionManage_Waves.setObjectName("actionManage_Waves")
        self.actionManage_Tables = QtGui.QAction(MainWindow)
        self.actionManage_Tables.setObjectName("actionManage_Tables")
        self.actionShow_Waves = QtGui.QAction(MainWindow)
        self.actionShow_Waves.setObjectName("actionShow_Waves")
        self.actionCreate_Plot = QtGui.QAction(MainWindow)
        self.actionCreate_Plot.setObjectName("actionCreate_Plot")
        self.menuNew.addAction(self.actionNew_Table)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionShow_Waves)
        self.menuData.addAction(self.actionManage_Waves)
        self.menuPlot.addAction(self.actionCreate_Plot)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PySciPlot", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNew.setTitle(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlot.setTitle(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Table.setText(QtGui.QApplication.translate("MainWindow", "New Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Table.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_Waves.setText(QtGui.QApplication.translate("MainWindow", "Manage Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_Waves.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_Tables.setText(QtGui.QApplication.translate("MainWindow", "Manage Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Waves.setText(QtGui.QApplication.translate("MainWindow", "Show Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Plot.setText(QtGui.QApplication.translate("MainWindow", "Create Plot", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

