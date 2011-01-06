from PyQt4.QtGui import QPushButton, QColor, QColorDialog, QApplication

import Util

class QColorButton2(QPushButton):
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



class QColorButton(QPushButton):
    """
    A push button that is used to select a color.
    
    The internal color is represented by a QColor object.
    """
    
    def __init__(self, *args):
        QPushButton.__init__(self, *args)

        self._app = QApplication.instance().window

        # Define the internal color
        self.setColor(QColor('#ffffff'))
    
    def getQColor(self):
        """Return the QColor object representing the currently selected color."""
        return self.color

    def getColor(self):
        """Return (r, g, b, a) for the currently selected color, as floats between 0 and 1."""
        return (str(self.getQColor().name()), float(self.getQColor().alphaF()))

    def getColorHex(self):
        """Return #rrggbb for the currently selected color."""
        return str(self.getQColor().name())

    def getRgbF(self):
        return self.getQColor().getRgbF()

    def setColor(self, color):
        """
        Change the color of this button. This will both set the background
        color of the button as well as set the text color to an appropriate value.

        color can be one of the following, where <> indicates optional argument:
        QColor
        (r, g, b, <a>) with values between 0 and 1
        [r, g, b, <a>] with values between 0 and 1
        #rrggbb
        """
        
        _type = type(color).__name__
        if _type == "QColor":
            self.color = color
        elif _type == "tuple" or _type == "list":
            scaledColor = [int(x*255) for x in color]
            self.color = QColor(*scaledColor)
        else:
            self.color = QColor(color)
        
        self.setStyleSheet("background-color: " + self.getColorHex() + "; color: " + Util.goodTextColor(self.getColorHex()))

    def createColorDialog(self):
        """
        Create a dialog box to select a color.
        """

        newColor = QColorDialog.getColor(self.getQColor(), self._app.ui.workspace, "Select Color", QColorDialog.ShowAlphaChannel)
        if newColor.isValid():
            self.setColor(newColor)



