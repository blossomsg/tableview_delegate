from ui.table_view_delgate import Ui_Form
from PyQt5 import QtWidgets
import sys


class TableView(QtWidgets.QWidget):
	"""
	Tableview to test the delegates for multiple rows and columns
	"""

	def __init__(self):
		super(TableView, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = TableView()
window.show()
sys.exit(app.exec_())
