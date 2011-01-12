from PyQt4.QtGui import QWidget, QMenu, QAction, QApplication

from Trace import *
from TraceListEntry import *
from models.WavesListModel import *
from models.TraceListModel import *
from QEditFigureSubWidget import *

class QScatterPlotTracesWidget(QEditFigureSubWidget):

    def __init__(self, plotOptionsWidget, *args):
        QEditFigureSubWidget.__init__(self, *args)

        self._plotOptionsWidget = plotOptionsWidget

    def initSubWidgets(self):
        self.getChild('lineColor').initButtonColor()
        self.getChild('pointMarkerFaceColor').initButtonColor()
        self.getChild('pointMarkerEdgeColor').initButtonColor()

        # Setup X and Y lists
        self._xListModel = WavesListModel(self._app.waves())
        self.getChild('xAxisListView').setModel(self._xListModel)
        self._app.waves().waveAdded.connect(self._xListModel.doReset)
        self._app.waves().waveRemoved[Wave].connect(self._xListModel.doReset)
        
        self._yListModel = WavesListModel(self._app.waves())
        self.getChild('yAxisListView').setModel(self._yListModel)
        self._app.waves().waveAdded.connect(self._yListModel.doReset)
        self._app.waves().waveRemoved[Wave].connect(self._yListModel.doReset)
        
        # Setup trace list
        traceListModel = TraceListModel()
        self.getChild('traceTableView').setModel(traceListModel)
        self._app.waves().waveRemoved[Wave].connect(self.deleteTracesWithWave)
        self.setupTraceListMenu()

        self.getChild('traceTableView').selectionModel().currentChanged.connect(self.selectedTraceChanged)

    def setupTraceListMenu(self):
        
        self.traceListMenu = QMenu(self.getChild('traceTableView'))

        self.deleteTraceFromTraceListAction = QAction("Delete Trace", self.traceListMenu)
        self.traceListMenu.addAction(self.deleteTraceFromTraceListAction)

    def addTracesToPlot(self):
        # This is the scatter plot, which holds the traces.  the plot object does not hold the traces
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject

        xAxisList = self.getChild('xAxisListView').selectedIndexes()
        yAxisList = self.getChild('yAxisListView').selectedIndexes()

        for x in xAxisList:
            for y in yAxisList:
                xWave = self._app.waves().waves()[x.row()]
                yWave = self._app.waves().waves()[y.row()]
                trace = Trace(xWave, yWave)
                self.saveOptionsToTrace(trace)
                plotTypeObject.addTrace(trace)

        self.refreshTraceList()

    def refreshTraceList(self):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject

        # Clear plot list model
        traceListModel = self.getChild('traceTableView').model()
        traceListModel.clearData()
            
        for trace in plotTypeObject.traces():
            traceListModel.addEntry(TraceListEntry(trace))

        traceListModel.doReset()

        self.getChild('traceTableView').selectRow(traceListModel.rowCount() - 1)
        
    def showTraceListMenu(self, point):
        """Display the menu that occurs when right clicking on a plot list entry."""

        index = self.getChild('traceTableView').indexAt(point)
        
        if index.row() < 0:
            return False
        
        def deleteTraceHelper():
            self.deleteTraceFromPlot(index.internalPointer().getTrace())

        # Connect actions
        self.deleteTraceFromTraceListAction.triggered.connect(deleteTraceHelper)

        self.traceListMenu.exec_(self.getChild('traceTableView').mapToGlobal(point))
        
        # Disconnect actions, so that we don't have multiple connections when
        # the menu is opened again.
        self.deleteTraceFromTraceListAction.triggered.disconnect(deleteTraceHelper)

    def deleteTracesWithWave(self, wave):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject

        for trace in plotTypeObject.traces():
            if wave.name() in [trace.xName(), trace.yName()]:
                self.deleteTraceFromPlot(trace)

    def deleteTraceFromPlot(self, trace):
        plotTypeObject = self._plotOptionsWidget.currentPlot().plotTypeObject
        plotTypeObject.removeTrace(trace)
        self.refreshTraceList()

    def saveOptionsToTrace(self, trace):
        for option in trace.properties.keys():
            trace.set(option, Util.getWidgetValue(self.getChild(option)))

    def saveOptionsToSelectedTraces(self):
        print "saving traces"
        indexes = self.getChild('traceTableView').selectedIndexes()
        
        traces = set()  # We use a set because each row has two selected indexes, and 
                        # we want to don't want to double-count rows
        for index in indexes:
            traces.add(index.internalPointer().getTrace())

        for trace in traces:
            self.saveOptionsToTrace(trace)

    def setUiToTrace(self, trace):
        for option in trace.properties.keys():
            Util.setWidgetValue(self.getChild(option), trace.get(option))

    def selectedTraceChanged(self, newIndex, oldIndex):
        self.setUiToTrace(newIndex.internalPointer().getTrace())

    def saveUi(self):
        self.saveOptionsToSelectedTraces()

    def resetUi(self):

        self.refreshTraceList()


