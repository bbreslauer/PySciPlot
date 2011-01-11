from PyQt4.QtGui import QWidget, QApplication

from QEditFigureSubWidget import *
from QScatterPlotAxisWidget import *
from QScatterPlotTracesWidget import *
from ui.Ui_ScatterPlotAxis import *
from ui.Ui_ScatterPlotTraces import *

class QScatterPlotTypeWidget(QEditFigureSubWidget):

    def __init__(self, plotOptionsWidget, *args):
        QEditFigureSubWidget.__init__(self, *args)

        self._plotOptionsWidget = plotOptionsWidget

    def initSubWidgets(self):
        # Add the various tabs to this widget
        self.bottomAxis = QScatterPlotAxisWidget(self.getChild('tabWidget'))
        bottomAxisUi = Ui_ScatterPlotAxis()
        bottomAxisUi.setupUi(self.bottomAxis)
        self.getChild('tabWidget').addTab(self.bottomAxis, 'Bottom Axis')

        self.leftAxis = QScatterPlotAxisWidget(self.getChild('tabWidget'))
        leftAxisUi = Ui_ScatterPlotAxis()
        leftAxisUi.setupUi(self.leftAxis)
        self.getChild('tabWidget').addTab(self.leftAxis, 'Left Axis')

        self.traces = QScatterPlotTracesWidget(self._plotOptionsWidget, self.getChild('tabWidget'))
        tracesUi = Ui_ScatterPlotTraces()
        tracesUi.setupUi(self.traces)
        self.traces.initSubWidgets()
        self.getChild('tabWidget').addTab(self.traces, 'Traces')

    def saveUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        self.traces.saveOptionsToSelectedTraces()
        
        bottomAxisUiOptions = self.bottomAxis.getOptions(plotTypeObject.get('bottomAxis').options())
        plotTypeObject.set('bottomAxis', bottomAxisUiOptions)

        leftAxisUiOptions = self.leftAxis.getOptions(plotTypeObject.get('leftAxis').options())
        plotTypeObject.set('leftAxis', leftAxisUiOptions)


    def resetUi(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        
        bottomAxisOptions = plotTypeObject.get('bottomAxis')
        self.bottomAxis.setOptions(bottomAxisOptions)

        leftAxisOptions = plotTypeObject.get('leftAxis')
        self.leftAxis.setOptions(leftAxisOptions)

        self.traces.resetUi()

