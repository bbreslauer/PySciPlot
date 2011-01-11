from PyQt4.QtGui import QWidget, QApplication, QDialogButtonBox

from QEditFigureSubWidget import *
from QScatterPlotTypeWidget import *
from models.PlotListModel import *
from ui.Ui_PlotTypeWidget import *

class QPlotOptionsWidget(QEditFigureSubWidget):

    def __init__(self, *args):
        QEditFigureSubWidget.__init__(self, *args)
        self._currentPlot = None
    
    def currentPlot(self):
        return self._currentPlot

    def initPlotSelector(self):
        self._plotListModel = PlotListModel()
        plotSelector = self.getChild('plotSelector')
        plotSelector.setModel(self._plotListModel)

    def initSubWidgets(self):
        # Add all the plot widgets to the stack
        self.scatterPlotWidget = QScatterPlotTypeWidget(self, self.getChild('plotTypeStack'))
        scatterPlotWidgetUi = Ui_PlotTypeWidget()
        scatterPlotWidgetUi.setupUi(self.scatterPlotWidget)
        self.scatterPlotWidget.initSubWidgets()
        self.getChild('plotTypeStack').addWidget(self.scatterPlotWidget)
        self.getChild('plotType').addItem('Scatter Plot')

        self.piePlotWidget = QEditFigureSubWidget(self.getChild('plotTypeStack'))
        piePlotWidgetUi = Ui_PlotTypeWidget()
        piePlotWidgetUi.setupUi(self.piePlotWidget)
        self.getChild('plotTypeStack').addWidget(self.piePlotWidget)
        self.getChild('plotType').addItem('Pie Chart')

    def changeCurrentPlot(self, index):
        if index < 0:
            return

        self._currentPlot = self._plotListModel.getPlot(index)
        self.getChild('plotSelector').setCurrentIndex(index)
        self.resetUi()
        self.getChild('plotTypeStack').currentWidget().resetUi() # Reset the plot type widget's ui

    def setFigure(self, figure, index=0):
        """
        Set the figure whose plots should be displayed.
        """
        self._plotListModel.setFigure(figure)
        self._plotListModel.doReset()

        if index >= figure.numPlots():
            index = 0
        
        self.changeCurrentPlot(index)
    
    def refreshPlotSelector(self):
        """
        Refresh the plot selector.  Intended to be used if the number of
        plots on a figure changes, so that we can make sure that the combo box
        is still valid.
        """
        self.setFigure(self._editFigureDialogModule.currentFigure(), self.getChild('plotSelector').currentIndex())

    def saveUi(self):
        """Save the UI data to the current Plot object."""
        
        currentPlot = self.currentPlot()
        for option in currentPlot.properties.keys():
            currentPlot.set(option, Util.getWidgetValue(self.getChild(option)))

    def resetUi(self):
        """
        Set the UI to the current Plot's settings.
        
        Any unknown widget types will be discarded.
        """
        
        currentPlot = self.currentPlot()
        for option in currentPlot.properties.keys():
            try:
                Util.setWidgetValue(self.getChild(option), currentPlot.get(option))
            except UnknownWidgetTypeError:
                pass

        # Change the plot type widget that is shown based on the type of plot
        # that is currently selected (scatter, pie, etc)
        self.getChild('plotTypeStack').setCurrentIndex(self.getChild('plotType').currentRow())


    def applyClicked(self):
        self.saveUi()
        self.refreshPlotSelector()

