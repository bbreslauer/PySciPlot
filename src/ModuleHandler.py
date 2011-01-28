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


from gui.SubWindows import SubWindow

class ModuleHandler():
    """
    Handle all modules, including importing them into the main program.
    """

    def __init__(self):
        pass

    def addWidgetToWindow(self, widget, subWindow):
        """
        Encapsulate a widget in a SubWindow (basically a QMdiSubWindow) and
        then add it to the QMdiArea.
        """

        subWindow.setWidget(widget)
        widget.setParent(subWindow)
        return subWindow


    def addWidgetToMenu(self, menuName, moduleMenu, window, action):
        """
        Add moduleMenu to the window's menu with the object name menuName.
        """
        menu = getattr(window, menuName)
        menu.addAction(moduleMenu)
        moduleMenu.triggered.connect(action)




