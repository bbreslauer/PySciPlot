import Util
from PyQt4.QtGui import QMdiSubWindow
from PyQt4.QtCore import Qt

class DialogSubWindow(QMdiSubWindow):
    """A simple wrapper class to QMdiSubWindow."""

    def __init__(self, parent=None):
        QMdiSubWindow.__init__(self, parent)
        self.setParent(parent)
        self._parent = parent

    def setWidget(self, widget):
        QMdiSubWindow.setWidget(self, widget)
        self.resize(widget.size())
    
    def show(self):
        self.setVisible(True)
        self.widget().setVisible(True)
        self.raise_()
        self._parent.setActiveSubWindow(self)
        Util.debug(3, "DialogSubWindow.show", "Showing " + str(type(self).__name__) + " window")
    
    def hide(self):
        self.setVisible(False)
        Util.debug(3, "DialogSubWindow.hide", "Hiding " + str(type(self).__name__) + " window")


