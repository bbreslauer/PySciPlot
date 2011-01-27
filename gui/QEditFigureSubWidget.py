from PyQt4.QtGui import QWidget, QApplication, QDialogButtonBox

from Property import Property
import Util

class QEditFigureSubWidget(QWidget):

    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self._app = QApplication.instance().window

    def getChild(self, name):
        # findChild is more intensive, so we try the self._ui method first
        # but it might fail if self._ui is not set
        try:
            return vars(self._ui)[name]
        except:
            return self.findChild(QWidget, name)

    def setUiObject(self, ui):
        """Get a reference to the ui object, for easy access later."""
        self._ui = ui

    def setEditFigureDialogModule(self, module):
        self._editFigureDialogModule = module

    def getCurrentUi(self):
        """
        Take the current UI values and return them.
        """

        currentProperties = {}
        for property in self.properties:
            currentProperties[property] = Util.getWidgetValue(self.getChild(property))

        return currentProperties

    def setCurrentUi(self, properties):
        """
        Set the current UI to the pass properties.
        """

        for (key, value) in properties.items():
            if isinstance(value, Property):
                Util.setWidgetValue(self.getChild(key), value.get())
            else:
                Util.setWidgetValue(self.getChild(key), value)

    def saveUi(self):
        """Save the UI data to the current internal object."""
        pass

    def resetUi(self):
        """Set the UI to the current internal object's data."""
        pass

    def applyClicked(self):
        self.saveUi()

    def resetClicked(self):
        self.resetUi()

    def okClikced(self):
        pass

    def cancelClicked(self):
        pass

    def buttonClickHandler(self, button):
        standardButton = self.getChild('buttons').standardButton(button)
        if standardButton == QDialogButtonBox.Apply:
            self.applyClicked()
        elif standardButton == QDialogButtonBox.Reset:
            self.resetClicked()
        elif standardButton == QDialogButtonBox.Ok:
            self.okClicked()
        elif standardButton == QDialogButtonBox.Cancel:
            self.cancelClicked()


    def resizeEvent(self, event):
        QWidget.resizeEvent(self, event)

        # Resize the stored settings widget to the proper height
        # since it is floating and not in a layout.
        try:
            self.getChild('storedSettingsButton').storedSettingsWidget.resetGeometry()
        except AttributeError:
            # this widget has not been created yet
            pass
        





