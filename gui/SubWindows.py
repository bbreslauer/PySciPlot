#from DialogSubWindow import DialogSubWindow

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

