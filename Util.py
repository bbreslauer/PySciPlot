# Utility functions

from PyQt4.QtGui import QColor

from Exceptions import UnknownWidgetTypeError

def setWidgetValue(widget, value):
    """
    Assigns the value to the widget, often in the text field.
    """

    widgetType = type(widget).__name__
    
    # This dictionary simulates enough of a switch statement for our needs
    dictionary = {
                    'QLineEdit':      'widget.setText(str(value))',
                    'QSpinBox':       'widget.setValue(int(value))',
                    'QDoubleSpinBox': 'widget.setValue(float(value))',
                    'QColorButton':   'widget.setColor(value)',
                    'QCheckBox':      'widget.setChecked(value)',
                    'QComboBox':      'widget.setCurrentIndex(widget.findText(str(value)))',
                    'QButtonGroup':   'pass',
                 }

    if widgetType in dictionary.keys():
        return eval(dictionary[widgetType])
    else:
        raise UnknownWidgetTypeError(widgetType)

    return True


def getWidgetValue(widget):
    """
    Returns the value from the widget.
    """

    widgetType = type(widget).__name__

    # This dictionary simulates enough of a switch statement for our needs
    dictionary = {
                    'QLineEdit':      'str(widget.text())',
                    'QSpinBox':       'int(widget.value())',
                    'QDoubleSpinBox': 'float(widget.value())',
                    'QColorButton':   'str(widget.text())',
                    'QCheckBox':      'widget.isChecked()',
                    'QComboBox':      'str(widget.currentText())',
                    'QButtonGroup':   'str(widget.checkedButton().text())',
                 }

    if widgetType in dictionary.keys():
        return eval(dictionary[widgetType])
    else:
        raise UnknownWidgetTypeError(widgetType)


def fileDialogDirectory(app):
    """
    Set the initial directory for a QFileDialog to either the cwd or
    the default directory.
    """

    if app.cwd != "":
        return app.cwd
    else:
        return app.preferences.get("defaultDirectory")


def goodTextColor(backgroundColor):
        """Determines whether complementary color should be white or black."""
        lightness = QColor(backgroundColor).lightnessF()
        if lightness > 0.4:
            return "#000000"
        return "#ffffff"





