from PyQt4.QtGui import QWidget, QDialogButtonBox, QFileDialog

import ConfigParser, os

import Util
from DialogSubWindow import DialogSubWindow
from ui.Ui_Preferences import Ui_Preferences

class Preferences():
    """
    Store preferences locally for easy programmatic access.

    Persistant copy of preferences will be stored in a file and loaded upon startup.
    User can modify preferences by opening UI, editing preferences, and saving them.
    By saving the preferences, the object will be updated to reflect the UI, and the
    file will also be updated.
    """

    prefs = {
            'defaultDirectory': ''
            }

    def __init__(self, app, fileName):
        self._app = app
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

        self._window = DialogSubWindow(self._app.ui.workspace)
        self._window.setWidget(self._widget)
        self._widget.setParent(self._window)

        self._window.hide()


    def get(self, variable):
        return self.prefs[variable]

    def setInternal(self, variable, value):
        self.prefs[variable] = value
        return True

    def showDialog(self):
        self.resetUi()
        self._window.show()

    def hideDialog(self):
        self.resetUi()
        self._window.hide()

    def loadPreferencesFile(self):
        """
        Read preferences from file into internal cache.
        If file cannot be found, return False
        """

        if os.path.isfile(self.preferencesFile):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.read(self.preferencesFile)

            for pref in self.prefs.keys():
                self.setInternal(pref, config.get('Preferences', str(pref)))

            return True
        return False
            
    def resetUi(self):
        """
        Update UI to the current internal cache of preferences.
        """

        for pref in self.prefs.keys():
            Util.setWidgetValue(vars(self._ui)[pref], self.get(pref))

    def savePreferences(self):
        """
        Save preferences to file and then read file to internal cache.
        Close dialog afterwards.
        """

        self.writePreferences()
        self.loadPreferencesFile()
        self.hideDialog()

    def writePreferences(self):
        """
        Write preferences to file from UI.
        """

        if os.path.isfile(self.preferencesFile) or not os.path.exists(self.preferencesFile):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.add_section('Preferences')

            for pref in self.prefs.keys():
                config.set('Preferences', str(pref), Util.getWidgetValue(vars(self._ui)[pref]))

            with open(self.preferencesFile, 'wb') as configFile:
                config.write(configFile)



    # Methods for specific preferences
    def defaultDirectorySelector(self):
        directory = QFileDialog.getExistingDirectory(self._app.ui.workspace, "Select Default Directory", "/")
        return Util.setWidgetValue(self._ui.defaultDirectory, directory)





