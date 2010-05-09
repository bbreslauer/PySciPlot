from PyQt4.QtGui import QWidget

from Module import Module
from Figure import Figure
from FigureListModel import FigureListModel
from WavesListModel import WavesListModel
from ui.Ui_EditFigureDialog2 import Ui_EditFigureDialog

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
            self.setupFigureTab(figure)
            self.setupPlotTab(figure)
            
            # If the current figure is renamed, make sure the label is updated to reflect that.
            # But remove all other connections from the label.  The only way the figure can
            # be updated is if it is the current figure, but that could change in the future.
            for figure in self._app.figures().figures():
                try:
                    figure.figureRenamed.disconnect(self.setupFigureListLabel)
                except:
                    pass

            self._app.figures().getFigure(self._ui.figureListView.selectionModel().currentIndex().row()).figureRenamed.connect(self.setupFigureListLabel)

        self._ui.addFigureButton.clicked.connect(createFigure)
        self._ui.showFigureButton.clicked.connect(showFigure)
        self._ui.deleteFigureButton.clicked.connect(deleteFigure)
        self._ui.figureListView.selectionModel().currentChanged.connect(changeFigure)
        
        return self._widget

    def setupFigureListLabel(self, figureName):
        self._ui.figureListLabel.setText("Currently working on:\n" + figureName)


    def setupFigureTab(self, figure):
        # Setup signals
        try:
            self._ui.figureRows.valueChanged.disconnect()
            self._ui.figureColumns.valueChanged.disconnect()
        except TypeError:
            pass
        self._ui.figureRows.valueChanged.connect(figure.setNumberOfRows)
        self._ui.figureColumns.valueChanged.connect(figure.setNumberOfColumns)

        # Set row and column numbers.  This needs to be after setting up the related
        # signals because if we change the value with the old signals connected,
        # the old figure will have its values set to the new figure's values.
        self._ui.figureRows.setValue(figure.rows())
        self._ui.figureColumns.setValue(figure.columns())


    def setupPlotTab(self, figure):
        # Setup Plot tab

        # setMaximum is not a C++ slot, so a helper function is needed
        def setPlotRowMaximum(value):
            self._ui.plotRow.setMaximum(value)
        def setPlotColumnMaximum(value):
            self._ui.plotColumn.setMaximum(value)

        # Setup signals
        self._ui.figureRows.valueChanged.connect(setPlotRowMaximum)
        self._ui.figureColumns.valueChanged.connect(setPlotColumnMaximum)
        
        self._ui.plotRow.setMaximum(figure.rows())
        self._ui.plotColumn.setMaximum(figure.columns())

        self._ui.plotRow.setValue(1)
        self._ui.plotColumn.setValue(1)

        # Add a trace to a plot on a figure
        def addTracesToPlot():
            row = self._ui.plotRow.value()
            col = self._ui.plotColumn.value()
            plot = figure.getPlot(row, col)

            xAxisList = self._ui.xAxisListView.selectedIndexes()
            yAxisList = self._ui.yAxisListView.selectedIndexes()

            for x in xAxisList:
                for y in yAxisList:
                    plot.addTrace(self._app.waves().waves()[x.row()], self._app.waves().waves()[y.row()])
            
        self._ui.addPlotButton.clicked.connect(addTracesToPlot)




    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu






