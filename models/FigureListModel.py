from PyQt4.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant

class FigureListModel(QAbstractListModel):
    """
    A list of all the figures in the application.
    """

    def __init__(self, figures, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.parent = parent
        self._figures = figures

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in this model."""
        return self._figures.length()

    def data(self, index, role):
        """Return the name of the figure entry at the given index."""

        if index.isValid() and (role == Qt.DisplayRole or role == Qt.EditRole):
            return self._figures.getFigure(index.row()).name()
        return QVariant()

    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal:
            return QVariant("Figures")
        elif orientation == Qt.Vertical:
            return QVariant(section)
        return QVariant()

    def flags(self, index):
        """Return the flags for the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def setData(self, index, value, role):
        "Change the name for the figure at index."""
        if index.isValid() and role == Qt.EditRole:
            # Do not allow for blank figure names
            if value == "":
                return False
            self._figures.getFigure(index.row()).rename(str(value.toString()))
            return True
        return False

    def doReset(self, *args):
        """Take any number of arguments and just reset the model."""
        self.reset()


