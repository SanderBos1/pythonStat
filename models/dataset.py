from PyQt6 import QtCore
from PyQt6.QtCore import Qt

class pandas_dataset(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(pandas_dataset, self).__init__()
        self._data = data.getDataset()

    #loads the data, select the row and column from the dataframe
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])

    def rowCount(self, index):
        #returns the amount of rows.
        return self._data.shape[0]

    def columnCount(self, index):
        # Returns the amount of columns
        return self._data.shape[1]
    
    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal :
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

        return None