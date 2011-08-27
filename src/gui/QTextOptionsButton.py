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


from PySide.QtGui import QPushButton, QDialogButtonBox, QColor, QApplication

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
    

