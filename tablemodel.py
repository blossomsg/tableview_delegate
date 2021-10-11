from PyQt5 import QtCore


class TableModel(QtCore.QAbstractTableModel):
	def __init__(self, head_columns_names, head_rows_names, table_rows_count=int, table_columns_count=int, parent=None):
		super(TableModel, self).__init__(parent)

		self.headColStringsList = head_columns_names
		self.headRowStringsList = head_rows_names
		self.data = []  # this is just an empty data to use for row
		self.data_column = []  # this is just an empty data to use for column because
		self.table_rows_count = table_rows_count
		self.table_columns_count = table_columns_count

	def rowCount(self, parent=QtCore.QModelIndex):
		return len(self.data)

	def columnCount(self, parent=QtCore.QModelIndex()):
		return len(self.data_column)

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
				return self.headColStringsList[section]
			if orientation == QtCore.Qt.Vertical:
				return self.headRowStringsList[section]

	def flags(self, index):
		return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

	def insertRow(self, position, index=QtCore.QModelIndex()):
		self.insertRows(position, self.table_rows_count, index)

	def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
		self.beginInsertRows(parent, position, position + rows - 1)
		for row in range(0, rows):
			# mention rows as per the column count
			self.data.insert(position, ["", "", "", "",""])
		self.endInsertRows()
		return True

	def insertColumn(self, position, index=QtCore.QModelIndex()):
		self.insertColumns(position, self.table_columns_count, index)

	def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
		self.beginInsertColumns(parent, position, position + columns - 1)
		for column in range(0, columns):
			# mention the column type here example [] (empty list)
			self.data_column.insert(position, [])
		self.endInsertColumns()
		return True
