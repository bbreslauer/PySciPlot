# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from PyQt4.QtGui import QWidget, QAction, QTableWidgetItem
from PyQt4.QtCore import Qt

import Util, math, numpy, scipy.optimize
from numpy import e
from Wave import Wave
from Module import Module
from gui.SubWindows import SubWindow
from ui.Ui_CurveFitting import Ui_CurveFitting

class CurveFitting(Module):
    """Module to fit waves to a function."""

    # To add new fitting functions, do the following:
    # 1) Edit GUI
    # 2) modify loadParameterTable, where it creates defaults
    # 3) Create a fit[Function] method to do the fitting
    # 4) Call fit[Function] from doFit

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        self._widget = QWidget()
        self._ui = Ui_CurveFitting()
        self._ui.setupUi(self._widget)

        self.setModels()
        self.setupSpinBoxes()
        self.setupParameterTableData()

        # Connect button signals
        self._ui.doFitButton.clicked.connect(self.doFit)
        self._ui.closeButton.clicked.connect(self.closeWindow)
        self._ui.function.currentIndexChanged[str].connect(self.saveAndLoadParameterTable)
        self._ui.function.currentIndexChanged[str].connect(self.connectSlotsOnFunctionChange)
        
        self.connectSlotsOnFunctionChange('')

    def setModels(self):
        # Set up model and view
        self._allWavesListModel = self._app.model('appWaves')
        self._ui.xWave.setModel(self._allWavesListModel)
        self._ui.yWave.setModel(self._allWavesListModel)
        self._ui.interpolationDomain.setModel(self._allWavesListModel)

    def setupSpinBoxes(self):
        self._ui.dataRangeStart.addWaveView(self._ui.xWave)
        self._ui.dataRangeEnd.addWaveView(self._ui.xWave)

        self._ui.dataRangeStart.addWaveView(self._ui.yWave)
        self._ui.dataRangeEnd.addWaveView(self._ui.yWave)

        self._ui.interpolationRangeStart.addWaveView(self._ui.interpolationDomain)
        self._ui.interpolationRangeEnd.addWaveView(self._ui.interpolationDomain)

    def setupParameterTableData(self):
        self._parameterTableData = {}
        
        self._currentFunction = Util.getWidgetValue(self._ui.function)
        self.loadParameterTable()

    def closeWindow(self):
        self._widget.parent().close()

    def connectSlotsOnFunctionChange(self, newFunctionName):
        """
        Disconnect slots dependent on which function is chosen.

        If polynomial function is chosen, connect slot to update parameter table
        on degree change.
        """

        # Disconnect slots
        try:
            self._ui.polynomialDegree.valueChanged[int].disconnect(self.parameterTablePolynomialRows)
        except:
            pass

        # Connect polynomial degree change
        if Util.getWidgetValue(self._ui.function) == 'Polynomial':
            self._ui.polynomialDegree.valueChanged[int].connect(self.parameterTablePolynomialRows)


    # Deal with parameter table
    def saveAndLoadParameterTable(self, newFunctionName):
        # These cannot be connected to currentIndexChanged individually
        # because they need to be called in order.
        self.saveParameterTable()
        self.loadParameterTable()

    def saveParameterTable(self):
        self._parameterTableData[self._currentFunction] = []

        # Save data to a 2-d array mimicking the table.
        # FIXME only works with text right now. Need to add in support for check boxes
        # Maybe do this by creating a QTableWidgetItem option in Util.getWidgetValue
        # and using QTableWidget.cellWidget to get the indiv. cells
        row = []
        for rowIndex in range(self._ui.parameterTable.rowCount()):
            for colIndex in range(self._ui.parameterTable.columnCount()):
                try:
                    row.append(str(self._ui.parameterTable.item(rowIndex, colIndex).text()))
                except AttributeError:
                    row.append('')
            self._parameterTableData[self._currentFunction].append(row)
            row = []
        
        # Now update _currentFunction to the function that is currently selected.
        # If this method was called because the user selected a different function,
        # then this will be modified. If it was called because the fit curve button
        # was pressed, then its value will not be changed.
        self._currentFunction = Util.getWidgetValue(self._ui.function)

    def loadParameterTable(self):
        # Clear the table, but leave all the column headers
        for rowIndex in range(self._ui.parameterTable.rowCount()):
            self._ui.parameterTable.removeRow(0)

        # If there is saved data, use it
        # FIXME same as in saveParameterTable, needs to accept checkmarks
        if self._currentFunction in self._parameterTableData:
            for rowIndex, row in enumerate(self._parameterTableData[self._currentFunction]):
                self._ui.parameterTable.insertRow(rowIndex)
                for colIndex, data in enumerate(row):
                    self._ui.parameterTable.setItem(rowIndex, colIndex, QTableWidgetItem(data))
        else:
            # If there is no saved data, create defaults here
            if self._currentFunction == 'Polynomial':
                self.parameterTablePolynomialRows()
            elif self._currentFunction == 'Sinusoid':
                self.setupParameterTableRows(['p0', 'p1', 'p2', 'p3'], [1, 1, 1, 1])
            elif self._currentFunction == 'Power Law':
                self.setupParameterTableRows(['y0', 'a', 'k'], [0, 1, 1])
            elif self._currentFunction == 'Exponential':
                self.setupParameterTableRows(['y0', 'A', 'b'], [0, 1, 1])
            elif self._currentFunction == 'Logarithm':
                self.setupParameterTableRows(['y0', 'a', 'base'], [0, 1, 10])

    def parameterTablePolynomialRows(self, *args):
        """
        If the polynomial degree the user selected is larger than the number
        of rows in the parameter table, then add extra rows here. If smaller,
        then remove rows.
        """

        degree = Util.getWidgetValue(self._ui.polynomialDegree)
        rowNames = []
        rowInitialValues = []
        for d in range(degree + 1):
            rowNames.append('p' + str(d))
            rowInitialValues.append(1)

        self.setupParameterTableRows(rowNames, rowInitialValues)

    def setupParameterTableRows(self, rowNames=[], rowInitialValues=[]):
        """
        rowNames should contain all the parameter names required in the table.
        """

        desiredNumRows = len(rowNames)
        rowCount = self._ui.parameterTable.rowCount()
        
        # Add or remove rows as necessary
        if desiredNumRows == rowCount:
            # Correct number of rows. Do nothing.
            pass 
        elif desiredNumRows < rowCount:
            # There are more rows than there should be. Remove some.
            self._ui.parameterTable.setRowCount(desiredNumRows)
        else:
            # There are fewer rows than there should be. Add some.
            self._ui.parameterTable.setRowCount(desiredNumRows)

            for d in range(rowCount, desiredNumRows):
                for colIndex in range(1, self._ui.parameterTable.columnCount()):
                    self._ui.parameterTable.setItem(d, colIndex, QTableWidgetItem())
        
        # Set parameter names
        for rowIndex, name in enumerate(rowNames):
            item = QTableWidgetItem(name)
            item.setFlags(Qt.ItemIsEnabled)
            self._ui.parameterTable.setItem(rowIndex, 0, item)

        # Set parameter initial values
        for rowIndex in range(rowCount, desiredNumRows):
            self._ui.parameterTable.item(rowIndex, 1).setText(str(rowInitialValues[rowIndex]))

    def parameterInitialValues(self, functionName):
        if functionName not in self._parameterTableData:
            return None

        tableData = self._parameterTableData[functionName]

        # Default non-number values to 1 so that we don't get trivial divide-by-0 errors
        # (but more specific checking should be done in the individual fit functions)
        initialValues = [float(row) if Util.isNumber(x) else 1 for row in tableData]
        return initialValues

    def parameterNames(self, functionName):
        if functionName not in self._parameterTableData:
            return None

        tableData = self._parameterTableData[functionName]

        names = [str(row[0]) for row in tableData]
        return names

    def doFit(self):
        # save user-defined parameters
        self.saveParameterTable()

        # Get all waves that are selected before doing anything else
        # If any waves are created, as they are in the output tab section,
        # then the wave combo boxes are refreshed, and the previous selection
        # is lost
        xWaveName = Util.getWidgetValue(self._ui.xWave)
        yWaveName = Util.getWidgetValue(self._ui.yWave)
        interpolationDomainWaveName = Util.getWidgetValue(self._ui.interpolationDomain)

        # Get data tab
        dataRangeStart = Util.getWidgetValue(self._ui.dataRangeStart)
        dataRangeEnd = Util.getWidgetValue(self._ui.dataRangeEnd)
        
        xWave = self._app.waves().wave(xWaveName)
        yWave = self._app.waves().wave(yWaveName)
        xLength = xWave.length()
        yLength = yWave.length()
        
        # Verify data range limits are valid
        if dataRangeStart > xLength or dataRangeStart > yLength:
            dataRangeStart = 0
        if dataRangeEnd > xLength or dataRangeEnd > yLength:
            dataRangeEnd = min(xLength, yLength) - 1

        xData = xWave.data(dataRangeStart, dataRangeEnd + 1)
        yData = yWave.data(dataRangeStart, dataRangeEnd + 1)

        # Get output tab
        outputOptions = {}
        outputWaves = {}

        outputOptions['createTable'] = Util.getWidgetValue(self._ui.createTable)

        outputOptions['outputParameters'] = Util.getWidgetValue(self._ui.outputParameters)
        if outputOptions['outputParameters']:
            outputOptions['saveLabels'] = Util.getWidgetValue(self._ui.saveLabels)

            # Create saveLabels wave
            if outputOptions['saveLabels']:
                saveLabelsDestination = self._app.waves().findGoodWaveName(Util.getWidgetValue(self._ui.saveLabelsDestination))
                outputWaves['saveLabelsWave'] = Wave(saveLabelsDestination, 'String')
                self._app.waves().addWave(outputWaves['saveLabelsWave'])

            # Create parameter wave
            parameterDestination = self._app.waves().findGoodWaveName(Util.getWidgetValue(self._ui.parameterDestination))
            outputWaves['parameterWave'] = Wave(parameterDestination, 'Decimal')
            self._app.waves().addWave(outputWaves['parameterWave'])

        outputOptions['outputInterpolation'] = Util.getWidgetValue(self._ui.outputInterpolation)
        if outputOptions['outputInterpolation']:
            # Create interpolation wave
            interpolationDestination = self._app.waves().findGoodWaveName(Util.getWidgetValue(self._ui.interpolationDestination))
            outputWaves['interpolationDestinationWave'] = Wave(interpolationDestination, 'Decimal')
            self._app.waves().addWave(outputWaves['interpolationDestinationWave'])
            
            interpolationDomainWave = self._app.waves().wave(interpolationDomainWaveName)
            interpolationRangeStart = Util.getWidgetValue(self._ui.interpolationRangeStart)
            interpolationRangeEnd = Util.getWidgetValue(self._ui.interpolationRangeEnd)
            
            outputWaves['interpolationDomainWave'] = interpolationDomainWave

            # Start the wave with as many blanks as necessary in order to get the destination wave
            # to line up correctly with the domain wave, for easy plotting.
            outputWaves['interpolationDestinationWave'].extend([''] * interpolationRangeStart)
            
            # Verify data range limits are valid
            interpolationDomainLength = interpolationDomainWave.length()
            if interpolationRangeStart > interpolationDomainLength:
                interpolationRangeStart = 0
            if interpolationRangeEnd > interpolationDomainLength:
                interpolationRangeEnd  = interpolationDomainLength - 1

            outputOptions['interpolationDomainWaveData'] = interpolationDomainWave.data(interpolationRangeStart, interpolationRangeEnd + 1)

        # Determine the function and call the appropriate method
        functionName = Util.getWidgetValue(self._ui.function)

        if functionName == 'Polynomial':
            self.fitPolynomial(xData, yData, outputWaves, outputOptions)
        elif functionName == 'Sinusoid':
            self.fitSinusoid(xData, yData, outputWaves, outputOptions)
        elif functionName == 'Power Law':
            self.fitPowerLaw(xData, yData, outputWaves, outputOptions)
        elif functionName == 'Exponential':
            self.fitExponential(xData, yData, outputWaves, outputOptions)
        elif functionName == 'Logarithm':
            self.fitLogarithm(xData, yData, outputWaves, outputOptions)

    def fitPolynomial(self, xData, yData, outputWaves={}, outputOptions={}):
        # Get the degree of the polynomial the user wants to use
        degree = Util.getWidgetValue(self._ui.polynomialDegree)

        def polynomialFunction(p, x):
            # If x is a list, then val needs to be a list
            # If x is a number, then val needs to be a number
            if isinstance(x, list):
                val = numpy.array([p[0]] * len(x))
            else:
                val = p[0]

            # Add x, x^2, x^3, etc entries
            for d in range(1, degree + 1):
                val += numpy.multiply(p[d], numpy.power(x, d))
            return val

        parameterNames = self.parameterNames('Polynomial')
        initialValues = self.parameterInitialValues('Polynomial')
        if initialValues is None:
            initialValues = [1] * degree

        self.fitFunction(polynomialFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Polynomial Fit')

    def fitSinusoid(self, xData, yData, outputWaves={}, outputOptions={}):
        sinusoidFunction = lambda p, x: p[0] + p[1] * numpy.cos(x / p[2] * 2. * numpy.pi + p[3])
        
        parameterNames = self.parameterNames('Sinusoid')
        initialValues = self.parameterInitialValues('Sinusoid')
        if initialValues is None:
            initialValues = [1, 1, 1, 1]

        self.fitFunction(sinusoidFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Sinusoid Fit')

    def fitPowerLaw(self, xData, yData, outputWaves={}, outputOptions={}):
        powerLawFunction = lambda p, x: numpy.add(p[0], numpy.multiply(p[1], numpy.power(x, p[2])))

        parameterNames = self.parameterNames('Power Law')
        initialValues = self.parameterInitialValues('Power Law')
        if initialValues is None:
            initialValues = [0, 1, 1]

        self.fitFunction(powerLawFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Power Law Fit')

    def fitExponential(self, xData, yData, outputWaves={}, outputOptions={}):
        exponentialFunction = lambda p, x: numpy.add(p[0], numpy.multiply(p[1], numpy.power(numpy.e, numpy.multiply(p[2], x))))

        parameterNames = self.parameterNames('Exponential')
        initialValues = self.parameterInitialValues('Exponential')
        if initialValues is None:
            initialValues = [0, 1, 1]

        self.fitFunction(exponentialFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Exponential Fit')

    def fitLogarithm(self, xData, yData, outputWaves={}, outputOptions={}):
        # There is no numpy log function where you can specify a custom base, so we'll define one
        customBaseLog = lambda base, x: numpy.divide(numpy.log(x), numpy.log(base))
        logarithmFunction = lambda p, x: numpy.add(p[0], numpy.multiply(p[1], customBaseLog(p[2], x)))

        parameterNames = self.parameterNames('Logarithm')
        initialValues = self.parameterInitialValues('Logarithm')
        if initialValues is None:
            initialValues = [0, 1, 10]

        self.fitFunction(logarithmFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Logarithm Fit')



    def fitFunction(self, function, parameterNames, initialValues, xData, yData, outputWaves={}, outputOptions={}, tableName='Fit'):
        # Can also include initial guesses for the parameters, as well as sigma's for weighting of the ydata

        # Need to fail with error message if the leastsq call does not succeed

        # Do the fit
        result = self.fitFunctionLeastSquares(function, initialValues, xData, yData)
        parameters = result[0]

        tableWaves = []

        # Deal with the parameter-related waves
        if outputOptions['outputParameters']:
            # save parameter labels
            if outputOptions['saveLabels']:
                tableWaves.append(outputWaves['saveLabelsWave'])

                outputWaves['saveLabelsWave'].extend(parameterNames)

            tableWaves.append(outputWaves['parameterWave'])

            # save parameters to a wave
            outputWaves['parameterWave'].extend(parameters)

        # Do the interpolation
        if outputOptions['outputInterpolation']:
            domain = outputOptions['interpolationDomainWaveData']
            
            determinedFunction = lambda x: function(parameters, x)
            for val in domain:
                outputWaves['interpolationDestinationWave'].push(determinedFunction(val))

            tableWaves.append(outputWaves['interpolationDomainWave'])
            tableWaves.append(outputWaves['interpolationDestinationWave'])

        # Create table
        if outputOptions['createTable']:
            self.createTable(tableWaves, tableName)

    def fitFunctionLeastSquares(self, func, guess, xData, yData):
        """
        Do a least squares fit for a generic function.

        func must have the signature (p, x) where p is a list of parameters
        and x is a float.

        guess is the user's guess of the parameters, and must be a list of 
        length len(p).

        xData and yData are the data to fit.
        """

        errorFunc = lambda p, x, y: func(p, x) - y

        return scipy.optimize.leastsq(errorFunc, guess[:], args=(xData, yData), full_output=True)


    def createTable(self, waves=[], title='Fit'):
        if len(waves) == 0:
            return

        self._app.createTable(waves, title)



    def load(self):
        self.window = SubWindow(self._app.ui.workspace)

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("actionCurveFiting")
        self.menuEntry.setText("Curve Fitting")
        self.menuEntry.triggered.connect(self.window.show)
        
        self.menu = vars(self._app.ui)["menuData"]
        self.menu.addAction(self.menuEntry)

        self.buildWidget()
        self.window.setWidget(self._widget)
        self._widget.setParent(self.window)

        self.window.hide()

    def unload(self):

        self._widget.deleteLater()
        self.window.deleteLater()
        self.menu.removeAction(self.menuEntry)

    def reload(self):
        self.setModels()
        self.setupSpinBoxes()
        self.setupParameterTableData()

