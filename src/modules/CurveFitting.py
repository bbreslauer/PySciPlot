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
        self._ui.dataRangeStart.addWaveView(self._ui.yWave)
        self._ui.dataRangeEnd.addWaveView(self._ui.xWave)
        self._ui.dataRangeEnd.addWaveView(self._ui.yWave)


    def closeWindow(self):
        self._widget.parent().close()



    def doFit(self):
        # Get data tab
        xWaveName = Util.getWidgetValue(self._ui.xWave)
        yWaveName = Util.getWidgetValue(self._ui.yWave)
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

        xData = xWave.data(dataRangeStart, dataRangeEnd)
        yData = yWave.data(dataRangeStart, dataRangeEnd)

        # Get output tab
        outputOptions = {}
        outputOptions['createTable'] = Util.getWidgetValue(self._ui.createTable)
        outputOptions['outputCoefficients'] = Util.getWidgetValue(self._ui.outputCoefficients)
        if outputOptions['outputCoefficients']:
            outputOptions['coefficientDestination'] = Util.getWidgetValue(self._ui.coefficientDestination)
            outputOptions['saveLabels'] = Util.getWidgetValue(self._ui.saveLabels)
            if outputOptions['saveLabels']:
                outputOptions['saveLabelsDestination'] = Util.getWidgetValue(self._ui.saveLabelsDestination)
            outputOptions['saveFitParameters'] = Util.getWidgetValue(self._ui.saveFitParameters)

        outputOptions['outputInterpolation'] = Util.getWidgetValue(self._ui.outputInterpolation)
        if outputOptions['outputInterpolation']:
            outputOptions['interpolationDestination'] = Util.getWidgetValue(self._ui.interpolationDestination)

            interpolationDomainWaveName = Util.getWidgetValue(self._ui.interpolationDomain)
            interpolationWave = self._app.waves().wave(interpolationDomainWaveName)
            interpolationRangeStart = Util.getWidgetValue(self._ui.interpolationRangeStart)
            interpolationRangeEnd = Util.getWidgetValue(self._ui.interpolationRangeEnd)
            
            interpolationDomainLength = interpolationWave.length()
            if interpolationRangeStart > interpolationDomainLength:
                interpolationRangeStart = 0
            if interpolationRangeEnd > interpolationDomainLength:
                interpolationRangeEnd  = interpolationDomainLength - 1

            outputOptions['interpolationWaveData'] = interpolationWave.data(interpolationRangeStart, interpolationRangeEnd)

        # Determine the function and call the appropriate method
        functionName = Util.getWidgetValue(self._ui.function)

        if functionName == 'Polynomial':
            self.fitPolynomial(xData, yData, outputOptions)




    def fitPolynomial(self, xData, yData, outputOptions={}):
        degree = Util.getWidgetValue(self._ui.polynomialDegree)
        coeffs, residuals, rank, singular_values, rcond = numpy.polyfit(xData, yData, degree, full=True)

        if outputOptions['outputCoefficients']:
            # save coefficient labels
            if outputOptions['saveLabels']:
                saveLabelsDestination = self._app.waves().findGoodWaveName(outputOptions['saveLabelsDestination'])
                saveLabelsWave = Wave(saveLabelsDestination, 'String')
                self._app.waves().addWave(saveLabelsWave)

                for deg in range(degree + 1):
                    saveLabelsWave.insert(0, 'Deg ' + str(deg))

                if outputOptions['saveFitParameters']:
                    saveLabelsWave.push('Residuals')
                    saveLabelsWave.push('Rank')
                    saveLabelsWave.extend(['Singular Values'] * (deg + 1))
                    saveLabelsWave.push('RCond')

            # save coefficients to a wave
            coefficientDestination = self._app.waves().findGoodWaveName(outputOptions['coefficientDestination'])
            coefficientWave = Wave(coefficientDestination, 'Decimal')
            self._app.waves().addWave(coefficientWave)
            coefficientWave.extend(coeffs)

            if outputOptions['saveFitParameters']:
                coefficientWave.extend([list(residuals), rank, list(singular_values), rcond])

        if outputOptions['outputInterpolation']:
            domain = outputOptions['interpolationWaveData']
            interpolationDestination = self._app.waves().findGoodWaveName(outputOptions['interpolationDestination'])
            interpolationDestinationWave = Wave(interpolationDestination, 'Decimal')
            self._app.waves().addWave(interpolationDestinationWave)

            interpolationDestinationWave.extend(list(numpy.polyval(coeffs, domain)))


        # TODO add createTable logic


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

