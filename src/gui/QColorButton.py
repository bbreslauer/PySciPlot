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


from PyQt4.QtGui import QPushButton, QColor, QColorDialog, QApplication

import Util, Property

class QColorButton(QPushButton):
    """
    A push button that is used to select a color.
    
    The internal color is represented by a QColor object.
    """
    
    def __init__(self, *args):
        QPushButton.__init__(self, *args)

        self._app = QApplication.instance().window

        # Define the internal color
        self.color = QColor('#ffffff')
        
        self.updateButtonColorsAndText()
    
    def getQColor(self):
        """Return the QColor object representing the currently selected color."""
        return self.color

    def getColorHex(self):
        """Return #rrggbb for the currently selected color."""
        return str(self.getQColor().name())

    def setColor(self, color):
        """
        Change the color of this button. This will both set the background
        color of the button as well as set the text color to an appropriate value.
        
        color should be a QColor, but can also be a Property.Color

        Returns False if assignment failed, True if assignment succeeded.
        """

        if isinstance(color, QColor):
            self.color = color
        elif isinstance(color, Property.Color):
            self.color = color.get()
        else:
            return False

        self.updateButtonColorsAndText()

    def initButtonColor(self):
        # See if the button (from the already-constructed UI) already has a
        # value that we should use
        splitText = str(self.text()).rpartition('(') # [2] now has "0,0,0,0)"
        splitText = splitText[2].rpartition(')') # [0] now has "0,0,0,0"
        textDefinedColor = splitText[0].split(',') # this now has a list of the four rgba values
        textDefinedColor = map(int, textDefinedColor)
        
        # If textDefinedColor is a valid list for QColor(), then use
        # it. If it is not, the QColor() constructor will do fail
        # and we will still have our original color.
        if len(textDefinedColor) in (3, 4):
            try:
                self.color = QColor(*textDefinedColor)
            except :
                pass

    def updateButtonColorsAndText(self):
        self.setStyleSheet("background-color: " + self.getColorHex() + "; color: " + Util.goodTextColor(self.getColorHex()))
        self.setText(str(self.getQColor().getRgb()))

    def createColorDialog(self):
        """
        Create a dialog box to select a color.
        """

        newColor = QColorDialog.getColor(self.getQColor(), self._app.ui.workspace, "Select Color", QColorDialog.ShowAlphaChannel)
        if newColor.isValid():
            self.setColor(newColor)



