from ui.table_view_delgate import Ui_Form
from tablemodel import TableModel
from PyQt5 import QtWidgets
from PyQt5 import QtGui
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
		self.table_col_names = [col for col in config.keys()]
		self.table_row_names = [row for row in range(5)]
		self.empty = [["", ""], ["", ""]]
		self.model = TableModel(self.table_col_names, self.table_row_names, self.empty)
		self.ui.tableView.setModel(self.model)


app = QtWidgets.QApplication(sys.argv)
app.setStyle('windows')
window = TableView()
window.show()
sys.exit(app.exec_())

# https://www.pythonguis.com/faq/editing-pyqt-tableview/
# https://stackoverflow.com/questions/25940413/how-to-initialize-qabstracttablemodel-with-an-empty-2d-array-while-preserving-he
