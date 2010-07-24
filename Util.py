# Utility functions

from Exceptions import UnknownWidgetTypeError

def setWidgetValue(widget, value):
    """
    Assigns the value to the widget, often in the text field.
    """

    widgetType = type(widget).__name__
    
    # This dictionary simulates enough of a switch statement
    dictionary = {
                    'QLineEdit': 'widget.setText(str(value))',
                    'QComboBox': 'widget.setCurrentIndex(widget.findText(str(value)))',
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

    # This dictionary simulates enough of a switch statement
    dictionary = {
                    'QLineEdit': 'str(widget.text())',
                    'QCheckBox': 'widget.isChecked()',
                    'QComboBox': 'str(widget.currentText())',
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

def findKey(dictionary, value):
    """
    Find the key in dictionary associated with value.
    """
    
    return [k for k, v in dictionary.iteritems() if v == value][0]
