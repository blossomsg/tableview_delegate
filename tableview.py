from ui.table_view_delgate import Ui_Form
from tablemodel import TableModel
from PyQt5 import QtWidgets
from tabledelegate import TableDelegate
import sys
import json

with open('configuration_file.json') as data:
	config = json.load(data)
table_strings = config


class TableView(QtWidgets.QWidget):
	"""
	Tableview to test the delegates for multiple rows and columns
	"""

	def __init__(self):
		super(TableView, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		# fetch the col header names
		self.table_col_names = [col for col in config.keys()]
		# creating row numbers with range
		self.table_row_names = [row for row in range(10)]
		# setup the table header rows and column names, and row and column count
		self.model = TableModel(head_columns_names=self.table_col_names, head_rows_names=self.table_row_names)
		self.delegate = TableDelegate()
		self.model.insertRow(0)  # position of the inserted row
		self.model.insertColumn(0)  # position of the inserted column
		self.ui.tableView.setModel(self.model)
		self.ui.tableView.setItemDelegateForColumn(3, self.delegate)
		# signal to get data from row/col
		self.ui.tableView.clicked.connect(self.index_selection)

	# caveat: only one row value can be returned at a time. for loop can be added later.
	# return the selected value from the tableview
	def index_selection(self):
		index = self.ui.tableView.selectedIndexes()
		print(index[0].row(), index[0].column())
		value = index[0].data()
		print(value)
		return value


app = QtWidgets.QApplication(sys.argv)
app.setStyle('windows')
window = TableView()
window.show()
sys.exit(app.exec_())

# https://forum.qt.io/topic/76087/get-content-of-cell-from-qtableview/6
# https://www.pythonguis.com/faq/editing-pyqt-tableview/
# https://stackoverflow.com/questions/25940413/how-to-initialize-qabstracttablemodel-with-an-empty-2d-array-while-preserving-he
# https://doc.qt.io/qt-5/qabstractitemdelegate.html
