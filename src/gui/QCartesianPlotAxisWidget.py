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


from Wave import *
from models.WavesListModel import WavesListModel
from QEditFigureSubWidget import *
from Property import GenericAxis

class QCartesianPlotAxisWidget(QEditFigureSubWidget):

    properties = GenericAxis.default.keys()

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


