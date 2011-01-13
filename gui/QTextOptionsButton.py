from PyQt4.QtGui import QPushButton, QDialog, QDialogButtonBox, QColor, QApplication

import matplotlib.font_manager as fm

from DialogSubWindow import DialogSubWindow
from ui.Ui_TextOptionsDialog import *
from gui.QTextOptionsDialog import *

import Util, Property

class QTextOptionsButton(QPushButton):
    """A push button that is used to select a font and text options."""

    def __init__(self, *args):
        QPushButton.__init__(self, *args)
        self._app = QApplication.instance().window

        self.textOptions = Property.TextOptions()

        # Set initial textOptions values based on application preferences
        if 'preferences' in self._app.__dict__.keys():
            preferenceTextOptions = self._app.preferences.getInternal('textOptions')
            if preferenceTextOptions is not None:
                self.setTextOptions(preferenceTextOptions)

        # Create dialog
        self._dialog = QTextOptionsDialog(self)
        self._ui = Ui_TextOptionsDialog()
        self._ui.setupUi(self._dialog)
        self._dialog.setUiObject(self._ui)

        self._window = DialogSubWindow(self._app.ui.workspace)
        self._window.setWidget(self._dialog)
        self._dialog.setParent(self._window)
        
        self.hideTextOptionsDialog()
        
        # Create font list from matplotlib fonts
        fontPropList = fm.createFontList(fm.findSystemFonts())
        
        # Get just the names
        fontList = map(lambda x:x.name, fontPropList)
        
        # Unique and sort the names
        fontList = list(set(fontList))
        fontList.sort()
        
        # Enter fonts into the ui widget
        self._ui.name.addItems(fontList)
        
    def getOption(self, option):
        return self.textOptions.get()[option]

    def getTextOptions(self):
        return self.textOptions

    def setTextOptions(self, textOptions={}):
        """
        Set text options.
        """
        self.textOptions.set(textOptions)

    def showTextOptionsDialog(self):
        """
        Create a dialog box to select a font and text options.
        """
        
        self._dialog.resetUi()
        self._window.show()
    
    def hideTextOptionsDialog(self):
        self._window.hide()
    

