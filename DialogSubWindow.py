from PyQt4.QtGui import QMdiSubWindow

class DialogSubWindow(QMdiSubWindow):
    """A simple wrapper class to QMdiSubWindow."""

    def __init__(self, parent=0):
        QMdiSubWindow.__init__(self, parent)
        self.setParent(parent)
    
    def show(self):
        self.setVisible(True)
        self.widget().setVisible(True)
    
    def hide(self):
        self.setVisible(False)


