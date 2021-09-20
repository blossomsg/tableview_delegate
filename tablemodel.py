from PyQt5 import QtCore


class TableModel(QtCore.QAbstractTableModel):
	def __init__(self, strings, parent=None):
		super(TableModel, self).__init__(parent)

		self.stringsList = strings

	def rowCount(self, index=QtCore.QModelIndex()):
		return len(self.stringsList)

	def columnCount(self, index=QtCore.QModelIndex()):
		return len(self.stringsList)

	def data(self, index=QtCore.QModelIndex(), role=QtCore.Qt.DisplayRole):
		if not index.isValid():
			return None
		elif role == QtCore.Qt.DisplayRole:
			return None

	def headerData(self, section, orientation=QtCore.Qt.Orientation, role=QtCore.Qt.DisplayRole):
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				return self.stringsList[section]
