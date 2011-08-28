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


from PySide.QtCore import QModelIndex, Qt
from PySide.QtGui import QStringListModel, QApplication

from Property import *

class StoredSettingsModel(QStringListModel):
    """
    A model for a list of properties.

    Each entry in the self._properties list is a list, with values
    [name, Property-dict]
    name is a string which will be displayed
    Property-dict is a dictionary with (property-name: Property) pairs
    """

    def __init__(self, widgetName, parent=None, *args):
        QStringListModel.__init__(self, parent, *args)
        self._app = QApplication.instance().window
        self._widgetName = widgetName

    def storedSettings(self):
        return self._app.storedSettings()

    def rowCount(self, parent=QModelIndex()):
        try:
            return len(self.storedSettings()[self._widgetName])
        except KeyError:
            return 0

    def index(self, row, column, parent=QModelIndex()):
        if row > self.rowCount():
            return self.createIndex(row, column, parent)
        try:
            return self.createIndex(row, column, self.storedSettings()[self._widgetName][row])
        except KeyError:
            return self.createIndex(row, column, parent)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return index.internalPointer()[0]
        return None

    def setData(self, index, value, role):
        name = str(value).strip()
        if index.isValid() and role == Qt.EditRole and name != "":
            try:
                index.internalPointer()[0] = name
                self.dataChanged.emit(index, index)
                return True
            except:
                return False
        return False

    def doReset(self, *args):
        self.reset()






