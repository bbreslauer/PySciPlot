from PyQt4.QtGui import QWidget, QApplication, QDialogButtonBox

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




