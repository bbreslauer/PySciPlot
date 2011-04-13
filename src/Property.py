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


from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import QColor
import copy

class Property(QObject):
    """
    Generic class to support simple property-holding types of data.  Examples
    of these could include Integers, Booleans, Colors, Fonts, and more.

    Any Property can emit the 'modified' signal.
    """
    
    # The Python type that corresponds to this Property class.
    castType = None

    # Signals
    modified = pyqtSignal()

    def __init__(self, *args):
        """
        Initialize the property.

        Set the default value for this property, and then set this property's
        value to the default.
        """

        QObject.__init__(self)
        
        # The actual value of this property.
        # We need to override the default initializer because when doing a deep
        # copy of a dict-of-properties, the property objects are still just copied
        # by reference. We need to copy their values, instead, so that we don't
        # have multiple dictionaries pointing to the same property.

        self._value = copy.deepcopy(self.default)
        if len(args) > 0:
            self.set(args[0])

    def __reduce__(self):
        """
        Method that is called when pickling the object.
        """
        return tuple([self.__class__, tuple([self.get()])])

    def __str__(self):
        """
        String representation of this property.
        """
        return "%s: value: %s" % (self.__class__, self.get())

    def __eq__(self, other):
        try:
            return self.get() == other.get()
        except:
            return self.get() == self.castType(other)

    def __ne__(self, other):
        try:
            return self.get() != other.get()
        except:
            return self.get() != self.castType(other)

    def __repr__(self):
        return self.__str__()

    def get(self):
        """
        Return the value of this property in the form of castType.
        """
        return self._value
    
    def getMpl(self):
        """Return the value of this property in a matplotlib compatible form."""
        return self.get()

    def set(self, newValue):
        """
        Set the value of this property to newValue.

        Returns true if the assignment succeeded. Returns false otherwise.

        Emits modified signal if the assignment succeeded and the new value was 
        different from the old value.
        """
        return self._set(newValue)

    def _set(self, newValue):
        """
        Cast newValue if necessary, then set variable to newValue.

        Equivalent to calling _castIfProperty, and then _setValue.

        This should not be considered a public method. Use set or setDefault instead.
        
        newValue is the value to set the variable to.

        Returns true if the assignment succeeded. Returns false otherwise.

        Emits modified signal if the assignment succeeded and the new value was 
        different from the old value.
        """

        # If newValue is a Property, run getValue() on it
        newValue = Property.getValue(newValue)
        
        # Do we need to do any last minute checking/scrubbing of the value
        # before casting it and setting it? If so, here is where we will do it
        newValue = self._validateValue(newValue)

        # Cast newValue to the appropriate Python type
        if self.castType not in (None, ""):
        #if self.castType not in (None, "") and not isinstance(newValue, self.castType):
            try:
                newValue = self.castType(newValue)
            except (ValueError, TypeError):
                return False

        # Finally, set the variable
        return self._setValue(newValue)

    def _setValue(self, newValue):
        """
        Set the property to newValue.
        
        This should not be considered a public method. Use set or setDefault instead.
        No type checking is done.
        
        newValue is the value to set the variable to. It defaults to self.default.

        Returns true if the assignment succeeded. Returns false otherwise.

        Emits modified signal if the assignment succeeded and the new value was 
        different from the old value.
        """

        if self._value != newValue:
            self._value = newValue
            self.modified.emit()
        else:
            return False
        return True

    def _validateValue(self, newValue):
        """
        Do any last-minute scrubbing of the value, to make sure that it is an
        appropriate type before applying it to the property.

        Defaults to doing nothing.

        This is an instance method, not static, because the subclass' method needs
        to be used, and the easiest way to determine which subclass to use is
        to use self.

        One example for the usefulness of this method is for the Boolean type, 
        where bool('False') == True, so we need to scrub this possible value
        and turn newValue from 'False' (a string) to False (a bool).
        """
        return newValue

    @staticmethod
    def getValue(arg):
        """
        Return the value in arg.
        
        If arg is a Property, return arg.get(). If arg is something else, 
        return arg.
        """

        if isinstance(arg, Property):
            return arg.get()
        return arg



#####################################################
#
# Individual properties
#
#####################################################

class Integer(Property):
    default = 0
    castType = int

class String(Property):
    default = ""
    castType = str

class Float(Property):
    default = 0.0
    castType = float

class Boolean(Property):
    default = False
    castType = bool

    def _validateValue(self, newValue):
        # bool('False') == True, because 'False' is a non-empty string, so
        # we need to check if newValue is a string, and if so, what its value is.
        if isinstance(newValue, str) and newValue.lower() in ('f', 'false'):
            newValue = False
        
        return newValue

class Dictionary(Property):
    default = dict()
    castType = dict

    def keys(self):
        return Property.get(self).keys()

    def _setValue(self, newValue):
        """
        First make sure that the new value is a dict.

        Then check if the internal value is a dict. If it is not, replace
        the internal value with the new value.

        If the internal value is already a dict, then instead of blindly 
        replacing the dictionary, we will update all the key/value entries
        that are in newValue. If at least one of them changes, then the
        modified signal will be emitted.
        """
        
        if not isinstance(newValue, dict):
            return False
        else:
            if not isinstance(self._value, dict) and not isinstance(self._value, Property):
                self._value = dict(newValue)
                self.modified.emit()
                return True
            else:
                isModified = False
                try:
                    currentKeys = self._value.keys()
                    for (key, value) in newValue.items():
                        # If there is an entry in newValue that does not exist in the current
                        # dictionary, then we throw it away
                        if key not in currentKeys:
                            continue

                        # Check if the value is going to be changed
                        if not isModified and value != self._value.get(key):
                            isModified = True
                        
                        self._setValueDictEntry(key, value)
            
                    if isModified:
                        self.modified.emit()
                    
                    return True
                except KeyError:
                    return False

    def _setValueDictEntry(self, key, value):
        """
        This is used to actually set the value. We abstract it to another method
        because if the dict entry is supposed to be a property, we need to set it
        via a set method rather than an =.
        """
        self._value[key] = value

class List(Property):
    default = []
    castType = list

class Color(Property):
    default = QColor()
    castType = QColor

    def getMpl(self):
        return self.get().getRgbF()
    
    def _validateValue(self, newValue):
        # The passed value could be one of the following:
        # QColor()
        # (f, f, f, f)    where f are floats between 0 and 1
        # (i, i, i, i)    where i are ints between 0 and 255
        #
        # The QColor constructor expects a QColor() or (i, i, i, i) passed to it
        # so if we get (f, f, f, f) we need to convert it
        if (isinstance(newValue, tuple) or isinstance(newValue, list)) and isinstance(newValue[0], float):
            newValue = map(lambda x: int(x * 255), newValue)

        return newValue

class SymbolString(String):
    default = ""

    symbols = {}

    def getMpl(self):
        """Convert from a word to a character representation of the line style."""
        return self.symbols[self.get()]

class AxisScaleType(SymbolString):
    default = "Linear"

    symbols = {
            'Linear': 'linear',
            'Logarithmic': 'log',
            'Symmetric Log': 'symlog',
        }

class Options(Dictionary):
    """
    This is a special type of dictionary, specifically one whose
    values are Property's.
    """

    def getMpl(self):
        """Convert the dictionary from properties to python types."""
        mplDict = {}

        for (key, value) in self.get().items():
            mplDict[key] = value.getMpl()

        return mplDict

    def _setValueDictEntry(self, key, value):
        self._value[key].set(value)
        
class TextOptions(Options):
    default = { 
        'name':                  String('Bitstream Vera Sans'),
        'style':                 String('normal'),
        'variant':               String('normal'),
        'stretch':               Integer(100),
        'weight':                Integer(100),
        'size':                  Integer(12),
        'color':                 Color(QColor(0,0,0,255)),
        'backgroundcolor':       Color(QColor(255,255,255,0)),
        'alpha':                 Float(1.0),
        'horizontalalignment':   String('center'),
        'verticalalignment':     String('center'),
        'linespacing':           Float(1.2),
        'rotation':              String('horizontal'),
    }

class GenericAxis(Options):
    default = {
        'autoscale':          Boolean(True),
        'minimum':            Float(-10),
        'maximum':            Float(10),
        'scaleType':          AxisScaleType('Linear'),
        'label':              String(''),
        'labelFont':          TextOptions({'verticalalignment': 'top'}),
        'visible':            Boolean(True),

        'majorTicksVisible':                    Boolean(True),
        'useMajorTicksAnchor':                  Boolean(False),
        'useMajorTicksSpacing':                 Boolean(False),
        'useMajorTicksNumber':                  Boolean(True),
        'useMajorTicksWaveValues':              Boolean(False),
        'majorTicksAnchor':                     Float(0),
        'majorTicksSpacing':                    Float(2),
        'majorTicksNumber':                     Integer(5),
        'majorTicksWaveValues':                 String(''),
        'majorTicksLabelVisible':               Boolean(True),
        'majorTicksLabelUseNumeric':            Boolean(True),
        'majorTicksLabelUseWave':               Boolean(False),
        'majorTicksLabelNumericFormat':         String('%.2g'),
        'majorTicksLabelWave':                  String(''),
        'majorTicksLabelFont':                  TextOptions({'verticalalignment': 'top'}),
        'majorTicksLabelPadding':               Integer(4),
        'majorTicksDirection':                  String('in'),
        'majorTicksColor':                      Color(QColor(0,0,0,255)),
        'majorTicksLength':                     Integer(4),
        'majorTicksWidth':                      Integer(1),
        #'majorTicksDisplayPrimary':             Boolean(True),
        #'majorTicksDisplaySecondary':           Boolean(True),
        #'majorTicksLabelDisplayPrimary':        Boolean(True),
        #'majorTicksLabelDisplaySecondary':      Boolean(False),
        'majorTicksLogBase':                    Float(10),
        'majorTicksLogLocations':               String('1'),
        
        'minorTicksVisible':                    Boolean(True),
        'minorTicksNumber':                     Integer(5),
        'minorTicksDirection':                  String('in'),
        'minorTicksColor':                      Color(QColor(0,0,0,255)),
        'minorTicksLength':                     Integer(2),
        'minorTicksWidth':                      Integer(1),
        #'minorTicksDisplayPrimary':             Boolean(True),
        #'minorTicksDisplaySecondary':           Boolean(True),
        'minorTicksLogLocations':               String('1,2,3,4,5,6,7,8,9'),
    }

class Legend(Options):
    # a font is not so simple to add, because it uses the matplotlib FontProperties class
    # instead of just a dict of values
    default = {
        'loc':              String('none'),
        'title':            String(''),
        'frameon':          Boolean(True),
        'fancybox':         Boolean(False),
        'shadow':           Boolean(False),
        'ncol':             Integer(1),
        'borderpad':        Float(0.3),
        'labelspacing':     Float(0.5),
        'handlelength':     Float(2.0),
        'handletextpad':    Float(0.5),
        'borderaxespad':    Float(0.5),
        'columnspacing':    Float(1.0),
        'markerscale':      Float(1.0),
    }


class LineStyle(SymbolString):
    default = "Solid"

    symbols = {
            'None': '',
            'Solid': '-',
            'Dashed': '--',
            'Dash Dot': '-.',
            'Dotted': ':',
        }

class PointMarker(SymbolString):
    default = "Point"

    symbols = {
            'None': '',
            'Point': '.',
            'Pixel': ',',
            'Circle': 'o',
            'Triangle - Down': 'v',
            'Triangle - Up': '^',
            'Triangle - Left': '<',
            'Triangle - Right': '>',
            'Y - Down': '1',
            'Y - Up': '2',
            'Y - Left': '3',
            'Y - Right': '4',
            'Square': 's',
            'Pentagon': 'p',
            'Star': '*',
            'Hexagon 1': 'h',
            'Hexagon 2': 'H',
            'Plus': '+',
            'X': 'x',
            'Diamond': 'D',
            'Thin Diamond': 'd',
            'Vertical Line': '|',
            'Horizontal Line': '_',
        }





