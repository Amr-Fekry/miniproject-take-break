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
		# A) gb
		self.gb = QtWidgets.QGroupBox("Type of alert")
		self.gb.setFixedSize(500, 100)
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
		
		# add widgets to layout
		self.layout.addWidget(self.gb)



def main():
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()