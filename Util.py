# Utility functions

import config

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QColor, QApplication

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
                    'QTextOptionsButton':    'widget.setTextOptions(value)',
                    'QCheckBox':      'widget.setChecked(value)',
                    'QRadioButton':   'widget.setChecked(value)',
                    'QComboBox':      'widget.setCurrentIndex(widget.findText(str(value)))',
                    'QGroupBox':      'widget.setChecked(value)',
                    'QListWidget':    'widget.setCurrentItem((widget.findItems(str(value), Qt.MatchExactly) or [widget.item(0)])[0])',
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
                    'QColorButton':   'widget.getQColor()',
                    'QTextOptionsButton':    'widget.getTextFormat()',
                    'QCheckBox':      'widget.isChecked()',
                    'QRadioButton':   'widget.isChecked()',
                    'QComboBox':      'str(widget.currentText())',
                    'QGroupBox':      'widget.isChecked()',
                    'QButtonGroup':   'str(widget.checkedButton().text())',
                    'QListWidget':    'str(widget.currentItem().text())',
                 }

    if widgetType in dictionary.keys():
        return eval(dictionary[widgetType])
    else:
        raise UnknownWidgetTypeError(widgetType)

def goodTextColor(backgroundColor):
    """
    Determines whether complementary color should be white or black.
    """

    lightness = QColor(backgroundColor).lightnessF()
    if lightness > 0.4:
        return "#000000"
    return "#ffffff"


def frange(start, end=None, inc=None):
    """
    A range function that accepts float increments.
    """

    if end == None:
        end = start + 0.0
        start = 0.0
    else: start += 0.0 # force it to be a float

    if inc == None:
        inc = 1.0

    count = int((end - start) / inc)
    if start + count * inc != end:
        # count is always one short
        count += 1

    L = [None,] * count
    for i in xrange(count):
        L[i] = start + i * inc

    return L


def debug(level, caller, text):
    """
    Output the text if the given debug level is at or below the level
    given when the application was started. So if the user requests a
    debug level of 2, then all 0, 1, and 2 debug strings will be printed.
    """

    if level <= config.debugLevel:
        print "[%s] %s" % (caller, text)


def uniqueList(l):
    """
    Return a list with all unique entries.
    """

    s = set(l)
    return list(s)








