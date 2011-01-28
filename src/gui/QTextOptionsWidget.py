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


from PyQt4.QtGui import QWidget, QDialogButtonBox

from QEditFigureSubWidget import *
from Property import *
import Util

class QTextOptionsWidget(QEditFigureSubWidget):

    properties = TextOptions.default.keys()

    def __init__(self, textOptionsButton, *args):
        QEditFigureSubWidget.__init__(self, *args)
        self.setTextOptionsButton(textOptionsButton)
        
    def textOptionsButton(self):
        return self._textOptionsButton

    def setTextOptionsButton(self, button):
        self._textOptionsButton = button

    def saveUi(self):
        newOptions = {}
        
        for option in self.textOptionsButton().getTextOptions().get().keys():
            newOptions[option] = Util.getWidgetValue(self.getChild(option))


        # If rotation is custom (i.e. an angle has been specified) then we need to
        # overwrite what was just added
        if Util.getWidgetValue(self.getChild('rotation')) == 'custom':
            newOptions['rotation'] = Util.getWidgetValue(self.getChild('rotationCustom'))

        self.textOptionsButton().setTextOptions(newOptions)

    def resetUi(self):
        """Reset the textOptions dialog to the textOptions in the button."""
        
        textOptions = self.textOptionsButton().getTextOptions().get()
        for (option, value) in textOptions.items():
            Util.setWidgetValue(self.getChild(option), value.get())

        # If rotation is custom (i.e. an angle has been specified) then we need to
        # use that instead. An exception will be raised if the rotation option is not
        # a float, in which case we have already set it correctly above.
        try:
            angle = float(textOptions['rotation'].get())
            Util.setWidgetValue(self.getChild('rotation'), 'custom')
            Util.setWidgetValue(self.getChild('rotationCustom'), angle)
        except:
            pass

    def okClicked(self):
        self.saveUi()
        self.textOptionsButton().hideTextOptionsWidget()
    
    def cancelClicked(self):
        self.resetUi()
        self.textOptionsButton().hideTextOptionsWidget()

    def resetClicked(self):
        self.resetUi()

    def rotationBoxHandler(self, text):
        """
        Either enable or disable the custom rotation value spinbox, depending
        on the value in the rotation combo box.
        """

        if text == 'custom':
            self.getChild('rotationCustom').setEnabled(True)
        else:
            self.getChild('rotationCustom').setEnabled(False)

