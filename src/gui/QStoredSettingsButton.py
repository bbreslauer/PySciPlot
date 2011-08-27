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


from PySide.QtGui import QToolButton, QApplication
from PySide.QtCore import Qt

from gui.SubWindows import SubWindow
from gui.QStoredSettingsWidget import *
from ui.Ui_StoredSettingsWidget import *


class QStoredSettingsButton(QToolButton):


    def __init__(self, *args):
        QToolButton.__init__(self, *args)

        self.storedSettingsWidget = QStoredSettingsWidget(self.parent(), self)
        self.storedSettingsWidget.setParent(self.parent())
        storedSettingsWidgetUi = Ui_StoredSettingsWidget()
        storedSettingsWidgetUi.setupUi(self.storedSettingsWidget)
        self.storedSettingsWidget.initSubWidgets()

        self.storedSettingsWidget.move(self.x() - self.storedSettingsWidget.width(), self.y())

        self.toggleWidget(False)

    def toggleWidget(self, visible=None):
        if visible is None:
            visible = not self.storedSettingsWidget.isVisible()

        self.storedSettingsWidget.setVisible(visible)
        if visible:
            self.setArrowType(Qt.RightArrow)
        else:
            self.setArrowType(Qt.LeftArrow)






