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
        """
        Return True if the value is set.
        Return False if the value is not set or the value stays the same.
        """

        if variable == 'value':
            try:
                return self._options[option].set(value)
            except (ValueError, TypeError):
                return False
        elif variable == 'default':
            try:
                return self._options[option].setDefault(value)
            except (ValueError, TypeError):
                return False
        else:
            return False

    def setMultiple(self, options, variable='value'):
        """
        Return True if all entries in formatOptions are set successfully.
        Return False if at least one entry in formatOptions is set successfully.
        Return None if no entries are set successfully.
        """
        
        if options == None:
            return True

        if isinstance(options, self.__class__):
            options = options.optionsDict()

        returnValue = None
        allSet = True
        oneSet = False
        for option in options.keys():
            returnValue = self.set(option, options[option], variable)
            allSet &= returnValue
            oneSet |= returnValue
        if allSet:
            return True
        elif oneSet:
            return False
        return None

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
            'label':              Property.String(''),
            'labelFont':          Property.TextOptions({'verticalalignment': 'top'}),
            'visible':            Property.Boolean(True),

            'majorTicksVisible':                    Property.Boolean(True),
            'useMajorTicksSpacing':                 Property.Boolean(False),
            'useMajorTicksNumber':                  Property.Boolean(True),
            'majorTicksSpacing':                    Property.Float(2),
            'majorTicksNumber':                     Property.Integer(5),
            'majorTicksLabelFormat':                Property.String('%.2g'),
            'majorTicksLabelFont':                  Property.TextOptions({'verticalalignment': 'top'}),
            'majorTicksLabelPadding':               Property.Integer(4),
            'majorTicksDirection':                  Property.String('in'),
            'majorTicksColor':                      Property.Color(QColor(0,0,0,255)),
            'majorTicksLength':                     Property.Integer(4),
            'majorTicksWidth':                      Property.Integer(1),
            'majorTicksDisplayPrimary':             Property.Boolean(True),
            'majorTicksDisplaySecondary':           Property.Boolean(True),
            'majorTicksLabelDisplayPrimary':        Property.Boolean(True),
            'majorTicksLabelDisplaySecondary':      Property.Boolean(False),
            
            'minorTicksVisible':                    Property.Boolean(True),
            'minorTicksNumber':                     Property.Integer(5),
            'minorTicksLabelFormat':                Property.String('%.2g'),
            'minorTicksLabelFont':                  Property.TextOptions({'verticalalignment': 'top'}),
            'minorTicksLabelPadding':               Property.Integer(4),
            'minorTicksDirection':                  Property.String('in'),
            'minorTicksColor':                      Property.Color(QColor(0,0,0,255)),
            'minorTicksLength':                     Property.Integer(2),
            'minorTicksWidth':                      Property.Integer(1),
            'minorTicksDisplayPrimary':             Property.Boolean(True),
            'minorTicksDisplaySecondary':           Property.Boolean(True),
            'minorTicksLabelDisplayPrimary':        Property.Boolean(False),
            'minorTicksLabelDisplaySecondary':      Property.Boolean(False),
                 }

        self.setup(defaultOptions, options)


