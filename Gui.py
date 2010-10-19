from PyQt4.QtGui import QPushButton, QColor, QColorDialog, QFont, QFontDialog, QDialog, QDialogButtonBox, qApp, QApplication

import matplotlib.font_manager as fm

from DialogSubWindow import DialogSubWindow
from ui.Ui_FontDialog import Ui_FontDialog

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

class QFontButton(QPushButton):
    """A push button that is used to select a font."""
    
    defaultFont = {     'name': 'Bitstream Vera Sans',
                        'style': 'normal',
                        'variant': 'normal',
                        'stretch': 100,
                        'weight': 100,
                        'size': 12
                    }
    
    def __init__(self, *args):
        QPushButton.__init__(self, *args)

        self.font = self.defaultFont

        # Create dialog
        self._dialog = QDialog()
        self._ui = Ui_FontDialog()
        self._ui.setupUi(self._dialog)
        
        self._window = DialogSubWindow(QApplication.instance().window.ui.workspace)
        self._window.setWidget(self._dialog)
        self._dialog.setParent(self._window)
        
        self.hideFontDialog()
        
        # Create font list from matplotlib fonts
        fontPropList = fm.createFontList(fm.findSystemFonts())
        
        # Get just the names
        fontList = map(lambda x:x.name, fontPropList)
        
        # Unique and sort the names
        fontList = list(set(fontList))
        fontList.sort()
        
        # Enter fonts into the ui widget
        self._ui.fontName.addItems(fontList)
        
        
        # Connect slots
        self._ui.buttons.button(QDialogButtonBox.Ok).clicked.connect(self.okClicked)
        self._ui.buttons.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelClicked)
    
    def setUiFont(self, font):
        """
        font is a dict of values related to the matplotlib font values.
        """
        
        Util.setWidgetValue(self._ui.fontName, font['name'])
        Util.setWidgetValue(self._ui.style, font['style'])
        Util.setWidgetValue(self._ui.variant, font['variant'])
        Util.setWidgetValue(self._ui.weight, font['weight'])
        Util.setWidgetValue(self._ui.stretch, font['stretch'])
        Util.setWidgetValue(self._ui.size, font['size'])
    
    def getUiFont(self):
        font = {}
        font['name'] = Util.getWidgetValue(self._ui.fontName)
        font['style'] = Util.getWidgetValue(self._ui.style)
        font['variant'] = Util.getWidgetValue(self._ui.variant)
        font['weight'] = Util.getWidgetValue(self._ui.weight)
        font['stretch'] = Util.getWidgetValue(self._ui.stretch)
        font['size'] = Util.getWidgetValue(self._ui.size)
        
        return font
        
    def getFont(self):
        return self.font
        
    def setFont(self, font):
        if font == {}:
            self.font = self.defaultFont
        else:
            self.font = font
    
    def showFontDialog(self):
        """
        Create a dialog box to select a font.
        """
        
        self.resetUi()
        self._window.show()
    
    def hideFontDialog(self):
        self._window.hide()
    
    def cancelClicked(self):
        self.resetUi()
        self.hideFontDialog()
    
    def okClicked(self):
        self.font = self.getUiFont()
        self.hideFontDialog()

    def resetUi(self):
        """Reset the font dialog to the font in this button."""
        
        self.setUiFont(self.font)


class DataTableSubWindow(DialogSubWindow):
    pass

class FigureSubWindow(DialogSubWindow):
    pass



