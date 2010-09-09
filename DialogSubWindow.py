from PyQt4.QtGui import QMdiSubWindow

class DialogSubWindow(QMdiSubWindow):
    """A simple wrapper class to QMdiSubWindow."""

    def __init__(self, parent=None):
        QMdiSubWindow.__init__(self, parent)
        self.setParent(parent)
        self._parent = parent
    
    def show(self):
        self.setVisible(True)
        self.widget().setVisible(True)
        self.raise_()
        self._parent.setActiveSubWindow(self)
    
    def hide(self):
        self.setVisible(False)


