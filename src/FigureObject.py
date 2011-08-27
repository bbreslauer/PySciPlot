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


from PySide.QtCore import QObject, Signal
from PySide.QtGui import QApplication

import Util

class FigureObject(QObject):
    """
    A part of the figure.
    """

    def __init__(self, properties={}):
        QObject.__init__(self)
        
        self._app = QApplication.instance().window

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
            Util.debug(3, "FigureObject.getMpl", "Getting mpl variable " + str(variable) + "=" + str(self.properties[variable].getMpl()))
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


