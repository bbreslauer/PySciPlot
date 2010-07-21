# Utility functions

from Exceptions import UnknownWidgetTypeError

def setWidgetValue(widget, value):
    """
    Assigns the value to the widget, often in the text field.
    """

    widgetType = type(widget).__name__
    
    # This dictionary simulates enough of a switch statement
    dictionary = {
                    'QLineEdit': widget.setText(str(value)),
                 }

    if widgetType in dictionary.keys():
        return dictionary[widgetType]
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
                    'QLineEdit': str(widget.text()),
                 }

    if widgetType in dictionary.keys():
        return dictionary[widgetType]
    else:
        raise UnknownWidgetTypeError(widgetType)




