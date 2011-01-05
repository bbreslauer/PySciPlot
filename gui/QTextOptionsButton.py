from PyQt4.QtGui import QPushButton, QDialog, QDialogButtonBox, QApplication

import matplotlib.font_manager as fm

from DialogSubWindow import DialogSubWindow
from ui.Ui_TextOptionsDialog import Ui_TextOptionsDialog

import Util

class QTextOptionsButton(QPushButton):
    """A push button that is used to select a font and text options."""
    
    textOptionProperties = {'name':                 { 'type': str, 'default': 'Bitstream Vera Sans' },
                            'style':                { 'type': str, 'default': 'normal' },
                            'variant':              { 'type': str, 'default': 'normal' },
                            'stretch':              { 'type': int, 'default': 100 },
                            'weight':               { 'type': int, 'default': 100 },
                            'size':                 { 'type': int, 'default': 12 },
                            'color':                { 'type': str, 'default': '#000000' },
                            'backgroundcolor':      { 'type': str, 'default': '#ffffff' },
                            'horizontalalignment':  { 'type': str, 'default': 'center' },
                            'verticalalignment':    { 'type': str, 'default': 'center' },
                            'linespacing':          { 'type': float, 'default': 1.2 },
                            'rotation':             { 'type': str, 'default': 'horizontal' },
                         }

    def __init__(self, *args):
        QPushButton.__init__(self, *args)
        self._app = QApplication.instance().window

        self.textOptions = {}
        self.setTextOptions()

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
        self._ui.rotation.currentIndexChanged[str].connect(self.rotationBoxHandler)
    
    def setUiTextOptions(self, textOptions):
        """
        textOptions is a dict of values related to the matplotlib Text kwarg values.
        """
        
        for variable in self.textOptions.keys():
            Util.setWidgetValue(vars(self._ui)[variable], textOptions[variable])

    def getUiTextOptions(self):
        textOptions = {}

        for variable in self.textOptionProperties.keys():
            textOptions[variable] = Util.getWidgetValue(vars(self._ui)[variable])
    
        return textOptions
        
    def getTextOptions(self):
        return self.textOptions
        
    def setTextOptions(self, textOptions={}):
        """
        Set text options.

        This method will set every option in the textOptionProperties keys list.
        The following questions will be asked for each option (in order),
        and the first positive result will be used.

        1) Is the option passed to this method?
        2) Did the user set a preference for this option?
        3) Set the option to the default in this class.
        """

        # Start by getting some key lists, so we don't have to create the
        # lists multiple times
        passedKeys = textOptions.keys()
        doPreferencesExist = 'preferences' in self._app.__dict__.keys()
        if doPreferencesExist:
            preferenceKeys = self._app.preferences.getInternal('textOptions').keys()

        for prop in self.textOptionProperties.keys():
            if prop in passedKeys:
                pass
            elif doPreferencesExist and prop in preferenceKeys:
                textOptions[prop] = self._app.preferences.getInternal('textOptions')[prop]
            else:
                textOptions[prop] = self.textOptionProperties[prop]['default']

        self.textOptions = textOptions
    
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

    def rotationBoxHandler(self, text):
        """
        Either enable or disable the custom rotation value spinbox, depending
        on the value in the rotation combo box.
        """

        if text == 'custom':
            self._ui.rotationCustom.setEnabled(True)
        else:
            self._ui.rotationCustom.setEnabled(False)



