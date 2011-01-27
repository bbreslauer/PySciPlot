from PyQt4.QtGui import QToolButton, QApplication
from PyQt4.QtCore import Qt

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






