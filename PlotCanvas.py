from PyQt4.QtGui import QGraphicsScene, QGraphicsView, QWidget
from PyQt4.QtCore import Qt, QRectF

class PlotCanvas(QGraphicsView):
    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent)
        
    
    
