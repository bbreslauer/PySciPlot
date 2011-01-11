from PyQt4.QtGui import QWidget, QApplication

from QEditFigureSubWidget import *

class QScatterPlotAxisWidget(QEditFigureSubWidget):

    def __init__(self, *args):
        QEditFigureSubWidget.__init__(self, *args)

    def getOptions(self, optionNames):
        options = {}
        
        for option in optionNames:
            options[option] = Util.getWidgetValue(self.getChild(option))

        return options

    def setOptions(self, options):
        for option in options.options():
            Util.setWidgetValue(self.getChild(option), options.get(option).get())


