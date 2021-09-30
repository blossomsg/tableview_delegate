from PyQt5 import QtCore


class TableModel(QtCore.QAbstractTableModel):
	def __init__(self, cols_strings, rows_strings, empty_strings, parent=None):
		super(TableModel, self).__init__(parent)

		self.colStringsList = cols_strings
		self.rowStringsList = rows_strings
		self.data = empty_strings

	def rowCount(self, index=QtCore.QModelIndex()):
		return len(self.data)

	def columnCount(self, index=QtCore.QModelIndex()):
		return len(self.data)

	def data(self, index=QtCore.QModelIndex, role=QtCore.Qt.DisplayRole):
		if index.isValid():
			if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
				value = self.data[index.row()][index.column()]
				return str(value)

	def setData(self, index=QtCore.QModelIndex, value=QtCore.QVariant, role=QtCore.Qt.EditRole):
		if role == QtCore.Qt.EditRole:
			self.data[index.row()][index.column()] = value
			return True
		return False

	def headerData(self, section, orientation=QtCore.Qt.Orientation, role=QtCore.Qt.DisplayRole):
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				return self.colStringsList[section]
			if orientation == QtCore.Qt.Vertical:
				return self.rowStringsList[section]

	def flags(self, index):
		return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable
