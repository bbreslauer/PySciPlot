from PyQt4.QtGui import QWidget

class DataTableViewWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(400, 300)
