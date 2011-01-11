from PyQt4.QtGui import QDialog, QWidget, QDialogButtonBox

import Util

class QTextOptionsDialog(QDialog):

    def __init__(self, textOptionsButton, *args):
        QDialog.__init__(self, *args)
        self.setTextOptionsButton(textOptionsButton)
        
    def setUiObject(self, ui):
        self._ui = ui

    def textOptionsButton(self):
        return self._textOptionsButton

    def setTextOptionsButton(self, button):
        self._textOptionsButton = button

    def getChild(self, name):
        try:
            return vars(self._ui)[name]
        except:
            return self.findChild(QWidget, name)

    def saveUi(self):
        textFormat = self.textOptionsButton().textFormat
        for option in textFormat.options():
            textFormat.set(option, Util.getWidgetValue(self.getChild(option)))

        # If rotation is custom (i.e. an angle has been specified) then we need to
        # overwrite what was just added
        if Util.getWidgetValue(self.getChild('rotation')) == 'custom':
            textFormat.set('rotation', Util.getWidgetValue(self.getChild('rotationCustom')))

    def resetUi(self):
        """Reset the textOptions dialog to the textOptions in the button."""
        textOptionsButton = self.textOptionsButton()

        for option in textOptionsButton.textFormat.options():
            Util.setWidgetValue(self.getChild(option), textOptionsButton.getOption(option).get())

        # If rotation is custom (i.e. an angle has been specified) then we need to
        # use that instead. An exception will be raised if the rotation option is not
        # a float, in which case we have already set it correctly above.
        try:
            angle = float(textOptionsButton.getOption('rotation').get())
            Util.setWidgetValue(self.getChild('rotation'), 'custom')
            Util.setWidgetValue(self.getChild('rotationCustom'), angle)
        except:
            pass


    def okClicked(self):
        self.saveUi()
        self.textOptionsButton().hideTextOptionsDialog()
    
    def cancelClicked(self):
        self.resetUi()
        self.textOptionsButton().hideTextOptionsDialog()

    def resetClicked(self):
        self.resetUi()

    def buttonClickHandler(self, button):
        standardButton = self.getChild('buttons').standardButton(button)
        if standardButton == QDialogButtonBox.Ok:
            self.okClicked()
        elif standardButton == QDialogButtonBox.Cancel:
            self.cancelClicked()
        elif standardButton == QDialogButtonBox.Reset:
            self.resetClicked()

    def rotationBoxHandler(self, text):
        """
        Either enable or disable the custom rotation value spinbox, depending
        on the value in the rotation combo box.
        """

        if text == 'custom':
            self.getChild('rotationCustom').setEnabled(True)
        else:
            self.getChild('rotationCustom').setEnabled(False)

