from PyQt4.QtGui import QPushButton, QDialogButtonBox, QColor, QApplication

import matplotlib.font_manager as fm

from gui.SubWindows import SubWindow
from ui.Ui_TextOptionsWidget import *
from gui.QTextOptionsWidget import *

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
        self._dialog = QTextOptionsWidget(self)
        self._ui = Ui_TextOptionsWidget()
        self._ui.setupUi(self._dialog)
        self._dialog.setUiObject(self._ui)

        self._window = SubWindow(self._app.ui.workspace)
        self._window.setWidget(self._dialog)
        self._dialog.setParent(self._window)
        
        self.hideTextOptionsWidget()
        
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
        return Property.TextOptions(self.textOptions)

    def setTextOptions(self, textOptions={}):
        """
        Set text options.
        """
        self.textOptions.set(textOptions)

    def showTextOptionsWidget(self):
        """
        Create a dialog box to select a font and text options.
        """
        
        self._dialog.resetUi()
        self._window.show()
    
    def hideTextOptionsWidget(self):
        self._window.hide()
    

