from PyQt4.QtGui import QWidget, QDialogButtonBox, QFileDialog, QApplication

import os

import xml.dom.minidom

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

    # These are the defaults for each preference. They will be overwritten
    # by the user's preferences at startup.
    prefs = {
            'projectDirectory': '~/',  # Dir for where to store project files
            'defaultDirectory': '~/',  # Dir for other purposes
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

        self._window = DialogSubWindow(self._app.ui.workspace)
        self._window.setWidget(self._widget)
        self._widget.setParent(self._window)

        self._window.hide()


    def getInternal(self, variable):
        return self.prefs[variable]

    def getUi(self, variable):
        return Util.getWidgetValue(vars(self._ui)[variable])

    def setInternal(self, variable, value):
        self.prefs[variable] = value
        return True
    
    def setUi(self, variable, value):
        return Util.setWidgetValue(vars(self._ui)[variable], value)

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
            dom = xml.dom.minidom.parse(self.preferencesFile)

            # root prefs element
            p = dom.documentElement
            
            # Load preferences from file
            child = p.firstChild
            while child is not None:
                if child.nodeType is xml.dom.minidom.Node.ELEMENT_NODE:
                    if child.nodeName in self.prefs.keys():
                        self.setInternal(child.nodeName, str(child.firstChild.data.strip()))

                child = child.nextSibling

            return True
        return False
            
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

        self.writePreferences()
        self.loadPreferencesFile()
        self.hideDialog()

    def writePreferences(self):
        """
        Write preferences to file from UI.
        """

        if os.path.isfile(self.preferencesFile) or not os.path.exists(self.preferencesFile):
            # Create document
            dom = xml.dom.minidom.Document()

            # Create root preferences element
            p = dom.createElement("Preferences")
            dom.appendChild(p)
            
            # Add each preference to dom
            for pref in self.prefs.keys():
                child = dom.createElement(pref)
                child.appendChild(dom.createTextNode(str(self.getUi(pref))))
                p.appendChild(child)

            with open(self.preferencesFile, 'w') as preferencesFile:
                dom.writexml(preferencesFile, indent='', addindent='  ', newl='\n')



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





