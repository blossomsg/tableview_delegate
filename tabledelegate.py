from PyQt5 import QtWidgets
from PyQt5 import QtCore


class TableDelegate(QtWidgets.QStyledItemDelegate):
	def __init__(self):
		super(TableDelegate, self).__init__()

	def createEditor(self, parent, option, index):
		editor = QtWidgets.QSpinBox(parent)
		editor.setMinimum(0)
		editor.setMaximum(100)
		return editor

	def setEditorData(self, editor, index):
		value = index.model().data(index, QtCore.Qt.EditRole)
		editor.setValue(int(value))

	def setModelData(self, editor, model, index):
		editor.interpretText()
		value = editor.value()
		model.setData(index, value, QtCore.Qt.EditRole)

	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)


# https://stackoverflow.com/questions/30615090/pyqt-using-qtextedit-as-editor-in-a-qstyleditemdelegate?rq=1
# https://doc.qt.io/qt-5/qtwidgets-itemviews-spinboxdelegate-example.html
