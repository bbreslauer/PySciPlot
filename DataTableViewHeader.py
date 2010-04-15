from PyQt4.QtGui import QHeaderView
from PyQt4.QtCore import Qt, SIGNAL

class DataTableViewHeader(QHeaderView):
    def __init__(self, orientation, parent=0):
        QHeaderView.__init__(self, orientation, parent)
        self.setParent(parent)
        self.setMovable(True)
        self.setHighlightSections(True)
        #self.connect(self,  SIGNAL("sectionMoved(int, int, int)"),  self.asdf)
        print "dtvh"
        #self.moveSection(1, 2)
    
    def isMovable(self):
        return False
    
    def moveSection(self, fromIndex, toIndex):
        print "moveSection"
        self.emit(SIGNAL("sectionMoved(int, int, int)"),  0,  fromIndex,  toIndex)
        #self.parent().model().moveWave(fromIndex, toIndex)a
    
    def asdf(self, a, b, c):
        print "asdf"
#        self.moveSection(c,  b)
        self.resetColumnOrder()
