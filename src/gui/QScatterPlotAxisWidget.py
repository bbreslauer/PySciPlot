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

class QScatterPlotAxisWidget(QEditFigureSubWidget):

    properties = GenericAxis.default.keys()

    def initSubWidgets(self):
        self._wavesModel = WavesListModel(self._app.waves())
        self.getChild('majorTicksLabelWave').setModel(self._wavesModel)
        self.getChild('majorTicksWaveValues').setModel(self._wavesModel)
        self._app.waves().waveAdded.connect(self._wavesModel.doReset)
        self._app.waves().waveRemoved[Wave].connect(self._wavesModel.doReset)

