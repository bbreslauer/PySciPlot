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


from PySide.QtCore import Signal

from Wave import *
from models.WavesListModel import WavesListModel
from QEditFigureSubWidget import *
from Property import GenericAxis

class QCartesianPlotAxisWidget(QEditFigureSubWidget):

    properties = GenericAxis.default.keys()

    def __init__(self, plotTypeWidget, axisName, *args):
        QEditFigureSubWidget.__init__(self, *args)
        self._plotTypeWidget = plotTypeWidget
        self._axisName = axisName

    def connectSignals(self):
        self.getChild('autoscale').stateChanged.connect(self.emitScalePropertiesChanged)
        self.getChild('scaleType').currentIndexChanged.connect(self.emitScalePropertiesChanged)
        self.getChild('minimum').textChanged.connect(self.emitScalePropertiesChanged)
        self.getChild('maximum').textChanged.connect(self.emitScalePropertiesChanged)

        self.getChild('slaveAxisToOther').stateChanged.connect(self.getMirroredScaleProperties)
        self.getChild('slavedTo').currentIndexChanged.connect(self.getMirroredScaleProperties)

    def initSubWidgets(self):
        self._wavesModel = self._app.model('appWaves')
        self.getChild('majorTicksLabelWave').setModel(self._wavesModel)
        self.getChild('majorTicksWaveValues').setModel(self._wavesModel)

    def changeScaleType(self, scaleType):
        if scaleType == 'Linear':
            self.getChild('majorTicksLocationsStackedWidget').setCurrentIndex(0)
            self.getChild('minorTicksLocationsStackedWidget').setCurrentIndex(0)
        else:
            self.getChild('majorTicksLocationsStackedWidget').setCurrentIndex(1)
            self.getChild('minorTicksLocationsStackedWidget').setCurrentIndex(1)

    def enableAnchorToValue(self, b):
        self.getChild('useMajorTicksAnchor').setEnabled(True)
        if self.getChild('useMajorTicksAnchor').isChecked():
            self.getChild('majorTicksAnchor').setEnabled(True)

    def disableAnchorToValue(self, b):
        self.getChild('useMajorTicksAnchor').setEnabled(False)
        self.getChild('majorTicksAnchor').setEnabled(False)

    def setAxisVisible(self, b):
        """
        Set the various group boxes to be enabled or disabled, based on
        whether the axis is set to be visible.
        """

        if not b:
            self.getChild('scaleGroupBox').setEnabled(False)
            self.getChild('majorTicksVisible').setEnabled(False)
            self.getChild('minorTicksVisible').setEnabled(False)
        else:
            self.getChild('majorTicksVisible').setEnabled(True)
            if self.getChild('majorTicksVisible').isChecked():
                self.getChild('minorTicksVisible').setEnabled(True)
            if not self.getChild('slaveAxisToOther').isChecked():
                self.getChild('scaleGroupBox').setEnabled(True)

    # Used when mirroring an axis, to keep the state consistent between axes.
    scalePropertiesChanged = Signal(str, bool, str, str, str)
    def emitScalePropertiesChanged(self, *args):
        self.scalePropertiesChanged.emit(self._axisName,
                                        Util.getWidgetValue(self.getChild('autoscale')),
                                        Util.getWidgetValue(self.getChild('scaleType')),
                                        Util.getWidgetValue(self.getChild('minimum')),
                                        Util.getWidgetValue(self.getChild('maximum')),
                                        )

    def changeScaleProperties(self, axisName, autoscale, scaleType, minimum, maximum):
        # change the scale properties to whatever is passed in. used when mirroring an axis
        if Util.getWidgetValue(self.getChild('slaveAxisToOther')) and axisName == Util.getWidgetValue(self.getChild('slavedTo')):
            Util.setWidgetValue(self.getChild('autoscale'), autoscale)
            Util.setWidgetValue(self.getChild('scaleType'), scaleType)
            Util.setWidgetValue(self.getChild('minimum'), minimum)
            Util.setWidgetValue(self.getChild('maximum'), maximum)

    def getMirroredScaleProperties(self):
        # force mirrored (master) axis to emit scalePropertiesChanged, so that we can update
        # this axis with the properties.
        if Util.getWidgetValue(self.getChild('slaveAxisToOther')) and self._axisName != Util.getWidgetValue(self.getChild('slavedTo')):
            self._plotTypeWidget.forceScalePropertiesUpdate(Util.getWidgetValue(self.getChild('slavedTo')))

