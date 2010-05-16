from PyQt4.QtGui import QWidget

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
        self.buildWidget()

    def buildWidget(self):
        """Create the widget and populate it."""

        # If no figures have been created yet, create the first one.
        # This way, everything works from the start and you don't have
        # to add a figure in order to start.
#        if self._app.figures().length() == 0:
#            self._app.figures().addFigure(Figure("NewFigure"))

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
            
            self.setupFigureListLabel(figure.name())
            self.resetSignalsOnFigureChange(figure)
            self.setupFigureTab(figure)
            self.setupPlotTab(figure)
            
#            # If the current figure is renamed, make sure the label is updated to reflect that.
#            # But remove all other connections from the label.  The only way the figure can
#            # be updated is if it is the current figure, but that could change in the future.
#            for figure in self._app.figures().figures():
#                try:
#                    figure.figureRenamed.disconnect(self.setupFigureListLabel)
#                except:
#                    pass
#
#            self._app.figures().getFigure(self._ui.figureListView.selectionModel().currentIndex().row()).figureRenamed.connect(self.setupFigureListLabel)

        self._ui.addFigureButton.clicked.connect(createFigure)
        self._ui.showFigureButton.clicked.connect(showFigure)
        self._ui.deleteFigureButton.clicked.connect(deleteFigure)
        self._ui.figureListView.selectionModel().currentChanged.connect(changeFigure)
        
        return self._widget

    def setupFigureListLabel(self, figureName):
        self._ui.figureListLabel.setText("Currently working on figure:\n" + figureName)

    def resetSignalsOnFigureChange(self, figure):
        """Disconnect and reconnect all signals whenever the active figure is changed."""
        # Disconnect signals, only if they exist.  A TypeError exception is raised 
        # whenever the signal does not exist.  We must handle these so that execution
        # continues, and we must use a separate try for each signal so that we make 
        # sure to disconnect every signal (since if an exception is raised, nothing 
        # in the try statement after that exception is executed).

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
            self._ui.addPlotButton.clicked.disconnect()
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

            for x in xAxisList:
                for y in yAxisList:
                    xWave = self._app.waves().waves()[x.row()]
                    yWave = self._app.waves().waves()[y.row()]
                    plot.addTrace(xWave, yWave)
            
            self.refreshPlotList(figure)

        def refreshPlotListHelper(value):
            self.refreshPlotList(figure)

        # Signal connections
        figure.figureRenamed.connect(self.setupFigureListLabel)

        self._ui.figureRows.valueChanged.connect(figure.setNumberOfRows)
        self._ui.figureRows.valueChanged.connect(setPlotNumMaximum)
        self._ui.figureRows.valueChanged.connect(refreshPlotListHelper)
        
        self._ui.figureColumns.valueChanged.connect(figure.setNumberOfColumns)
        self._ui.figureColumns.valueChanged.connect(setPlotNumMaximum)
        self._ui.figureColumns.valueChanged.connect(refreshPlotListHelper)

        self._ui.addPlotButton.clicked.connect(addTracesToPlot)

    def setupFigureTab(self, figure):
        # Set row and column numbers.  Block some signals
        # because the number of rows or columns isn't really changing,
        # it's only changing in the UI because we're switching plots.
        self._ui.figureRows.blockSignals(True)
        self._ui.figureColumns.blockSignals(True)

        self._ui.figureRows.setValue(figure.rows())
        self._ui.figureColumns.setValue(figure.columns())

        # Unblock signals
        self._ui.figureRows.blockSignals(False)
        self._ui.figureColumns.blockSignals(False)


    def setupPlotTab(self, figure):
        # Setup Plot tab
        self._ui.plotNum.setMaximum(figure.rows() * figure.columns())
        self._ui.plotNum.setValue(1)
        self.refreshPlotList(figure)

    def refreshPlotList(self, figure):
        """Get all traces in all visible plots and put them into the plot list model."""
        
        # Clear plot list model
        plotListModel = self._ui.plotListView.model()
        plotListModel.clearData()

        # Loop through plots and add all traces to model
        for plotNum in range(1, figure.numPlots() + 1):
            plot = figure.getPlot(plotNum)
            for trace in plot.getTraces():
                plotListModel.addEntry(PlotListEntry(plotNum, trace.getXName(), trace.getYName()))

        plotListModel.doReset()
        
        return True

    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu






