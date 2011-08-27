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


from PySide.QtGui import QWidget, QDialog, QMessageBox, QFrame, QApplication
from PySide.QtCore import Qt

from models.StoredSettingsModel import *
from ui.Ui_StoredSettingsName import *

import Util

class QStoredSettingsWidget(QFrame):

    def __init__(self, propertyWidget, parentButton, *args):
        """
        propertyWidget is the specific widget that the properties will be applied to.
        So when a user selects a set of properties from the list, they will be applied
        to the widget defined in propertyWidget.
        """
        QFrame.__init__(self, *args)
        self._app = QApplication.instance().window
        self.setPropertyWidget(propertyWidget)
        self._parentButton = parentButton

    def initSubWidgets(self):
        # Set up model and view
        self.storedSettingsModel = StoredSettingsModel(self._widgetName)
        self.getChild('storedSettingsView').setModel(self.storedSettingsModel)

    def getChild(self, name):
        return self.findChild(QWidget, name)

    def propertyWidget(self):
        return self._propertyWidget

    def setPropertyWidget(self, propertyWidget):
        self._propertyWidget = propertyWidget
        self._widgetName = propertyWidget.__class__.__name__

    def saveClicked(self):
        properties = self.propertyWidget().getCurrentUi()
        if self._widgetName not in self._app.storedSettings().keys():
            self._app.storedSettings()[self._widgetName] = []

        # Get the name the user wants to use
        nameDialog = QDialog(self)
        nameUi = Ui_StoredSettingsName()
        nameUi.setupUi(nameDialog)

        def saveSettings():
            name = Util.getWidgetValue(nameUi.name)
            name = name.strip()
            if name == "":
                failedMessage = QMessageBox(nameDialog)
                failedMessage.setText("Cannot use a blank name.")
                failedMessage.exec_()
            else:
                self._app.storedSettings()[self._widgetName].append([name, properties])
                nameDialog.close()

        def cancelSettings():
            nameDialog.close()

        nameUi.buttons.accepted.connect(saveSettings)
        nameUi.buttons.rejected.connect(cancelSettings)

        nameDialog.exec_()

        self.storedSettingsModel.doReset()
        
    def loadClicked(self):
        try:
            properties = self.getChild('storedSettingsView').selectedIndexes()[0].internalPointer()[1]
            self.propertyWidget().setCurrentUi(properties)
        except IndexError:
            pass

        self._parentButton.toggleWidget(False)

    def deleteClicked(self):
        try:
            self._app.storedSettings()[self._widgetName].remove(self.getChild('storedSettingsView').selectedIndexes()[0].internalPointer())
        except IndexError:
            pass

        self.storedSettingsModel.doReset()

    def resetGeometry(self):
        self.setGeometry(self._parentButton.x() - self.width(), self._parentButton.y(), self.width(), self._parentButton.height())



