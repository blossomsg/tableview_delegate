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
		self.table_col_names = [col for col in config.keys()]
		self.model = TableModel(self.table_col_names)
		self.ui.tableView.setModel(self.model)
		self.horizontalHeader = self.ui.tableView.horizontalHeader()
		self.horizontalHeader.setVisible(True)


app = QtWidgets.QApplication(sys.argv)
window = TableView()
window.show()
sys.exit(app.exec_())
