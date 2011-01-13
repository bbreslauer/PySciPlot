from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import QColor

import Type

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
        
        # The default value for this property. The default value could be different
        # per instance, which is why this is not an instance attr. The first args 
        # passed to __init__ will be assigned to self.default.
        self.default = None
        
        # The actual value of this property.
        self.value = None

        if len(args) > 0:
            self.setDefault(args[0])

        self.reset()

    def __reduce__(self):
        """
        Method that is called when pickling the object.
        """
        return tuple([self.__class__, tuple([self.get()])])

    def __str__(self):
        """
        String representation of this property.
        """
        return "%s: default: %s, value: %s" % (self.__class__, self.getDefault(), self.get())

    def __repr__(self):
        return self.__str__()

    def get(self, variable='value'):
        """
        Return the value of this property in the form of castType.
        """
        if variable == 'value':
            return self.value
        elif variable == 'default':
            return self.default
        return None
    
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
        return self._set('value', newValue)

    def getDefault(self):
        """Return the default value for this property in the form of castType."""
        return self.get('default')

    def setDefault(self, newDefault):
        """
        Set the default value of this property.

        Returns true if the assignment succeeded. Returns false otherwise.

        Emits modified signal if the assignment succeeded and the new value was 
        different from the old value.
        """
        return self._set('default', newDefault)

    def reset(self):
        """Reset the value of this property to the default."""
        return self.set(self.getDefault())

    def _set(self, variable, newValue):
        """
        Cast newValue if necessary, then set variable to newValue.

        Equivalent to calling _castIfProperty, and then _setVariable.

        This should not be considered a public method. Use set or setDefault instead.
        
        variable should be either 'value' or 'default'.
        newValue is the value to set the variable to.

        Returns true if the assignment succeeded. Returns false otherwise.

        Emits modified signal if the assignment succeeded and the new value was 
        different from the old value.
        """

        # If newValue is a Property, run getValue() on it
        newValue = Property.getValue(newValue)
        
        # Do we need to do any last minute checking/scrubbing of the value
        # before casting it and setting it? If so, here is where we will do it
        newValue = self._validateValue(variable, newValue)

        # Cast newValue to the appropriate Python type
        if self.castType not in (None, ""):
        #if self.castType not in (None, "") and not isinstance(newValue, self.castType):
            try:
                newValue = self.castType(newValue)
            except (ValueError, TypeError):
                return False

        # Finally, set the variable
        return self._setVariable(variable, newValue)

    def _setVariable(self, variable, newValue):
        """
        Set variable to newValue.
        
        This should not be considered a public method. Use set or setDefault instead.
        No type checking is done.
        
        variable should be either 'value' or 'default'. It defaults to 'value'.
        newValue is the value to set the variable to. It defaults to self.default.

        Returns true if the assignment succeeded. Returns false otherwise.

        Emits modified signal if the assignment succeeded and the new value was 
        different from the old value.
        """

        if variable == 'value':
            if self.value != newValue:
                self.value = newValue
                self.modified.emit()
            else:
                return False
        elif variable == 'default':
            self.default = newValue
        else:
            return False
        
        return True

    def _validateValue(self, variable, newValue):
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

    def _validateValue(self, variable, newValue):
        # bool('False') == True, because 'False' is a non-empty string, so
        # we need to check if newValue is a string, and if so, what its value is.
        if isinstance(newValue, str) and newValue.lower() in ('f', 'false'):
            newValue = False
        
        return newValue

class Dictionary(Property):
    default = {}
    castType = dict

class List(Property):
    default = []
    castType = list

class Color(Property):
    default = QColor()
    castType = QColor

    def getMpl(self):
        return self.get().getRgbF()
    
    def _validateValue(self, variable, newValue):
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


class Options(Property):
    default = Type.Options()
    castType = Type.Options

    def getMpl(self):
        """Create a dict of types, not of properties."""
        mplDict = {}

        for option in self.get().options():
            mplDict[option] = self.get().get(option).getMpl()

        return mplDict

    def _setVariable(self, variable, newValue):
        """
        We need to override the default because the Options type has
        multiple internal values. If we used the default Property._setVariable
        then we would be creating a new Type.Options each time, which results
        in a lot of extra overhead. By doing this, we keep the same Type.Options
        and just replace specific values.

        But, if self.value or self.default is not yet set, then we cannot do this,
        and so we will default back to the normal behavior.
        """
        if variable == 'value':
            returnValue = True
            try:
                returnValue = self.value.setMultiple(newValue)
            except:
                self.value = newValue
            if returnValue != None:
                self.modified.emit()  # if returnValue is not None, then at least one
                                      # entry has been modified.
        elif variable == 'default':
            try:
                self.value.setMultiple(newValue, 'default')
            except:
                self.default = newValue
        else:
            return False

        return True

class TextOptions(Options):
    default = Type.TextFormat()
    castType = Type.TextFormat

class GenericAxis(Options):
    default = Type.GenericAxis()
    castType = Type.GenericAxis

class SymbolString(String):
    default = ""

    symbols = {}

    def getMpl(self):
        """Convert from a word to a character representation of the line style."""
        return self.symbols[self.get()]


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





