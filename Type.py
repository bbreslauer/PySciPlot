from PyQt4.QtGui import QColor

import Property

class Options(object):

    def __init__(self, options={}):
        self.setup({}, options)
        
    def setup(self, defaultOptions, options={}):
        # Define all the options that are allowed in this object.
        # Anything not defined here will not be allowed later on.
        self._options = defaultOptions

        # Now set the options to the user specified values
        # and make them the defaults for the properties.
        self.setMultiple(options, 'default')
        self.setMultiple(options, 'value')

    def __reduce__(self):
        """Method for pickling."""
        return tuple([self.__class__, tuple([self.options()])])

    def set(self, option, value, variable='value'):
        if variable == 'value':
            try:
                self._options[option].set(value)
            except (ValueError, TypeError):
                return False
            return True 
        elif variable == 'default':
            try:
                self._options[option].setDefault(value)
            except (ValueError, TypeError):
                return False
            return True 
        else:
            return False

    def setMultiple(self, options, variable='value'):
        """
        Return True if all entries in formatOptions are set successfully.
        Return False if at least one entry in formatOptions fails to be set.
        """
        
        if options == None:
            return True

        if isinstance(options, self.__class__):
            options = options.optionsDict()

        returnValue = True
        for option in options.keys():
            returnValue &= self.set(option, options[option], variable)
        return returnValue

    def get(self, option):
        """Return the value of an options."""
        try:
            return self._options[option]
        except KeyError:
            return None

    def options(self):
        """Return the names of the options (the keys of the options dictionary)."""
        return self._options.keys()

    def optionsDict(self):
        """Return the dictionary of options."""
        return self._options

class TextFormat(Options):

    def __init__(self, options={}):
        defaultOptions = { 
            'name':                  Property.String('Bitstream Vera Sans'),
            'style':                 Property.String('normal'),
            'variant':               Property.String('normal'),
            'stretch':               Property.Integer(100),
            'weight':                Property.Integer(100),
            'size':                  Property.Integer(12),
            'color':                 Property.Color(QColor(0,0,0,255)),
            'backgroundcolor':       Property.Color(QColor(255,255,255,0)),
            'alpha':                 Property.Float(1.0),
            'horizontalalignment':   Property.String('center'),
            'verticalalignment':     Property.String('center'),
            'linespacing':           Property.Float(1.2),
            'rotation':              Property.String('horizontal'),
           }

        self.setup(defaultOptions, options)


class GenericAxis(Options):

    def __init__(self, options={}):
        defaultOptions = {
            'autoscale':          Property.Boolean(True),
            'minimum':            Property.Float(-10),
            'maximum':            Property.Float(10),
            'scaleType':          Property.String('Linear'),
            'ticks':              Property.Boolean(True),
            'label':              Property.String(''),
            'visible':            Property.Boolean(True),
            'majorTicksNumber':   Property.Integer(5),
            'majorTicksSpacing':  Property.Float(2),
            'minorTicksNumber':   Property.Integer(3),
            'useTickSpacing':     Property.Boolean(False),
            'useTickNumber':      Property.Boolean(True),
            'tickLabelFormat':    Property.String('%.2g'),
            'tickLabelFont':      Property.TextOptions({'verticalalignment': 'top'}),
            'labelFont':          Property.TextOptions({'verticalalignment': 'top'}),
                }

        self.setup(defaultOptions, options)


