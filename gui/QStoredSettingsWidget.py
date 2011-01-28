from PyQt4.QtGui import QWidget, QFrame, QApplication
from PyQt4.QtCore import Qt

from models.StoredSettingsModel import *

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
        self._app.storedSettings()[self._widgetName].append(['New Setting', properties])
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



