# Utility functions

from Exceptions import UnknownWidgetTypeError

def setWidgetValue(widget, value):
    """
    Assigns the value to the widget, often in the text field.
    """

    widgetType = type(widget).__name__
    
    if widgetType == 'QLineEdit':
        widget.setText(str(value))
    else:
        raise UnknownWidgetTypeError

    return True



def getWidgetValue(widget):
    """
    Returns the value from the widget.
    """

    widgetType = type(widget).__name__
    
    if widgetType == 'QLineEdit':
        return str(widget.text())
    else:
        raise UnknownWidgetTypeError




