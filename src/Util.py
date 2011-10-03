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


# Utility functions

import config, numpy

from PySide.QtCore import Qt
from PySide.QtGui import QColor, QApplication

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
                    'QWaveLimitSpinBox':       'widget.setValue(int(value))',
                    'QWaveStartSpinBox':       'widget.setValue(int(value))',
                    'QWaveEndSpinBox':       'widget.setValue(int(value))',
                    'QDoubleSpinBox': 'widget.setValue(float(value))',
                    'QColorButton':   'widget.setColor(value)',
                    'QTextOptionsButton':    'widget.setTextOptions(value)',
                    'QCheckBox':      'widget.setChecked(value)',
                    'QRadioButton':   'widget.setChecked(value)',
                    'QComboBox':      'widget.setCurrentIndex(widget.findText(str(value)))',
                    'QWaveComboBox':      'widget.setCurrentIndex(widget.findText(str(value)))',
                    'QGroupBox':      'widget.setChecked(value)',
                    'QListWidget':    'widget.setCurrentItem((widget.findItems(str(value), Qt.MatchExactly) or [widget.item(0)])[0])',
                    'QButtonGroup':   'pass',
                 }

    if widgetType in dictionary.keys():
        return eval(dictionary[widgetType])
    else:
        raise UnknownWidgetTypeError(widgetType + ': ' + str(value))

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
                    'QWaveLimitSpinBox':       'int(widget.value())',
                    'QWaveStartSpinBox':       'int(widget.value())',
                    'QWaveEndSpinBox':       'int(widget.value())',
                    'QDoubleSpinBox': 'float(widget.value())',
                    'QColorButton':   'widget.getColorTuple()',
                    'QTextOptionsButton':    'widget.getTextOptions()',
                    'QCheckBox':      'widget.isChecked()',
                    'QRadioButton':   'widget.isChecked()',
                    'QComboBox':      'str(widget.currentText())',
                    'QWaveComboBox':      'str(widget.currentText())',
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


def subdivideList(l, subDivider):
    """
    Create a new list with subDivider equally-spaced entries between 
    every two consecutive entries in l.

    l - must be a list of numbers
    subDivider - float or int
    """

    newList = []

    # We don't want to loop for the last entry in the list
    for index in range(len(l) - 1):
        newList.extend(list(numpy.linspace(l[index], l[index+1], num=subDivider+1, endpoint=False)))
    
    newList.append(float(l[-1]))

    return newList

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

