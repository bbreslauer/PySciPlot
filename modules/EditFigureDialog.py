from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QMenu, QAction, QMessageBox, QPalette, QDialogButtonBox, QColor, QColorDialog

from Trace import Trace
from Module import Module
from Figure import Figure
from models.FigureListModel import FigureListModel
from models.WavesListModel import WavesListModel
from models.TraceListModel import TraceListModel
from models.PlotListModel import PlotListModel
from TraceListEntry import TraceListEntry
from ui.Ui_EditFigureDialog import Ui_EditFigureDialog

class EditFigureDialog(Module):
    """Module to display the Edit Figure dialog window."""

    def __init__(self, app):
        self._widget = QWidget()
        self._app = app
        self.buildWidget()

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._ui = Ui_EditFigureDialog()
        self._ui.setupUi(self._widget)
        
        # Setup figure list
        figureListModel = FigureListModel(self._app.figures())
        self._ui.figureListView.setModel(figureListModel)
        self._app.figures().figureAdded.connect(figureListModel.doReset)
        self._app.figures().figureRemoved.connect(figureListModel.doReset)

        # Setup plot combo box
        plotListModel = PlotListModel()
        self._ui.plotComboBox.setModel(plotListModel)
        self._ui.plotComboBox.currentIndexChanged.connect(self.plotUi_refreshTraceList)

        # Setup X and Y lists
        xListModel = WavesListModel(self._app.waves())
        self._ui.xAxisListView.setModel(xListModel)
        self._app.waves().waveAdded.connect(xListModel.doReset)
        self._app.waves().waveRemoved.connect(xListModel.doReset)
        
        yListModel = WavesListModel(self._app.waves())
        self._ui.yAxisListView.setModel(yListModel)
        self._app.waves().waveAdded.connect(yListModel.doReset)
        self._app.waves().waveRemoved.connect(yListModel.doReset)

        # Setup trace list
        traceListModel = TraceListModel()
        self._ui.traceTableView.setModel(traceListModel)
        self.setupTraceListMenu()

        # Setup buttons
        self._ui.figureOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.figureObject_setAttributes)
        self._ui.figureOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.figureUi_resetFields)
        
        self._ui.plotOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.plotObject_setAttributes)
        self._ui.plotOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.plotUi_resetPlotOptions)

        self._ui.traceOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.traceObject_updateAttributes)
        self._ui.traceOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.plotUi_resetTraceOptions)

        self._ui.addTraceButton.clicked.connect(self.addTracesToPlot)


        def createFigure():
            self._app.figures().addFigure(Figure(self._app, "NewFigure"))

        def showFigure():
            """Display the figure, in case it got hidden."""
            
            if self.currentFigure():
                self.currentFigure().showFigure()

        def deleteFigure():
            """
            Delete button has been pressed.  Make sure the user really wants
            to delete the figure.
            """
            
            figure = self.currentFigure()
            
            # Make sure we are on a valid figure
            if not figure:
                return False
            
            # Ask user if they really want to delete the figure
            questionMessage = QMessageBox()
            questionMessage.setIcon(QMessageBox.Question)
            questionMessage.setText("You are about to delete a figure.")
            questionMessage.setInformativeText("Are you sure this is what you want to do?")
            questionMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            questionMessage.setDefaultButton(QMessageBox.No)
            answer = questionMessage.exec_()

            if answer == QMessageBox.Yes:
                figure.hideFigure()
                self._app.figures().removeFigure(figure)

        def changeFigure(index):
            """Change the tabs to use data from the selected figure."""

            figure = self.currentFigure()

            if figure:
                self._ui.figureListLabel.setText("Currently working on figure:\n" + figure.name())
                self.figureUi_resetFields()
                self._ui.plotComboBox.model().setFigure(figure)
                self._ui.plotComboBox.setCurrentIndex(0)
                self.plotUi_setupTab()

        def changePlot(row):
            """Change the content on the plot tab."""

            plot = self.currentPlot()

            if plot:
                self.plotUi_setupTab()

        def figureBackgroundColorHelper():
            """Open a color dialog box to select a color."""
            self.createColorDialog(QColor(str(self._ui.figureBackgroundColorButton.text())), self.figureBackgroundColorCallback)

        def traceLineColorHelper():
            """Open a color dialog box to select a color."""
            self.createColorDialog(QColor(str(self._ui.traceLineColorButton.text())), self.traceLineColorCallback)

        def plotBackgroundColorHelper():
            """Open a color dialog box to select a color."""
            self.createColorDialog(QColor(str(self._ui.plotBackgroundColorButton.text())), self.plotBackgroundColorCallback)

        def pointMarkerFaceColorHelper():
            self.createColorDialog(QColor(str(self._ui.pointMarkerFaceColorButton.text())), self.pointMarkerFaceColorCallback)

        def pointMarkerEdgeColorHelper():
            self.createColorDialog(QColor(str(self._ui.pointMarkerEdgeColorButton.text())), self.pointMarkerEdgeColorCallback)

            
        self._ui.addFigureButton.clicked.connect(createFigure)
        self._ui.showFigureButton.clicked.connect(showFigure)
        self._ui.deleteFigureButton.clicked.connect(deleteFigure)
        self._ui.figureListView.selectionModel().currentChanged.connect(changeFigure)
        self._ui.traceTableView.selectionModel().currentChanged.connect(self.plotUi_resetTraceOptions)
        self._ui.plotComboBox.currentIndexChanged.connect(changePlot)
        self._ui.figureBackgroundColorButton.clicked.connect(figureBackgroundColorHelper)
        self._ui.traceLineColorButton.clicked.connect(traceLineColorHelper)
        self._ui.plotBackgroundColorButton.clicked.connect(plotBackgroundColorHelper)
        self._ui.pointMarkerFaceColorButton.clicked.connect(pointMarkerFaceColorHelper)
        self._ui.pointMarkerEdgeColorButton.clicked.connect(pointMarkerEdgeColorHelper)
        
        return self._widget

    #
    # Get current items
    #
    def currentFigure(self):
        return self._ui.figureListView.selectionModel().currentIndex().internalPointer()

    def currentPlot(self):
        return self._ui.plotComboBox.model().getPlot(self._ui.plotComboBox.currentIndex())


    #
    # Figure tab
    #
    def figureObject_setAttributes(self):
        """Set the attributes for the current figure to what the UI says."""

        figure = self.currentFigure()
        
        figure.setNumberOfRows(self._ui.figureRows.value())
        figure.setNumberOfColumns(self._ui.figureColumns.value())
        figure.setBackgroundColor(QColor(self._ui.figureBackgroundColorButton.text()))
        
        #self.refreshTraceList()
        #self._ui.plotComboBox.model().doReset()
        #self._ui.plotComboBox.setCurrentIndex(0)

    def figureUi_resetFields(self):
        """
        Set figure tab to values for the current figure object.
        """
        figure = self.currentFigure()
        
        
        self.figureUi_setRows(figure.rows())
        self.figureUi_setColumns(figure.columns())
        self.figureUi_setBackgroundColor(figure.backgroundColor().name())
    
    def figureUi_setRows(self, rows):
        self._ui.figureRows.setValue(rows)

    def figureUi_setColumns(self, columns):
        self._ui.figureColumns.setValue(columns)

    def figureUi_setBackgroundColor(self, colorName):
        self._ui.figureBackgroundColorButton.setStyleSheet("background-color: " + colorName + "; color: " + self.goodTextColor(colorName))
        self._ui.figureBackgroundColorButton.setText(colorName)

    def figureBackgroundColorCallback(self, newColor):
        if newColor.isValid():
            self.figureUi_setBackgroundColor(newColor.name())




    #
    # Plot tab
    #

    def plotUi_setPlotName(self, name):
        self._ui.plotName.setText(name)

    def plotUi_setBackgroundColor(self, colorName):
        self._ui.plotBackgroundColorButton.setStyleSheet("background-color: " + colorName + "; color: " + self.goodTextColor(colorName))
        self._ui.plotBackgroundColorButton.setText(colorName)
    
    def plotUi_setTraceLineColor(self, colorName):
        self._ui.traceLineColorButton.setStyleSheet("background-color: " + colorName + "; color: " + self.goodTextColor(colorName))
        self._ui.traceLineColorButton.setText(colorName)

    def plotUi_setPointMarkerFaceColor(self, colorName):
        self._ui.pointMarkerFaceColorButton.setStyleSheet("background-color: " + colorName + "; color: " + self.goodTextColor(colorName))
        self._ui.pointMarkerFaceColorButton.setText(colorName)

    def plotUi_setPointMarkerEdgeColor(self, colorName):
        self._ui.pointMarkerEdgeColorButton.setStyleSheet("background-color: " + colorName + "; color: " + self.goodTextColor(colorName))
        self._ui.pointMarkerEdgeColorButton.setText(colorName)



    def plotUi_setLinestyle(self, linestyle):
        self._ui.lineStyle.setCurrentIndex(self._ui.lineStyle.findText(linestyle))

    def plotUi_setPointMarker(self, pointMarker):
        self._ui.pointMarker.setCurrentIndex(self._ui.pointMarker.findText(pointMarker))

    def plotBackgroundColorCallback(self, newColor):
        if newColor.isValid():
            self.plotUi_setBackgroundColor(newColor.name())

    def traceLineColorCallback(self, newColor):
        if newColor.isValid():
            self.plotUi_setTraceLineColor(newColor.name())

    def pointMarkerFaceColorCallback(self, newColor):
        if newColor.isValid():
            self.plotUi_setPointMarkerFaceColor(newColor.name())

    def pointMarkerEdgeColorCallback(self, newColor):
        if newColor.isValid():
            self.plotUi_setPointMarkerEdgeColor(newColor.name())

    def addTracesToPlot(self):
        plot = self.currentPlot()

        xAxisList = self._ui.xAxisListView.selectedIndexes()
        yAxisList = self._ui.yAxisListView.selectedIndexes()
        traceColor = str(self._ui.traceLineColorButton.text())
        lineStyle = str(self._ui.lineStyle.currentText())
        pointMarker = str(self._ui.pointMarker.currentText())
        pointMarkerFaceColor = str(self._ui.pointMarkerFaceColorButton.text())
        pointMarkerEdgeColor = str(self._ui.pointMarkerEdgeColorButton.text())

        plot.blockSignals(True)
        for x in xAxisList:
            for y in yAxisList:
                xWave = self._app.waves().waves()[x.row()]
                yWave = self._app.waves().waves()[y.row()]
                trace = Trace(xWave, yWave, traceColor=traceColor,
                                            lineStyle=lineStyle,
                                            pointMarker=pointMarker,
                                            pointMarkerFaceColor=pointMarkerFaceColor,
                                            pointMarkerEdgeColor=pointMarkerEdgeColor
                             )
                plot.addTrace(trace)

        plot.blockSignals(False)
        plot.refresh()
        
        self.plotUi_refreshTraceList()


    def plotObject_setAttributes(self):
        """Update the Plot attributes with everything in the current UI."""

        plot = self.currentPlot()

        plot.setName(self._ui.plotName.text())
        plot.setBackgroundColor(QColor(self._ui.plotBackgroundColorButton.text()))

    def plotUi_setupTab(self):
        """Setup Plot tab."""

        self.plotUi_resetPlotOptions()
        self.plotUi_refreshTraceList()
        self.plotUi_resetTraceOptions()


    def plotUi_resetPlotOptions(self):
        """
        Set plot options group to values for the current plot object.
        """

        plot = self.currentPlot()
        
        self.plotUi_setPlotName(plot.getName())
        self.plotUi_setBackgroundColor(plot.backgroundColor().name())

    def plotUi_resetTraceOptions(self, index=None):
        """Update all trace options for the trace that was just clicked, as identified by index."""
        
        if not index:
            return

        trace = self._ui.traceTableView.model().getTraceListEntryByRow(index.row()).getTrace()

        # Setup color drop-down box
        self.plotUi_setTraceLineColor(trace.getLineColor())
        self.plotUi_setLinestyle(trace.getLinestyle())
        self.plotUi_setPointMarker(trace.getPointMarker())
        self.plotUi_setPointMarkerFaceColor(trace.getPointMarkerFaceColor())
        self.plotUi_setPointMarkerEdgeColor(trace.getPointMarkerEdgeColor())

    def traceObject_updateAttributes(self):
        updateBool = False
        for traceIndex in self._ui.traceTableView.selectedIndexes():
            trace = traceIndex.internalPointer().getTrace()
            
            trace.blockSignals(True)
            updateBool |= trace.setLineColor(str(self._ui.traceLineColorButton.text()))
            updateBool |= trace.setLinestyle(str(self._ui.lineStyle.currentText()))
            updateBool |= trace.setPointMarker(str(self._ui.pointMarker.currentText()))
            updateBool |= trace.setPointMarkerFaceColor(str(self._ui.pointMarkerFaceColorButton.text()))
            updateBool |= trace.setPointMarkerEdgeColor(str(self._ui.pointMarkerEdgeColorButton.text()))
            trace.blockSignals(False)

        if updateBool:
            self.currentPlot().refresh()





    def plotUi_refreshTraceList(self):
        """Get all traces in current plot and put them into the plot list model."""
        
        #figure = self.currentFigure()
        plot = self.currentPlot()

        # Clear plot list model
        traceListModel = self._ui.traceTableView.model()
        traceListModel.clearData()
            
        for trace in plot.getTraces():
            traceListModel.addEntry(TraceListEntry(trace))

        ## Loop through plots and add all traces to model
        #for plotNum in range(1, figure.numPlots() + 1):
        #    plot = figure.getPlot(plotNum)
        #    for trace in plot.getTraces():
        #        traceListModel.addEntry(TraceListEntry(trace))

        traceListModel.doReset()

        self._ui.traceTableView.selectRow(traceListModel.rowCount() - 1)
        
        return True



    def setupTraceListMenu(self):
        """Prepare the menu for right clicking on a plot list entry."""

        # Setup plot list right-click menu
        self._ui.traceTableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self._ui.traceTableView.customContextMenuRequested.connect(self.showTraceListMenu)
        
        self.traceListMenu = QMenu(self._ui.traceTableView)

        self.deleteTraceFromTraceListAction = QAction("Delete Trace", self.traceListMenu)
        self.traceListMenu.addAction(self.deleteTraceFromTraceListAction)

    def deleteTraceFromPlot(self, row):
        traceListEntry = self._ui.traceTableView.model().getTraceListEntryByRow(row)
        trace   = traceListEntry.getTrace()

        self.currentPlot().removeTrace(trace)

        self.plotUi_refreshTraceList()

    def showTraceListMenu(self, point):
        """Display the menu that occurs when right clicking on a plot list entry."""

        index = self._ui.traceTableView.indexAt(point)
        
        if index.row() < 0:
            self._ui.traceTableView.setCurrentIndex(self._ui.traceTableView.model().index(-1,0))
            return False

        def deleteTraceHelper():
            self.deleteTraceFromPlot(index.row())

        # Connect actions
        self.deleteTraceFromTraceListAction.triggered.connect(deleteTraceHelper)

        self.traceListMenu.exec_(self._ui.traceTableView.mapToGlobal(point))
        
        # Disconnect actions, so that we don't have multiple connections when
        # the menu is opened again.
        self.deleteTraceFromTraceListAction.triggered.disconnect(deleteTraceHelper)




    # Random stuff for now
    def createColorDialog(self, currentColor, callBack):
        newColor = QColorDialog.getColor(currentColor)
        callBack(newColor)

    def goodTextColor(self, backgroundColor):
        """Determines whether complementary color should be white or black."""
        lightness = QColor(backgroundColor).lightnessF()
        if lightness > 0.4:
            return "#000000"
        return "#ffffff"




    """Module-required methods"""
    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu






