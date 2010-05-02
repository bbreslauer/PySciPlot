from PyQt4.QtGui import QWidget

from Module import Module
from Figure import Figure
from FigureListModel import FigureListModel
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
        if self._app.figures().length() == 0:
            self._app.figures().addFigure(Figure("NewFigure"))

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
        

        def createFigure():
            self._app.figures().addFigure(Figure("NewFigure"))

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
            
            # Setup signals
            try:
                self._ui.figureRows.valueChanged.disconnect()
                self._ui.figureColumns.valueChanged.disconnect()
            except TypeError:
                pass
            self._ui.figureRows.valueChanged.connect(figure.changeNumberOfRows)
            self._ui.figureColumns.valueChanged.connect(figure.changeNumberOfColumns)

            # Set row and column numbers.  This needs to be after setting up the related
            # signals because if we change the value with the old signals connected, 
            # the old figure will have its values set to the new figure's values.
            self._ui.figureRows.setValue(figure.rows())
            self._ui.figureColumns.setValue(figure.columns())

            # Setup Plot tab

            # Setup signals
            self._ui.figureRows.valueChanged.connect(self._ui.plotRow.setMaximum)
            self._ui.figureColumns.valueChanged.connect(self._ui.plotColumn.setMaximum)
            
            self._ui.plotRow.setMaximum(figure.rows())
            self._ui.plotColumn.setMaximum(figure.columns())

        self._ui.addFigureButton.clicked.connect(createFigure)
        self._ui.deleteFigureButton.clicked.connect(deleteFigure)
        self._ui.figureListView.clicked.connect(changeFigure)
        
        return self._widget

    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu






