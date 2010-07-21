from PyQt4.QtCore import Qt
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
from ui.Ui_EditFigureDialog import Ui_EditFigureDialog

class EditFigureDialog(Module):
    """Module to display the Edit Figure dialog window."""

    # Widgets that control the plot
    # The key is the name of the widget
    # the value is a dict with the following parameters
    #   - 'object' = figure, plot, trace
    #       which object this widget applies to
    #   - 'type' = 'lineedit', 'spinbox', 'doublespinbox', 'color', 'dropdown', 'checkbox'
    #       the type of object that this is
    widgets = { 'plotName':                     { 'object': 'plot',     'type': 'lineedit' },
                'plotBackgroundColor':          { 'object': 'plot',     'type': 'color' },
                'plotXAxisAutoscale':           { 'object': 'plot',     'type': 'checkbox' },
                'plotXAxisMinimum':             { 'object': 'plot',     'type': 'doublespinbox' },
                'plotXAxisMaximum':             { 'object': 'plot',     'type': 'doublespinbox' },
                'plotYAxisAutoscale':           { 'object': 'plot',     'type': 'checkbox' },
                'plotYAxisMinimum':             { 'object': 'plot',     'type': 'doublespinbox' },
                'plotYAxisMaximum':             { 'object': 'plot',     'type': 'doublespinbox' },
                'plotTopAxisVisible':           { 'object': 'plot',     'type': 'checkbox' },
                'plotLeftAxisVisible':          { 'object': 'plot',     'type': 'checkbox' },
                'plotBottomAxisVisible':        { 'object': 'plot',     'type': 'checkbox' },
                'plotRightAxisVisible':         { 'object': 'plot',     'type': 'checkbox' },
                'figureName':                   { 'object': 'figure',   'type': 'lineedit' },
                'figureTitle':                  { 'object': 'figure',   'type': 'lineedit' },
                'figureRows':                   { 'object': 'figure',   'type': 'spinbox' },
                'figureColumns':                { 'object': 'figure',   'type': 'spinbox' },
                'figureBackgroundColor':        { 'object': 'figure',   'type': 'color' },
                'traceLineStyle':               { 'object': 'trace',    'type': 'dropdown' },
                'tracePointMarker':             { 'object': 'trace',    'type': 'dropdown' },
                'traceLineColor':               { 'object': 'trace',    'type': 'color' },
                'traceLineWidth':               { 'object': 'trace',    'type': 'doublespinbox' },
                'tracePointMarkerEdgeColor':    { 'object': 'trace',    'type': 'color' },
                'tracePointMarkerFaceColor':    { 'object': 'trace',    'type': 'color' },
                'tracePointMarkerEdgeWidth':    { 'object': 'trace',    'type': 'doublespinbox' },
                'tracePointMarkerSize':         { 'object': 'trace',    'type': 'doublespinbox' },

              }


    # To create a new type, update setUiValue and setObjectValueFromUi methods
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
        self._ui.plotXAxisMinimum.setMinimum(-1.7E308)
        self._ui.plotXAxisMinimum.setMaximum(1.7E308)
        self._ui.plotXAxisMaximum.setMinimum(-1.7E308)
        self._ui.plotXAxisMaximum.setMaximum(1.7E308)
        self._ui.plotYAxisMinimum.setMinimum(-1.7E308)
        self._ui.plotYAxisMinimum.setMaximum(1.7E308)
        self._ui.plotYAxisMaximum.setMinimum(-1.7E308)
        self._ui.plotYAxisMaximum.setMaximum(1.7E308)

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
        
        self.registerColorCallbackFunctions()
        self.registerColorHelperFunctions()
        
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

    # Create an anonymous function that creates a callback function
    # This must be done in a separate method so that widgetName does not take the last entry in the for loop in the method below
    def makeColorCallbackFunction(self, widgetName):
        return lambda color: self.setUiValue(widgetName, color.name())


    # Register and create helper function (for color buttons)
    def registerColorCallbackFunctions(self):
        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['type'] == 'color':
                vars(self)[widgetName + 'Callback'] = self.makeColorCallbackFunction(widgetName)

    # Create an anonymous function that creates a color dialog box
    # This must be done in a separate method so that widgetName does not take the last entry in the for loop in the method below
    def makeColorHelperFunction(self, widgetName):
        return lambda: self.createColorDialog(QColor(str(vars(self._ui)[widgetName].text())), vars(self)[widgetName + 'Callback'])

    def registerColorHelperFunctions(self):
        for widgetName in self.widgets.keys():
            if self.widgets[widgetName]['type'] == 'color':
                vars(self)[widgetName + 'Helper'] = self.makeColorHelperFunction(widgetName)
                vars(self._ui)[widgetName].clicked.connect(vars(self)[widgetName + 'Helper'])
               

    # Set UI value
    def setUiValue(self, widgetName, value):
        widget = vars(self._ui)[widgetName]
        widgetType = self.widgets[widgetName]['type']

#        if widgetType == 'lineedit':
#            widget.setText(value)
#        elif widgetType == 'doublespinbox':
#            widget.setValue(value)
#        elif widgetType == 'spinbox':
#            widget.setValue(value)
#        elif widgetType == 'color':
#            widget.setStyleSheet("background-color: " + value + "; color: " + self.goodTextColor(value))
#            widget.setText(value)
#        elif widgetType == 'dropdown':
#            widget.setCurrentIndex(widget.findText(value))
#        elif widgetType == 'checkbox':
#            state = Qt.Unchecked
#            if value:
#                state = Qt.Checked
#            widget.setCheckState(state)


        if widgetType == 'lineedit':
            widget.setText(str(value))
        elif widgetType == 'doublespinbox':
            widget.setValue(float(value))
        elif widgetType == 'spinbox':
            widget.setValue(int(value))
        elif widgetType == 'color':
            widget.setStyleSheet("background-color: " + str(value) + "; color: " + self.goodTextColor(str(value)))
            widget.setText(str(value))
        elif widgetType == 'dropdown':
            widget.setCurrentIndex(widget.findText(str(value)))
        elif widgetType == 'checkbox':
            state = Qt.Unchecked
            if value:
                state = Qt.Checked
            widget.setCheckState(state)



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
#        value = ""
#
#        widget = vars(self._ui)[widgetName]
#        widgetType = self.widgets[widgetName]['type']
#        
#        if widgetType == 'lineedit':
#            value = widget.text()
#        elif widgetType == 'doublespinbox':
#            value = widget.value()
#        elif widgetType == 'spinbox':
#            value = widget.value()
#        elif widgetType == 'color':
#            value = widget.text()
#        elif widgetType == 'dropdown':
#            value = str(widget.currentText())
#        elif widgetType == 'checkbox':
#            value = widget.isChecked()
        
        value = self.getUiWidgetValue(widgetName)

        if not theObject:
            theObject = self.getObjectForWidget(widgetName)

        if theObject:
            return theObject.set_(widgetName, value)
        
        return False


    # get the value from a widget
    def getUiWidgetValue(self, widgetName):
        widget = vars(self._ui)[widgetName]
        widgetType = self.widgets[widgetName]['type']
        
        value = ""
        if widgetType == 'lineedit':
            value = widget.text()
        elif widgetType == 'doublespinbox':
            value = widget.value()
        elif widgetType == 'spinbox':
            value = widget.value()
        elif widgetType == 'color':
            value = widget.text()
        elif widgetType == 'dropdown':
            value = str(widget.currentText())
        elif widgetType == 'checkbox':
            value = widget.isChecked()

        return value
        




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
            FigureSettings.saveSettings(fileName, self)

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


    # Random stuff for now
    def createColorDialog(self, currentColor, callBack):
        newColor = QColorDialog.getColor(currentColor)
        if newColor.isValid():
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

    def load(self):
        self.window = DialogSubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionEditFiguresDialog")
        self.menuEntry.setShortcut("Ctrl+E")
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
    def saveSettings(fileName, figureDialog):
        # Verify that the file is actually a file or does not exist
        if os.path.isfile(fileName) or not os.path.exists(fileName):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.add_section('Figure')
            config.set('Figure', 'pysciplot_version', '1')
    
            for widgetName in figureDialog.widgets.keys():
                if figureDialog.widgets[widgetName]['object'] == 'figure':
                    config.set('Figure', str(widgetName), str(figureDialog.getUiWidgetValue(widgetName)))
    
            with open(fileName, 'wb') as configFile:
                config.write(configFile)

    
    @staticmethod
    def loadSettings(fileName, figureDialog):
        if os.path.isfile(fileName):
            config = ConfigParser.SafeConfigParser()
            config.optionxform = str
            config.read(fileName)
            version = config.get('Figure', 'pysciplot_version')

            for widgetName in figureDialog.widgets.keys():
                if figureDialog.widgets[widgetName]['object'] == 'figure':
                    figureDialog.setUiValue(widgetName, config.get('Figure', str(widgetName)))





