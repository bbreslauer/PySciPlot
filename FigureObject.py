import Util

class FigureObject(object):
    """
    A part of the figure.
    """

    def __init__(self, properties={}):
        self.properties = properties

        # Connect signals
        for prop in self.properties.keys():
            try:
                self.properties[prop].modified.connect(getattr(self, "update_" + prop))
            except:
                self.properties[prop].modified.connect(self.refresh)
        
    def get(self, variable):
        try:
            Util.debug(3, "FigureObject.get", "Getting variable " + str(variable) + "=" + str(self.properties[variable].get()))
            return self.properties[variable].get()
        except KeyError:
            return None

    def getMpl(self, variable):
        try:
            Util.debug(3, "FigureObject.getMpl", "Getting mpl variable " + str(variable) + "=" + str(self.properties[variable].get()))
            return self.properties[variable].getMpl()
        except KeyError:
            return None

    def set_(self, variable, value):
        print "FigureObject.set_ is deprecated. Please use FigureObject.set instead." + str(variable) + "   " + str(value)
        return self.set(variable, value)
    
    def set(self, variable, value):
        Util.debug(2, "FigureObject.set", "Setting " + str(variable) + " to " + str(value))

        try:
            return self.properties[variable].set(value)
        except KeyError:
            return None

    def setMultiple(self, properties):

        for (key, value) in properties.items():
            self.set(key, value)

        return True


