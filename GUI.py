import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Take a break")
		self.setWindowIcon(QtGui.QIcon("logo.png"))

		self.initUI()

	def initUI(self):
		# create a widget for the page and give it a layout
		self.page = QtWidgets.QWidget()
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignCenter)
		self.page.setLayout(self.layout)
		# set it as central widget
		self.setCentralWidget(self.page)
		# give the page a lightgray background
		self.page.setStyleSheet("QWidget {background-color: lightgray}")
		# create widgets
		# A) gb: groupbox
		self.gb = QtWidgets.QGroupBox("Type of alert")
		self.gb.setFixedSize(500, 120)
		self.gb.setStyleSheet("""QGroupBox {
								 border: 1px solid red; 
								 border-radius: 5px;
								 margin: 30px;
								 font-size: 20px;
								 color: red }

						         QGroupBox:title {
				                 subcontrol-origin: margin;
				                 subcontrol-position: top left;
				                 padding: 0 10px 0 10px }""")
		# B) gb_layout: layout for the group box
		self.gb_layout = QtWidgets.QHBoxLayout()
		self.gb.setLayout(self.gb_layout)
		# C) entry1
		self.entry1 = QtWidgets.QLineEdit()
		self.entry1.setMinimumSize(300, 30) 
		self.entry1.setStyleSheet("QLineEdit {background-color: white}")
		# add C to B
		self.gb_layout.addWidget(self.entry1, 0, QtCore.Qt.AlignLeft)


		# add widgets to layout
		self.layout.addWidget(self.gb)



def main():
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()