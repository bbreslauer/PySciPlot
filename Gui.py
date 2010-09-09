from PyQt4.QtGui import QPushButton, QColor, QColorDialog

from DialogSubWindow import DialogSubWindow

import Util

class QColorButton(QPushButton):
    """A push button that is used to select a color."""

    def setColor(self, color):
        """
        Set the color of this button.  This will both set the background
        color as well as set the text to the rgb hex value.
        """
        
        _type = type(color).__name__
        if _type == "QColor":
            colorText = color.name()
        else:
            colorText = color

        self.setStyleSheet("background-color: " + colorText + "; color: " + Util.goodTextColor(colorText))
        self.setText(colorText)

    def createColorDialog(self):
        """
        Create a dialog box to select a color.
        """

        newColor = QColorDialog.getColor(QColor(str(self.text())))
        if newColor.isValid():
            self.setColor(newColor)


class DataTableSubWindow(DialogSubWindow):
    pass

class FigureSubWindow(DialogSubWindow):
    pass



