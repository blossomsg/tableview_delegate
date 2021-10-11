from ui.table_view_delgate import Ui_Form
from tablemodel import TableModel
from PyQt5 import QtWidgets
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
		self.model = TableModel(head_columns_names=self.table_col_names, head_rows_names=self.table_row_names,
								table_rows_count=5, table_columns_count=5)
		self.model.insertRow(0)  # position of the inserted row
		self.model.insertColumn(0)  # position of the inserted column
		self.ui.tableView.setModel(self.model)


app = QtWidgets.QApplication(sys.argv)
app.setStyle('windows')
window = TableView()
window.show()
sys.exit(app.exec_())

# https://www.pythonguis.com/faq/editing-pyqt-tableview/
# https://stackoverflow.com/questions/25940413/how-to-initialize-qabstracttablemodel-with-an-empty-2d-array-while-preserving-he
