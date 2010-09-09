from PyQt4.QtCore import Qt, QObject
from PyQt4.QtGui import QWidget, QMenu, QAction, QMessageBox, QPalette, QDialogButtonBox, QColor, QColorDialog, QFileDialog

import ConfigParser, os

import Util
from Trace import Trace
from Module import Module
from Figure import Figure
from DialogSubWindow import DialogSubWindow
from models.FigureListModel import FigureListModel
from models.WavesListModel import WavesListModel
from models.TraceListModel import TraceListModel
from models.PlotListModel import PlotListModel
from TraceListEntry import TraceListEntry
from Gui import QColorButton
from ui.Ui_EditFigureDialog import Ui_EditFigureDialog

class EditFigureDialog(Module):
    """Module to display the Edit Figure dialog window."""

    # Widgets that control the plot
    # The key is the name of the widget
    # the value is a dict with the following parameters
    #   - 'object' = figure, plot, trace
    #       which object this widget applies to
    widgets = { 'plotName':                           { 'object': 'plot'   },
                'plotBackgroundColor':                { 'object': 'plot'   },
                'plotBottomAxisAutoscale':            { 'object': 'plot'   },
                'plotBottomAxisMinimum':              { 'object': 'plot'   },
                'plotBottomAxisMaximum':              { 'object': 'plot'   },
                'plotBottomAxisScaleType':            { 'object': 'plot'   },
                'plotBottomAxisTicks':                { 'object': 'plot'   },
                'plotBottomAxisMajorTicksNumber':     { 'object': 'plot'   },
                'plotBottomAxisMajorTicksSpacing':    { 'object': 'plot'   },
                'plotBottomAxisMinorTicksNumber':     { 'object': 'plot'   },
                'plotBottomAxisUseTickSpacing':       { 'object': 'plot'   },
                'plotBottomAxisUseTickNumber':        { 'object': 'plot'   },
                'plotLeftAxisAutoscale':              { 'object': 'plot'   },
                'plotLeftAxisMinimum':                { 'object': 'plot'   },
                'plotLeftAxisMaximum':                { 'object': 'plot'   },
                'plotTopAxisVisible':                 { 'object': 'plot'   },
                'plotLeftAxisVisible':                { 'object': 'plot'   },
                'plotBottomAxisVisible':              { 'object': 'plot'   },
                'plotRightAxisVisible':               { 'object': 'plot'   },
                'figureName':                         { 'object': 'figure' },
                'figureTitle':                        { 'object': 'figure' },
                'figureRows':                         { 'object': 'figure' },
                'figureColumns':                      { 'object': 'figure' },
                'figureBackgroundColor':              { 'object': 'figure' },
                'traceLineStyle':                     { 'object': 'trace'  },
                'tracePointMarker':                   { 'object': 'trace'  },
                'traceLineColor':                     { 'object': 'trace'  },
                'traceLineWidth':                     { 'object': 'trace'  },
                'tracePointMarkerEdgeColor':          { 'object': 'trace'  },
                'tracePointMarkerFaceColor':          { 'object': 'trace'  },
                'tracePointMarkerEdgeWidth':          { 'object': 'trace'  },
                'tracePointMarkerSize':               { 'object': 'trace'  },
                }


    # To create a new type, update setWidgetValue and getWidgetValue methods in Util.py
    # To create a new widget, update the widgets dict above and also the properties variable in the object that it deals with, and implement code to use that widget
    
    
    def __init__(self, app):
        Module.__init__(self, app)

    def buildWidget(self):
        """Create the widget and populate it."""

        # Create enclosing widget and UI
        self._widget = QWidget()
        self._ui = Ui_EditFigureDialog()
        self._ui.setupUi(self._widget)
        
        # Setup figure list
        self._figureListModel = FigureListModel(self._app.figures())
        self._ui.figureSelector.setModel(self._figureListModel)
        self._app.figures().figureAdded.connect(self._figureListModel.doReset)
        self._app.figures().figureRemoved.connect(self._figureListModel.doReset)

        # Setup plot combo box
        self._plotListModel = PlotListModel()
        self._ui.plotSelector.setModel(self._plotListModel)
        self._ui.plotSelector.currentIndexChanged.connect(self.plotUi_refreshTraceList)
        
        # Setup X and Y lists
        self._xListModel = WavesListModel(self._app.waves())
        self._ui.xAxisListView.setModel(self._xListModel)
        self._app.waves().waveAdded.connect(self._xListModel.doReset)
        self._app.waves().waveRemoved.connect(self._xListModel.doReset)
        
        self._yListModel = WavesListModel(self._app.waves())
        self._ui.yAxisListView.setModel(self._yListModel)
        self._app.waves().waveAdded.connect(self._yListModel.doReset)
        self._app.waves().waveRemoved.connect(self._yListModel.doReset)

        # Setup trace list
        traceListModel = TraceListModel()
        self._ui.traceTableView.setModel(traceListModel)
        self.setupTraceListMenu()

        # Setup max/min values for spin boxes
        self._ui.plotBottomAxisMinimum.setMinimum(-1.7E308)
        self._ui.plotBottomAxisMinimum.setMaximum(1.7E308)
        self._ui.plotBottomAxisMaximum.setMinimum(-1.7E308)
        self._ui.plotBottomAxisMaximum.setMaximum(1.7E308)
        self._ui.plotBottomAxisMajorTicksSpacing.setMaximum(1.7E308)
        self._ui.plotLeftAxisMinimum.setMinimum(-1.7E308)
        self._ui.plotLeftAxisMinimum.setMaximum(1.7E308)
        self._ui.plotLeftAxisMaximum.setMinimum(-1.7E308)
        self._ui.plotLeftAxisMaximum.setMaximum(1.7E308)

        # Setup buttons
        self._ui.figureOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.figureObject_setAttributes)
        self._ui.figureOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.figureUi_resetFields)
        
        self._ui.plotOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.plotObject_setAttributes)
        self._ui.plotOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.plotUi_resetPlotOptions)

        self._ui.traceOptionsButtons.button(QDialogButtonBox.Apply).clicked.connect(self.traceObject_updateAttributes)
        self._ui.traceOptionsButtons.button(QDialogButtonBox.Reset).clicked.connect(self.plotUi_resetTraceOptions)

        self._ui.addTraceButton.clicked.connect(self.addTracesToPlot)

        self._ui.figureSettingsSave.clicked.connect(self.saveFigureSettings)
        self._ui.figureSettingsLoad.clicked.connect(self.loadFigureSettings)

        self._ui.traceSave.clicked.connect(self.saveTrace)
        self._ui.traceLoad.clicked.connect(self.loadTrace)

        self._ui.plotBottomAxisAutoscale.stateChanged.connect(self.plotUi_axisAutoscaleToggled)
        self._ui.plotLeftAxisAutoscale.stateChanged.connect(self.plotUi_axisAutoscaleToggled)
        self._ui.plotTopAxisAutoscale.stateChanged.connect(self.plotUi_axisAutoscaleToggled)
        self._ui.plotRightAxisAutoscale.stateChanged.connect(self.plotUi_axisAutoscaleToggled)

        self._ui.plotBottomAxisUseTickSpacing.clicked.connect(self.plotUi_axisMajorTicksToggled)
        self._ui.plotBottomAxisUseTickNumber.clicked.connect(self.plotUi_axisMajorTicksToggled)


        def createFigure():
            figure = Figure(self._app, "NewFigure")
            self._app.figures().addFigure(figure)

            # Select figure
            self._ui.figureSelector.setCurrentIndex(self._ui.figureSelector.model().rowCount() - 1)

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
                self.figureUi_resetFields()
                self._ui.plotSelector.model().setFigure(figure)
                self._ui.plotSelector.setCurrentIndex(0)
                self.plotUi_setupTab()

        def changePlot(row):
            """Change the content on the plot tab."""

            plot = self.currentPlot()

            if plot:
                self.plotUi_setupTab()

            
        self._ui.addFigureButton.clicked.connect(createFigure)
        self._ui.showFigureButton.clicked.connect(showFigure)
        self._ui.deleteFigureButton.clicked.connect(deleteFigure)
        self._ui.figureSelector.currentIndexChanged.connect(changeFigure)
        self._ui.traceTableView.selectionModel().currentChanged.connect(self.plotUi_resetTraceOptions)
        self._ui.plotSelector.currentIndexChanged.connect(changePlot)
        
        for widgetName in self.widgets.keys():
            if type(vars(self._ui)[widgetName]).__name__ == 'QColorButton':
                vars(self._ui)[widgetName].clicked.connect(vars(self._ui)[widgetName].createColorDialog)

        return self._widget

    #
    # Get current items
    #
    def currentFigure(self):
        return self._ui.figureSelector.model().index(self._ui.figureSelector.currentIndex(), 0).internalPointer()

    def currentPlot(self):
        return self._ui.plotSelector.model().getPlot(self._ui.plotSelector.currentIndex())




    #
    # Generic methods for plot properties that user can edit
    #
    
    def getObjectForWidget(self, widgetName):
        if self.widgets[widgetName]['object'] == 'figure':
            return self.currentFigure()
        elif self.widgets[widgetName]['object'] == 'plot':
            return self.currentPlot()
        elif self.widgets[widgetName]['object'] == 'trace':
            modelRow = self._ui.traceTableView.currentIndex().row()
            if modelRow >= 0:
                traceListEntry = self._ui.traceTableView.model().getTraceListEntryByRow(modelRow)
                if traceListEntry:
                    trace = traceListEntry.getTrace()
                    return trace
            return None

    # Set UI value
    def setUiValue(self, widgetName, value):
        widget = vars(self._ui)[widgetName]
        Util.setWidgetValue(widget, value)

    # Reset UI to object value
    def setUiValueFromObject(self, widgetName):
        theObject = self.getObjectForWidget(widgetName)
        if theObject:
            value = theObject.get(widgetName)
            self.setUiValue(widgetName, value)
            return True
        return False

    # set object value to UI
    def setObjectValueFromUi(self, widgetName, theObject=None):
        value = self.getUiValue(widgetName)

        if not theObject:
            theObject = self.getObjectForWidget(widgetName)

        if theObject:
            return theObject.set_(widgetName, value)
        
        return False


    # get the value from a widget
    def getUiValue(self, widgetName):
        widget = vars(self._ui)[widgetName]
        return Util.getWidgetValue(widget)



    #
    # Figure tab
    #
    def figureObject_setAttributes(self):
        """Set the attributes for the current figure to what the UI says."""

        figure = self.currentFigure()

        updateBool = False
        figure.blockSignals(True)
        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['object'] == 'figure':
                updateBool |= self.setObjectValueFromUi(widgetName)

        figure.blockSignals(False)

        if updateBool:
            figure.refresh()
            
            # Figure name may have changed, so we'll reset the figure combo box
            # But keep the same figure selected
            currentFigureIndex = self._ui.figureSelector.currentIndex()
            currentPlotIndex = self._ui.plotSelector.currentIndex()
            self._ui.figureSelector.model().doReset()
            self._ui.figureSelector.setCurrentIndex(currentFigureIndex)

            # Rows/columns may have changed, so we'll reset the plot combo box
            self._ui.plotSelector.model().setFigure(figure)
            self._ui.plotSelector.model().doReset()
           
            if currentPlotIndex >= (figure.numPlots() - 1):
                print "a"
                self._ui.plotSelector.setCurrentIndex(0)
            else:
                print "b" + str(currentPlotIndex)
                self._ui.plotSelector.setCurrentIndex(currentPlotIndex)

            
        
    def figureUi_resetFields(self):
        """
        Set figure tab to values for the current figure object.
        """
        
        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['object'] == 'figure':
                self.setUiValueFromObject(widgetName)
        
        

    #
    # Plot tab
    #

    def plotUi_setupTab(self):
        """Setup Plot tab."""

        self.plotUi_resetPlotOptions()
        self.plotUi_refreshTraceList()
        self.plotUi_resetTraceOptions()

    def plotObject_setAttributes(self):
        """Update the Plot attributes with everything in the current UI."""

        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['object'] == 'plot':
                self.setObjectValueFromUi(widgetName)

        # Plot names may have changed, so reset the plot combo box.  But it will necessarily
        # have the same number of entries, unlike when changing the figure values
        currentPlotIndex = self._ui.plotSelector.currentIndex()
        self._ui.plotSelector.model().doReset()
        self._ui.plotSelector.setCurrentIndex(currentPlotIndex)

    def plotUi_resetPlotOptions(self):
        """
        Set plot options group to values for the current plot object.
        """
        
        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['object'] == 'plot':
                self.setUiValueFromObject(widgetName)


    def plotUi_resetTraceOptions(self, *args):
        """Update all trace options for the trace that was just clicked."""
        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['object'] == 'trace':
                self.setUiValueFromObject(widgetName)

    def plotUi_axisAutoscaleToggled(self, checkState):
        """
        Toggle enabled/disabled status of min/max fields for plot axes.
        """

        if self._widget.sender() is self._ui.plotBottomAxisAutoscale:
            self._ui.plotBottomAxisMinimum.setEnabled(not self._ui.plotBottomAxisAutoscale.isChecked())
            self._ui.plotBottomAxisMaximum.setEnabled(not self._ui.plotBottomAxisAutoscale.isChecked())
        elif self._widget.sender() is self._ui.plotLeftAxisAutoscale:
            self._ui.plotLeftAxisMinimum.setEnabled(not self._ui.plotLeftAxisAutoscale.isChecked())
            self._ui.plotLeftAxisMaximum.setEnabled(not self._ui.plotLeftAxisAutoscale.isChecked())
        elif self._widget.sender() is self._ui.plotTopAxisAutoscale:
            self._ui.plotTopAxisMinimum.setEnabled(not self._ui.plotTopAxisAutoscale.isChecked())
            self._ui.plotTopAxisMaximum.setEnabled(not self._ui.plotTopAxisAutoscale.isChecked())
        elif self._widget.sender() is self._ui.plotRightAxisAutoscale:
            self._ui.plotRightAxisMinimum.setEnabled(not self._ui.plotRightAxisAutoscale.isChecked())
            self._ui.plotRightAxisMaximum.setEnabled(not self._ui.plotRightAxisAutoscale.isChecked())

    def plotUi_axisMajorTicksToggled(self, checked):
        """
        Toggle enabled/disabled status of major tick options.
        """

        if self._widget.sender() is self._ui.plotBottomAxisUseTickSpacing:
            self._ui.plotBottomAxisMajorTicksSpacing.setEnabled(True)
            self._ui.plotBottomAxisMajorTicksNumber.setEnabled(False)
        elif self._widget.sender() is self._ui.plotBottomAxisUseTickNumber:
            self._ui.plotBottomAxisMajorTicksSpacing.setEnabled(False)
            self._ui.plotBottomAxisMajorTicksNumber.setEnabled(True)



    def traceObject_updateAttributes(self, traces=None):
        updateBool = False

        if not traces:
            traces = set()
            for traceIndex in self._ui.traceTableView.selectedIndexes():
                traces.add(traceIndex.internalPointer().getTrace())
        elif type(traces).__name__ != 'set':
            traces = set([traces])
            
        for trace in traces:
            trace.blockSignals(True)
            
            for widgetName in self.widgets.keys():
                if self.widgets[widgetName]['object'] == 'trace':
                    updateBool |= self.setObjectValueFromUi(widgetName, trace)

            trace.blockSignals(False)

        if updateBool:
            self.currentPlot().refresh()








    def addTracesToPlot(self):
        plot = self.currentPlot()

        xAxisList = self._ui.xAxisListView.selectedIndexes()
        yAxisList = self._ui.yAxisListView.selectedIndexes()

        plot.blockSignals(True)
        for x in xAxisList:
            for y in yAxisList:
                xWave = self._app.waves().waves()[x.row()]
                yWave = self._app.waves().waves()[y.row()]
                trace = Trace(xWave, yWave)
                self.traceObject_updateAttributes(trace)
                plot.addTrace(trace)

        plot.blockSignals(False)
        plot.refresh()
        
        self.plotUi_refreshTraceList()






    def plotUi_refreshTraceList(self):
        """Get all traces in current plot and put them into the plot list model."""
        
        #figure = self.currentFigure()
        plot = self.currentPlot()

        # Clear plot list model
        traceListModel = self._ui.traceTableView.model()
        traceListModel.clearData()
            
        for trace in plot.traces():
            traceListModel.addEntry(TraceListEntry(trace))

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
        trace = traceListEntry.getTrace()

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



    # Saving options to files
    def saveFigureSettings(self):
        fileDialog = QFileDialog(self._app.ui.workspace, "Save Figure Settings")
        fileDialog.setFilter("PySciPlot Figure Settings (*.pspf);;All Files (*.*)")
        fileDialog.setDefaultSuffix("pspf")
        fileDialog.setDirectory(Util.fileDialogDirectory(self._app))
        fileDialog.exec_()
        fileName = str(fileDialog.selectedFiles()[0])

        # Save current working directory
        self._app.cwd = str(fileDialog.directory().absolutePath())

        if fileName != "":
            FigureSettings.writeSettings(fileName, self)

    def loadFigureSettings(self):
        fileDialog = QFileDialog(self._app.ui.workspace, "Load Figure Settings")
        fileDialog.setFilter("PySciPlot Figure Settings (*.pspf);;All Files (*.*)")
        fileDialog.setDirectory(Util.fileDialogDirectory(self._app))
        fileDialog.exec_()
        fileName = str(fileDialog.selectedFiles()[0])
        
        # Save current working directory
        self._app.cwd = str(fileDialog.directory().absolutePath())

        if fileName != "":
            FigureSettings.loadSettings(fileName, self)

    def saveTrace(self):
        fileDialog = QFileDialog(self._app.ui.workspace, "Save Trace")
        fileDialog.setFilter("PySciPlot Trace Settings (*.pspt);;All Files (*.*)")
        fileDialog.setDefaultSuffix("pspt")
        fileDialog.setDirectory(Util.fileDialogDirectory(self._app))
        fileDialog.exec_()
        fileName = str(fileDialog.selectedFiles()[0])

        # Save current working directory
        self._app.cwd = str(fileDialog.directory().absolutePath())

        if fileName != "":
            optionsOnly = Util.getWidgetValue(self._ui.traceSaveOptions)
            TraceSave.writeSettings(fileName, self, optionsOnly)

    def loadTrace(self):
        fileDialog = QFileDialog(self._app.ui.workspace, "Load Trace")
        fileDialog.setFilter("PySciPlot Trace Settings (*.pspt);;All Files (*.*)")
        fileDialog.setDirectory(Util.fileDialogDirectory(self._app))
        fileDialog.exec_()
        fileName = str(fileDialog.selectedFiles()[0])
        
        # Save current working directory
        self._app.cwd = str(fileDialog.directory().absolutePath())

        if fileName != "":
            TraceSave.loadSettings(fileName, self)




    """Module-required methods"""
    def getMenuNameToAddTo(self):
        return "menuPlot"

    def prepareMenuItem(self, menu):
        menu.setObjectName("actionEditFiguresDialog")
        menu.setShortcut("Ctrl+E")
        menu.setText("Edit Figures")
        return menu

    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionEditFiguresDialog")
        self.menuEntry.setShortcut("Ctrl+F")
        self.menuEntry.setText("Edit Figures")
        self.menuEntry.triggered.connect(self.window.show)
        self.menu = vars(self._app.ui)["menuPlot"]
        self.menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):
        # Disconnect some slots
        self._app.figures().figureAdded.disconnect(self._figureListModel.doReset)
        self._app.figures().figureRemoved.disconnect(self._figureListModel.doReset)
        self._ui.plotSelector.currentIndexChanged.disconnect(self.plotUi_refreshTraceList)
        self._app.waves().waveAdded.disconnect(self._xListModel.doReset)
        self._app.waves().waveRemoved.disconnect(self._xListModel.doReset)
        self._app.waves().waveAdded.disconnect(self._yListModel.doReset)
        self._app.waves().waveRemoved.disconnect(self._yListModel.doReset)
        self.menuEntry.triggered.disconnect()

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)





class FigureSettings():
    """
    Save/Load figure settings to/from a file.
    """

    @staticmethod
    def collectSettings(config, figureDialog):
        """
        Pull all of the settings into a ConfigParser class, but do not
        write them out yet.  This allows us to collect a whole bunch of 
        settings and just write them out once.
        """

        for widgetName in figureDialog.widgets.keys():
            if figureDialog.widgets[widgetName]['object'] == 'figure':
                config.set('Figure', str(widgetName), str(figureDialog.getUiValue(widgetName)))
        return config

    @staticmethod
    def writeSettings(fileName, figureDialog):
        """
        Write all the figure settings to a file.
        """

        # Verify that the file is actually a file or does not exist
        if os.path.isfile(fileName) or not os.path.exists(fileName):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.add_section('Application')
            config.set('Application', 'pysciplot_version', '1')
            config.add_section('Figure')
            
            config = FigureSettings.collectSettings(config, figureDialog)
    
            with open(fileName, 'wb') as configFile:
                config.write(configFile)

    
    @staticmethod
    def loadSettings(fileName, figureDialog):
        """
        Load the figure settings from a file.
        """

        if os.path.isfile(fileName):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.read(fileName)
            version = config.get('Application', 'pysciplot_version')

            for widgetName in figureDialog.widgets.keys():
                if figureDialog.widgets[widgetName]['object'] == 'figure':
                    figureDialog.setUiValue(widgetName, config.get('Figure', str(widgetName)))


class TraceSave():
    """
    Save/Load trace settings to/from a file.
    """

    @staticmethod
    def collectSettings(config, figureDialog):
        """
        Pull all of the settings into a ConfigParser class, but do not
        write them out yet.  This allows us to collect a whole bunch of 
        settings and just write them out once.
        """

        for widgetName in figureDialog.widgets.keys():
            if figureDialog.widgets[widgetName]['object'] == 'trace':
                config.set('Trace', str(widgetName), str(figureDialog.getUiValue(widgetName)))
        return config

    @staticmethod
    def writeSettings(fileName, figureDialog, optionsOnly):
        """
        Write all the trace settings to a file.

        The optionsOnly argument indicates whether to save only the options, or the options
        and the data.
        """

        # Verify that the file is actually a file or does not exist
        if os.path.isfile(fileName) or not os.path.exists(fileName):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.add_section('Application')
            config.set('Application', 'pysciplot_version', '1')
            config.add_section('Trace')
            
            config = TraceSave.collectSettings(config, figureDialog)
    
            with open(fileName, 'wb') as configFile:
                config.write(configFile)

    
    @staticmethod
    def loadSettings(fileName, figureDialog):
        """
        Load the trace settings from a file.
        """

        if os.path.isfile(fileName):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.read(fileName)
            version = config.get('Application', 'pysciplot_version')

            for widgetName in figureDialog.widgets.keys():
                if figureDialog.widgets[widgetName]['object'] == 'trace':
                    figureDialog.setUiValue(widgetName, config.get('Trace', str(widgetName)))






