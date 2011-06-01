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


from PyQt4.QtGui import QWidget, QAction

import Util, numpy
from Wave import Wave
from Module import Module
from gui.SubWindows import SubWindow
from ui.Ui_CurveFitting import Ui_CurveFitting

class CurveFitting(Module):
    """Module to fit waves to a function."""

    def __init__(self):
        Module.__init__(self)

    def buildWidget(self):
        self._widget = QWidget()
        self._ui = Ui_CurveFitting()
        self._ui.setupUi(self._widget)

        self.setModels()
        self.setupSpinBoxes()

        # Connect button signals
        self._ui.doFitButton.clicked.connect(self.doFit)
        self._ui.closeButton.clicked.connect(self.closeWindow)

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


    def closeWindow(self):
        self._widget.parent().close()



    def doFit(self):
        
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

        outputOptions['outputCoefficients'] = Util.getWidgetValue(self._ui.outputCoefficients)
        if outputOptions['outputCoefficients']:
            outputOptions['saveLabels'] = Util.getWidgetValue(self._ui.saveLabels)
            outputOptions['saveFitParameters'] = Util.getWidgetValue(self._ui.saveFitParameters)

            # Create saveLabels wave
            if outputOptions['saveLabels']:
                saveLabelsDestination = self._app.waves().findGoodWaveName(Util.getWidgetValue(self._ui.saveLabelsDestination))
                outputWaves['saveLabelsWave'] = Wave(saveLabelsDestination, 'String')
                self._app.waves().addWave(outputWaves['saveLabelsWave'])

            # Create coefficient wave
            coefficientDestination = self._app.waves().findGoodWaveName(Util.getWidgetValue(self._ui.coefficientDestination))
            outputWaves['coefficientWave'] = Wave(coefficientDestination, 'Decimal')
            self._app.waves().addWave(outputWaves['coefficientWave'])

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




    def fitPolynomial(self, xData, yData, outputWaves={}, outputOptions={}):
        # Get the degree of the polynomial the user wants to use
        degree = Util.getWidgetValue(self._ui.polynomialDegree)

        # Do the polynomial fit
        coeffs, residuals, rank, singular_values, rcond = numpy.polyfit(xData, yData, degree, full=True)

        tableWaves = []

        # Deal with the coefficient-related waves
        if outputOptions['outputCoefficients']:
            # save coefficient labels
            if outputOptions['saveLabels']:
                tableWaves.append(outputWaves['saveLabelsWave'])

                for deg in range(degree + 1):
                    outputWaves['saveLabelsWave'].insert(0, 'Deg ' + str(deg))

                if outputOptions['saveFitParameters']:
                    outputWaves['saveLabelsWave'].push('Residuals')
                    outputWaves['saveLabelsWave'].push('Rank')
                    outputWaves['saveLabelsWave'].extend(['Singular Values'] * (deg + 1))
                    outputWaves['saveLabelsWave'].push('RCond')

            tableWaves.append(outputWaves['coefficientWave'])

            # save coefficients to a wave
            outputWaves['coefficientWave'].extend(coeffs)

            if outputOptions['saveFitParameters']:
                outputWaves['coefficientWave'].extend([list(residuals), rank, list(singular_values), rcond])

        # Do the interpolation
        if outputOptions['outputInterpolation']:
            domain = outputOptions['interpolationDomainWaveData']
            
            outputWaves['interpolationDestinationWave'].extend(list(numpy.polyval(coeffs, domain)))

            tableWaves.append(outputWaves['interpolationDomainWave'])
            tableWaves.append(outputWaves['interpolationDestinationWave'])

        # Create table
        self.createTable(tableWaves, 'Polynomial Fit')

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

