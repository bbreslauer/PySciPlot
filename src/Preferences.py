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


from PySide.QtGui import QWidget, QDialogButtonBox, QFileDialog, QApplication

import os, pickle

import Util, Property
from gui.SubWindows import SubWindow
from ui.Ui_Preferences import Ui_Preferences

class Preferences():
    """
    Store preferences locally for easy programmatic access.

    Persistant copy of preferences will be stored in a file and loaded upon startup.
    User can modify preferences by opening UI, editing preferences, and saving them.
    By saving the preferences, the object will be updated to reflect the UI, and the
    file will also be updated.
    """

    # These are the defaults for each preference. They will be overwritten
    # by the user's preferences at startup.
    prefs = {
            'projectDirectory': Property.String('~/'),   # Dir for where to store project files
            'defaultDirectory': Property.String('~/'),   # Dir for other purposes
            'textOptions':      Property.TextOptions(),  # Default text options
            }

    def __init__(self, fileName):
        self._app = QApplication.instance().window
        self.preferencesFile = os.path.expanduser(fileName)

        self._widget = QWidget()
        self._ui = Ui_Preferences()
        self._ui.setupUi(self._widget)

        # Load preferences from file
        self.loadPreferencesFile()
        self.resetUi()
        
        # Connect button signals
        self._ui.buttons.button(QDialogButtonBox.Reset).clicked.connect(self.resetUi)
        self._ui.buttons.button(QDialogButtonBox.Save).clicked.connect(self.savePreferences)
        self._ui.buttons.button(QDialogButtonBox.Cancel).clicked.connect(self.hideDialog)
        self._ui.defaultDirectoryButton.clicked.connect(self.defaultDirectorySelector)
        self._ui.projectDirectoryButton.clicked.connect(self.projectDirectorySelector)
        #self._ui.textOptions.clicked.connect(self._ui.textOptions.showTextOptionsDialog)

        self._window = SubWindow(self._app.ui.workspace)
        self._window.setWidget(self._widget)
        self._widget.setParent(self._window)

        self._window.hide()


    def getInternal(self, variable):
        try:
            return self.prefs[variable].get()
        except:
            return None

    def getUi(self, variable):
        return Util.getWidgetValue(vars(self._ui)[variable])

    def setInternal(self, variable, value):
        return self.prefs[variable].set(value)
    
    def setUi(self, variable, value):
        return Util.setWidgetValue(vars(self._ui)[variable], value)

    def showDialog(self):
        self.resetUi()
        self._window.show()

    def hideDialog(self):
        self.resetUi()
        self._window.hide()

    def loadPreferencesFile(self):
        if os.path.isfile(self.preferencesFile):
            with open(self.preferencesFile, 'r') as fileHandle:
                self.prefs = pickle.load(fileHandle)
            
    def uiToInternal(self):
        """
        Copy the UI pref values to the internal prefs dict.
        """
        for pref in self.prefs.keys():
            self.setInternal(pref, self.getUi(pref))

    def resetUi(self):
        """
        Update UI to the current internal cache of preferences.
        """

        for pref in self.prefs.keys():
            self.setUi(pref, self.getInternal(pref))

    def savePreferences(self):
        """
        Save preferences to file and then read file to internal cache.
        Close dialog afterwards.
        """
        
        self.uiToInternal()
        self.writePreferences()
        self.loadPreferencesFile()
        self.hideDialog()

    def writePreferences(self):
        if os.path.isfile(self.preferencesFile) or not os.path.exists(self.preferencesFile):
            with open(self.preferencesFile, 'wb') as fileHandle:
                pickle.dump(self.prefs, fileHandle)



    # Methods for specific preferences
    def defaultDirectorySelector(self):
        directory = QFileDialog.getExistingDirectory(self._app.ui.workspace, "Select Default Directory", Util.getWidgetValue(self._ui.defaultDirectory))
        if os.path.isdir(directory):
            return self.setUi('defaultDirectory', directory)
        return False

    def projectDirectorySelector(self):
        directory = QFileDialog.getExistingDirectory(self._app.ui.workspace, "Select Project Directory", Util.getWidgetValue(self._ui.projectDirectory))
        if os.path.isdir(directory):
            return self.setUi('projectDirectory', directory)
        return False





