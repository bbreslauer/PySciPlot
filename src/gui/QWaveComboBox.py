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


from PyQt4.QtGui import QComboBox, QApplication

class QWaveComboBox(QComboBox):
    """
    Extend QComboBox so that it includes functionality to 
    deal with resetting the model but keeping the selection
    present.
    """

    def __init__(self, parent=None):
        QComboBox.__init__(self, parent)

    def setModel(self, model):
        """
        Override setModel to include connections and disconnections for the
        reset-based signals. The model's reset-based signals are used to 
        determine what the current index is, and to set it back to that
        after the model has been reset.
        """

        if self.model():
            try:
                self.model().modelAboutToBeReset.disconnect(self.beforeReset)
            except:
                pass
            try:
                self.model().modelReset.disconnect(self.afterReset)
            except:
                pass

        QComboBox.setModel(self, model)

        self.model().modelAboutToBeReset.connect(self.beforeReset)
        self.model().modelReset.connect(self.afterReset)


    def beforeReset(self):
        """
        Determine the current index and save it to the combo box.
        """
        self._currentItem = self.currentText()

    def afterReset(self):
        """
        Reset the current and selected item to what was saved to the combo box
        in beforeReset. If the saved item is no longer in the model, default
        to the first item in the view.
        """
        
        if self._currentItem:
            index = self.model().getIndexByWaveName(self._currentItem)
            if index < 0:
                index = 0
            self.setCurrentIndex(index)
            del self._currentItem
        else:
            # There was no current item, so default to the beginning of the list
            self.setCurrentIndex(0)

