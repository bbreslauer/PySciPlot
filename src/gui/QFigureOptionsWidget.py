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


from PySide.QtGui import QWidget, QApplication, QDialogButtonBox

import Util
from QEditFigureSubWidget import *

class QFigureOptionsWidget(QEditFigureSubWidget):

    properties = (  
                 'windowTitle',
                 'title',
                 'titleFont',
                 'rows',
                 'columns',
                 'width',
                 'height',
                 'axesPadding',
                 'backgroundColor',
                 'linkPlotAxes',
                )

    def saveUi(self):
        """Save the UI data to the current Figure object."""
        
        self._editFigureDialogModule.currentFigure().setMultiple(self.getCurrentUi())

    def resetUi(self):
        """Set the UI to the current Figure's settings."""
        try:
            self.setCurrentUi(self._editFigureDialogModule.currentFigure().properties)
        except:
            # There were probably no figures available (the last one was deleted) and so properties doesn't exist.
            # In this case, just leave the current options alone.
            pass

    def resetUiSize(self):
        """Set the UI to the current Figure's settings, but only for the width and height."""

        size = {}
        size['width'] = self._editFigureDialogModule.currentFigure().properties['width']
        size['height'] = self._editFigureDialogModule.currentFigure().properties['height']

        try:
            self.setCurrentUi(size)
        except:
            pass

    def reload(self):
        pass
