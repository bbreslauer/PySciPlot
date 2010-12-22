from PyQt4.QtGui import QPushButton, QColor, QColorDialog, QApplication

import Util

class QColorButton(QPushButton):
    """A push button that is used to select a color."""
    
    def __init__(self, *args):
        QPushButton.__init__(self, *args)
    
    def getPrefix(self):
        return str(self.text()).rpartition('#')[0]

    def getColor(self):
        splitText = str(self.text()).rpartition('#')
        return splitText[1] + splitText[2]

    def setColor(self, color):
        """
        Set the color of this button.  This will both set the background
        color as well as set the text to the rgb hex value.
        """
        
        colorText = '#ffffff'

        _type = type(color).__name__
        if _type == "QColor":
            colorText = color.name()
        else:
            colorText = color
        self.setStyleSheet("background-color: " + colorText + "; color: " + Util.goodTextColor(colorText))
        self.setText(str(self.getPrefix()) + str(colorText))

    def createColorDialog(self):
        """
        Create a dialog box to select a color.
        """

        newColor = QColorDialog.getColor(QColor(str(self.getColor())))
        if newColor.isValid():
            self.setColor(newColor)


