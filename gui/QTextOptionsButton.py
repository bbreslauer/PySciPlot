from PyQt4.QtGui import QPushButton, QDialog, QDialogButtonBox, QApplication

import matplotlib.font_manager as fm

from DialogSubWindow import DialogSubWindow
from ui.Ui_TextOptionsDialog import Ui_TextOptionsDialog

import Util

class QTextOptionsButton(QPushButton):
    """A push button that is used to select a font and text options."""
    
    defaultTextOptions = {  'name':             { 'type': str, 'default': 'Bitstream Vera Sans' },
                            'style':            { 'type': str, 'default': 'normal' },
                            'variant':          { 'type': str, 'default': 'normal' },
                            'stretch':          { 'type': int, 'default': 100 },
                            'weight':           { 'type': int, 'default': 100 },
                            'size':             { 'type': int, 'default': 12 },
                            'color':            { 'type': str, 'default': '#000000' },
                            'backgroundcolor':  { 'type': str, 'default': '#ffffff' },
                         }
    
    def __init__(self, *args):
        QPushButton.__init__(self, *args)
        self._app = QApplication.instance().window

        self.textOptions = {}
        self.setTextOptionsToDefaults()

        # Create dialog
        self._dialog = QDialog()
        self._ui = Ui_TextOptionsDialog()
        self._ui.setupUi(self._dialog)

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
        
        
        # Connect slots
        self._ui.buttons.button(QDialogButtonBox.Ok).clicked.connect(self.okClicked)
        self._ui.buttons.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelClicked)
        self._ui.buttons.button(QDialogButtonBox.Reset).clicked.connect(self.resetUi)
        self._ui.color.clicked.connect(self._ui.color.createColorDialog)
        self._ui.backgroundcolor.clicked.connect(self._ui.backgroundcolor.createColorDialog)
    
    def setUiTextOptions(self, textOptions):
        """
        textOptions is a dict of values related to the matplotlib Text kwarg values.
        """
        
        for variable in self.textOptions.keys():
            Util.setWidgetValue(vars(self._ui)[variable], textOptions[variable])

    def getUiTextOptions(self):
        textOptions = {}

        for variable in self.textOptions.keys():
            textOptions[variable] = Util.getWidgetValue(vars(self._ui)[variable])
    
        return textOptions
        
    def getTextOptions(self):
        return self.textOptions
        
    def setTextOptions(self, textOptions={}):
        if textOptions == {}:
            self.setTextOptionsToDefaults()
        else:
            self.textOptions = textOptions

    def setTextOptionsToDefaults(self):
        """
        Check for a value in user's preferences. If none exists, then go with the program's default.
        """

        for variable in self.defaultTextOptions.keys():
            if 'preferences' in self._app.__dict__.keys() and variable in self._app.preferences.getInternal('textOptions').keys():
                self.textOptions[variable] = self._app.preferences.getInternal('textOptions')[variable]
            else:
                self.textOptions[variable] = self.defaultTextOptions[variable]['default']
    
    def showTextOptionsDialog(self):
        """
        Create a dialog box to select a font and text options.
        """
        
        self.resetUi()
        self._window.show()
    
    def hideTextOptionsDialog(self):
        self._window.hide()
    
    def cancelClicked(self):
        self.resetUi()
        self.hideTextOptionsDialog()
    
    def okClicked(self):
        self.textOptions = self.getUiTextOptions()
        self.hideTextOptionsDialog()

    def resetUi(self):
        """Reset the textOptions dialog to the textOptions in this button."""
        
        self.setUiTextOptions(self.textOptions)

