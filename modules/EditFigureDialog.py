from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QMenu, QAction

from Trace import Trace
from Module import Module
from Figure import Figure
from FigureListModel import FigureListModel
from WavesListModel import WavesListModel
from PlotListModel import PlotListModel
from PlotListEntry import PlotListEntry
from ui.Ui_EditFigureDialog import Ui_EditFigureDialog

class EditFigureDialog(Module):
    """Module to display the Edit Figure dialog window."""

    def __init__(self, app):
        self._widget = QWidget()
        self._app = app
        self._currentFigure = None
        self.buildWidget()

    def buildWidget(self):
        """Create the widget and populate it."""

        # If no figures have been created yet, create the first one.
        # This way, everything works from the start and you don't have
        # to add a figure in order to start.

        # Create enclosing widget and UI
        self._ui = Ui_EditFigureDialog()
        self._ui.setupUi(self._widget)
        
        # QT Designer puts a widget around the layout object.  This gets around it
        # so that the entire window resizes correctly.
        self._widget.setLayout(self._ui.horizontalLayout)

        # Setup figure list
        figureListModel = FigureListModel(self._app.figures())
        self._ui.figureListView.setModel(figureListModel)
        self._app.figures().figureAdded.connect(figureListModel.doReset)
        self._app.figures().figureRemoved.connect(figureListModel.doReset)

        # Setup X and Y lists
        xListModel = WavesListModel(self._app.waves())
        self._ui.xAxisListView.setModel(xListModel)
        self._app.waves().waveAdded.connect(xListModel.doReset)
        self._app.waves().waveRemoved.connect(xListModel.doReset)
        
        yListModel = WavesListModel(self._app.waves())
        self._ui.yAxisListView.setModel(yListModel)
        self._app.waves().waveAdded.connect(yListModel.doReset)
        self._app.waves().waveRemoved.connect(yListModel.doReset)

        # Setup plot list
        plotListModel = PlotListModel()
        self._ui.plotListView.setModel(plotListModel)
        self.setupPlotListMenu()
        

        def createFigure():
            self._app.figures().addFigure(Figure(self._app, "NewFigure"))

        def showFigure():
            """Display the figure, in case it got hidden."""

            index = self._ui.figureListView.selectedIndexes()[0]
            self._app.figures().getFigure(index.row()).showFigure()

        def deleteFigure():
            """
            Delete button has been pressed.  Make sure the user really wants
            to delete the figure.
            """
            
            index = self._ui.figureListView.selectedIndexes()[0]
            
            # Ask user if they really want to delete the figure
            questionMessage = QMessageBox()
            questionMessage.setIcon(QMessageBox.Question)
            questionMessage.setText("You are about to delete a figure.")
            questionMessage.setInformativeText("Are you sure this is what you want to do?")
            questionMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            questionMessage.setDefaultButton(QMessageBox.No)
            answer = questionMessage.exec_()

            if answer == QMessageBox.Yes:
                self._app.figures().removeFigure(index.row())

        def changeFigure(index):
            """Change the tabs to use data from the selected figure."""

            figure = self._app.figures().getFigure(index.row())
            
            self.setCurrentFigure(figure)
            self.setupFigureListLabel()
            self.resetSignalsOnFigureChange()
            self.setupFigureTab()
            self.setupPlotTab()
            
        self._ui.addFigureButton.clicked.connect(createFigure)
        self._ui.showFigureButton.clicked.connect(showFigure)
        self._ui.deleteFigureButton.clicked.connect(deleteFigure)
        self._ui.figureListView.selectionModel().currentChanged.connect(changeFigure)
        
        return self._widget

    def setupFigureListLabel(self):
        self._ui.figureListLabel.setText("Currently working on figure:\n" + self._currentFigure.name())

    def setCurrentFigure(self, figure):
        self._currentFigure = figure

    def resetSignalsOnFigureChange(self):
        """Disconnect and reconnect all signals whenever the active figure is changed."""
        # Disconnect signals, only if they exist.  A TypeError exception is raised 
        # whenever the signal does not exist.  We must handle these so that execution
        # continues, and we must use a separate try for each signal so that we make 
        # sure to disconnect every signal (since if an exception is raised, nothing 
        # in the try statement after that exception is executed).

        figure = self._currentFigure

        # Signal disconnections
        for f in self._app.figures().figures():
            try:
                f.figureRenamed.disconnect(self.setupFigureListLabel)
            except TypeError:
                pass

        try:
            self._ui.figureRows.valueChanged.disconnect()
        except TypeError:
            pass
        try:
            self._ui.figureColumns.valueChanged.disconnect()
        except TypeError:
            pass
        try:
            self._ui.addTraceButton.clicked.disconnect()
        except TypeError:
            pass
#        try:
#        except TypeError:
#            pass

        # Helper functions

        # setMaximum is not a C++ slot, so a helper function is needed
        def setPlotNumMaximum(value):
            self._ui.plotNum.setMaximum(figure.rows() * figure.columns())
        
        # Add a trace to a plot on a figure
        def addTracesToPlot():
            plotNum = self._ui.plotNum.value()
            plot = figure.getPlot(plotNum)

            xAxisList = self._ui.xAxisListView.selectedIndexes()
            yAxisList = self._ui.yAxisListView.selectedIndexes()
            traceColor = str(self._ui.traceColor.currentText())

            for x in xAxisList:
                for y in yAxisList:
                    xWave = self._app.waves().waves()[x.row()]
                    yWave = self._app.waves().waves()[y.row()]
                    trace = Trace(xWave, yWave, traceColor)
                    plot.addTrace(trace)
            
            self.refreshPlotList()

        def refreshPlotListHelper(value):
            self.refreshPlotList()

        # Signal connections
        figure.figureRenamed.connect(self.setupFigureListLabel)

        self._ui.figureRows.valueChanged.connect(figure.setNumberOfRows)
        self._ui.figureRows.valueChanged.connect(setPlotNumMaximum)
        self._ui.figureRows.valueChanged.connect(refreshPlotListHelper)
        
        self._ui.figureColumns.valueChanged.connect(figure.setNumberOfColumns)
        self._ui.figureColumns.valueChanged.connect(setPlotNumMaximum)
        self._ui.figureColumns.valueChanged.connect(refreshPlotListHelper)

        self._ui.addTraceButton.clicked.connect(addTracesToPlot)

    def setupFigureTab(self):
        # Set row and column numbers.  Block some signals
        # because the number of rows or columns isn't really changing,
        # it's only changing in the UI because we're switching plots.
        figure = self._currentFigure

        self._ui.figureRows.blockSignals(True)
        self._ui.figureColumns.blockSignals(True)

        self._ui.figureRows.setValue(figure.rows())
        self._ui.figureColumns.setValue(figure.columns())

        # Unblock signals
        self._ui.figureRows.blockSignals(False)
        self._ui.figureColumns.blockSignals(False)


    def setupPlotTab(self):
        # Setup Plot tab
        figure = self._currentFigure

        self._ui.plotNum.setMaximum(figure.rows() * figure.columns())
        self._ui.plotNum.setValue(1)
        self.refreshPlotList()

    def refreshPlotList(self):
        """Get all traces in all visible plots and put them into the plot list model."""
        
        figure = self._currentFigure

        # Clear plot list model
        plotListModel = self._ui.plotListView.model()
        plotListModel.clearData()

        # Loop through plots and add all traces to model
        for plotNum in range(1, figure.numPlots() + 1):
            plot = figure.getPlot(plotNum)
            for trace in plot.getTraces():
                plotListModel.addEntry(PlotListEntry(plotNum, trace))

        plotListModel.doReset()
        
        return True

    def setupPlotListMenu(self):
        """Prepare the menu for right clicking on a plot list entry."""

        # Setup plot list right-click menu
        self._ui.plotListView.setContextMenuPolicy(Qt.CustomContextMenu)
        self._ui.plotListView.customContextMenuRequested.connect(self.showPlotListMenu)
        
        self.plotListMenu = QMenu(self._ui.plotListView)

        self.deleteTraceFromPlotListAction = QAction("Delete Trace", self.plotListMenu)
        self.plotListMenu.addAction(self.deleteTraceFromPlotListAction)

    def deleteTraceFromPlot(self, row):
        plotListEntry = self._ui.plotListView.model().getPlotListEntryByRow(row)
        plotNum = plotListEntry.getPlotNum()
        trace   = plotListEntry.getTrace()

        plot = self._currentFigure.getPlot(plotNum)
        plot.removeTrace(trace)

        self.refreshPlotList()


    def showPlotListMenu(self, point):
        """Display the menu that occurs when right clicking on a plot list entry."""

        index = self._ui.plotListView.indexAt(point)
        
        if index.row() < 0:
            return False

        def deleteTraceHelper():
            self.deleteTraceFromPlot(index.row())

        # Connect actions
        self.deleteTraceFromPlotListAction.triggered.connect(deleteTraceHelper)

        self.plotListMenu.exec_(self._ui.plotListView.mapToGlobal(point))
        
        # Disconnect actions, so that we don't have multiple connections when
        # the menu is opened again.
        self.deleteTraceFromPlotListAction.triggered.disconnect(deleteTraceHelper)



    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu






