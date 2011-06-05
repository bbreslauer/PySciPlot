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
from numpy import pi, e
from Wave import Wave
from Module import Module
from gui.SubWindows import SubWindow
from ui.Ui_CurveFitting import Ui_CurveFitting

class CurveFitting(Module):
    """Module to fit waves to a function."""

    # To add new fitting functions, do the following:
    # 1) Edit GUI
    # 2) Modify _parameterTableDefaults
    # 3) Create a fit[Function] method to do the fitting
    # 4) Call fit[Function] from doFit

    # Default values for parameter table
    # Each dict entry is a list of lists. The inner list contains a row of values.
    _parameterTableDefaults = {
            'Polynomial': [
                ['p0', 1],
                ['p1', 1],
                ['p2', 1],
                ],
            'Sinusoid': [
                ['p0', 1],
                ['p1', 1],
                ['p2', 1],
                ['p3', 1],
                ],
            'Power Law': [
                ['y0', 0],
                ['a', 1],
                ['k', 1],
                ],
            'Exponential': [
                ['y0', 0],
                ['A', 1],
                ['b', 1],
                ],
            'Logarithm': [
                ['y0', 0],
                ['a', 1],
                ['base', 10],
                ],
            'Gaussian': [
                ['amp', 1],
                ['mean', 0],
                ['width', 1],
                ],
            'Lorentzian': [
                ['amp', 1],
                ['mean', 0],
                ['hwhm', 1],
                ],
            }

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
        self._ui.function.currentIndexChanged[str].connect(self.changeFunction)
        self._ui.function.currentIndexChanged[str].connect(self.connectSlotsOnFunctionChange)
        self._ui.initialValuesWave.activated[str].connect(self.changeInitialValuesWave)
        self._ui.useInitialValuesWave.toggled[bool].connect(self.changeInitialValuesWaveFromCheckbox)
        
        self.connectSlotsOnFunctionChange('')

    def setModels(self):
        # Set up model and view
        self._allWavesListModel = self._app.model('appWaves')
        self._ui.xWave.setModel(self._allWavesListModel)
        self._ui.yWave.setModel(self._allWavesListModel)
        self._ui.initialValuesWave.setModel(self._allWavesListModel)
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
        self._currentFunction = None
        self.changeFunction('')
    
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
            self._ui.polynomialDegree.valueChanged[int].disconnect(self.changePolynomialDegree)
        except:
            pass

        # Connect polynomial degree change
        if Util.getWidgetValue(self._ui.function) == 'Polynomial':
            self._ui.polynomialDegree.valueChanged[int].connect(self.changePolynomialDegree)

    def changeFunction(self, newFunctionName):
        # Save parameters for old function
        if self._currentFunction:
            self._parameterTableData[self._currentFunction] = self.getCurrentParameterTable()

        # Now update _currentFunction to the function that is currently selected.
        # If this method was called because the user selected a different function,
        # then this will be modified. If it was called because the fit curve button
        # was pressed, then its value will not be changed.
        self._currentFunction = Util.getWidgetValue(self._ui.function)

        # Enter in parameters for new function
        # If there are previously user-entered values, then use them
        # else, if a wave is selected, then use that
        # else, use the initial values
        # Either way, if there are blank entries, then use initial values for them

        # Clear the table, but leave all the column headers
        for rowIndex in range(self._ui.parameterTable.rowCount()):
            self._ui.parameterTable.removeRow(0)

        parameters = []
        # If there is saved data, use it
        if self._currentFunction in self._parameterTableData:
            parameters = self._parameterTableData[self._currentFunction]

        # If there aren't enough rows for all the parameters, extend with 
        # initial values. This will also occur if no parameters had been saved.
        savedParametersLength = len(parameters)
        defaultParameters = self._parameterTableDefaults[self._currentFunction]
        if savedParametersLength < len(defaultParameters):
            parameters.extend(defaultParameters[len(parameters):])
            
            # Use wave if requested by the user
            if Util.getWidgetValue(self._ui.useInitialValuesWave):
                # Convert from QString to str
                waveName = str(Util.getWidgetValue(self._ui.initialValuesWave))
                if self._app.waves().wave(waveName) is None:
                    # waveName is not a name of a wave
                    pass
                else:
                    waveData = self._app.waves().wave(waveName).data()
                    for i in range(savedParametersLength, len(defaultParameters)):
                        parameters[i][1] = waveData[i]
        
        self.writeParametersToTable(parameters)

    def writeParametersToTable(self, parameters, startRow=0):
        # Determine how many rows the table should have
        numRows = startRow + len(parameters)
        self._ui.parameterTable.setRowCount(numRows)

        # Now actually write to the table
        for rowIndex, row in enumerate(parameters, startRow):
            for colIndex, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                if colIndex == 0:
                    # parameter name, do not want it editable
                    item.setFlags(Qt.ItemIsEnabled)

                self._ui.parameterTable.setItem(rowIndex, colIndex, item)
                
    def changePolynomialDegree(self, newDegree):
        # If decreasing the degree, just remove the last entries
        # If increasing the degree,
        #    If a wave is selected, then use that for the new values
        #    else, use the initial values
        
        desiredNumRows = newDegree + 1
        currentNumRows = self._ui.parameterTable.rowCount()
        
        if desiredNumRows == currentNumRows:
            # Nothing to do
            return

        # Set defaults
        rows = []
        for d in range(desiredNumRows):
            rows.append(['p' + str(d), 1])
        self._parameterTableDefaults['Polynomial'] = rows

        # Update table
        self._ui.parameterTable.setRowCount(desiredNumRows)

        if desiredNumRows < currentNumRows:
            # We are done, because no rows need to be edited
            return

        # Degree is being increased
        parameters = self._parameterTableDefaults['Polynomial'][currentNumRows:desiredNumRows]
        if Util.getWidgetValue(self._ui.useInitialValuesWave):
            # Convert from QString to str
            waveName = str(Util.getWidgetValue(self._ui.initialValuesWave))
            if self._app.waves().wave(waveName) is None:
                # waveName is not a name of a wave
                pass
            else:
                waveData = self._app.waves().wave(waveName).data(currentNumRows, desiredNumRows)
                for index, value in enumerate(waveData):
                    parameters[index][1] = value

        self.writeParametersToTable(parameters, currentNumRows)

    def changeInitialValuesWaveFromCheckbox(self, checked):
        """
        If the useInitialValuesWave checkbox is checked, then
        call changeInitialValuesWave.
        """

        if checked:
            self.changeInitialValuesWave(str(Util.getWidgetValue(self._ui.initialValuesWave)))

    def changeInitialValuesWave(self, waveName):
        # Use the wave for as many parameters as possible
        # if the wave is too long, then just use the first n values
        # if the wave is too short, then leave the current value in place
        #     if there is no current value, then use the initial values

        if Util.getWidgetValue(self._ui.useInitialValuesWave):
            # Get the current values, with any undefined values using the initial values
            parameters = self.currentParametersBackedByInitials()

            # Now get the wave values
            parameters = self.updateParametersListWithWave(parameters, waveName)

            # Set the table to the parameters
            self.writeParametersToTable(parameters)


    def updateParametersListWithWave(self, parameters, waveName):
        """
        Given a list of parameter table rows, and the name of a wave,
        this will update the parameter values with the entries in the wave.
        """

        waveName = str(waveName)
        if self._app.waves().wave(waveName) is None:
            # waveName is not a name of a wave
            return parameters

        waveData = self._app.waves().wave(waveName).data(0, len(parameters))
        for i in range(len(waveData)):
            parameters[i][1] = waveData[i]

        return parameters

    def currentParametersBackedByInitials(self):
        # Start with initial values
        parameters = self._parameterTableDefaults[self._currentFunction]

        # Then get the current values and update parameters with it
        currentParameters = self.getCurrentParameterTable()
        for rowIndex, row in enumerate(currentParameters):
            parameters[rowIndex] = row

        return parameters

    def getCurrentParameterTable(self):
        """
        Save data to a 2-d array mimicking the table.
        """
        # FIXME only works with text right now. Need to add in support for check boxes
        # Maybe do this by creating a QTableWidgetItem option in Util.getWidgetValue
        # and using QTableWidget.cellWidget to get the indiv. cells
        table = []
        row = []
        for rowIndex in range(self._ui.parameterTable.rowCount()):
            for colIndex in range(self._ui.parameterTable.columnCount()):
                try:
                    row.append(str(self._ui.parameterTable.item(rowIndex, colIndex).text()))
                except AttributeError:
                    row.append('')
            table.append(row)
            row = []

        return table

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
        elif functionName == 'Gaussian':
            self.fitGaussian(xData, yData, outputWaves, outputOptions)
        elif functionName == 'Lorentzian':
            self.fitLorentzian(xData, yData, outputWaves, outputOptions)

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

    def fitGaussian(self, xData, yData, outputWaves={}, outputOptions={}):
        gaussianFunction = lambda p, x: numpy.multiply(p[0], numpy.power(numpy.e, numpy.divide(-1 * numpy.power((numpy.subtract(x, p[1])), 2), 2 * numpy.power(p[2], 2))))

        parameterNames = self.parameterNames('Gaussian')
        initialValues = self.parameterInitialValues('Gaussian')
        if initialValues is None:
            initialValues = [1, 0, 1]

        self.fitFunction(gaussianFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Gaussian Fit')

    def fitLorentzian(self, xData, yData, outputWaves={}, outputOptions={}):
        lorentzianFunction = lambda p, x: numpy.divide(numpy.multiply(p[0], p[2]), numpy.add(numpy.power(numpy.subtract(x, p[1]), 2), numpy.power(p[2], 2)))

        parameterNames = self.parameterNames('Lorentzian')
        initialValues = self.parameterInitialValues('Lorentzian')
        if initialValues is None:
            initialValues = [1, 0, 1]

        self.fitFunction(lorentzianFunction, parameterNames, initialValues, xData, yData, outputWaves, outputOptions, 'Lorentzian Fit')



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
        Util.setWidgetValue(self._ui.function, 'Polynomial')
        Util.setWidgetValue(self._ui.useInitialValuesWave, False)

