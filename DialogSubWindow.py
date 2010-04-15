from PyQt4.QtGui import QMdiSubWindow

class DialogSubWindow(QMdiSubWindow):
    def __init__(self, parent=0):
        QMdiSubWindow.__init__(self, parent)
        self.mainWindow = parent
    
    def show(self):
        self.setVisible(True)
        self.widget().setVisible(True)
    
    
