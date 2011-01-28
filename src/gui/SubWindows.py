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


from PyQt4.QtGui import QMdiSubWindow
from PyQt4.QtCore import Qt

class SubWindow(QMdiSubWindow):
    """
    A simple wrapper class to QMdiSubWindow.
    """

    def __init__(self, parent=None, flags=Qt.SubWindow):
        QMdiSubWindow.__init__(self, parent, flags)

    def setWidget(self, widget):
        QMdiSubWindow.setWidget(self, widget)
        self.resize(widget.size())
    
    def show(self):
        QMdiSubWindow.show(self)
        self.widget().setVisible(True)


class DataTableSubWindow(SubWindow):
    pass

class FigureSubWindow(SubWindow):
    pass

