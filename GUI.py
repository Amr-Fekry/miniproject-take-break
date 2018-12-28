import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt


class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Take a break")
		self.setWindowIcon(QtGui.QIcon("logo.png"))

		self.initUI()

	#_______________________________________VIEW______________________________________

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
		self.gb.setFixedSize(530, 120)
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
		# D) alert_choice
		self.alert_choice = QtWidgets.QComboBox(self)
		self.alert_choice.addItem("Local File (Song\\Video)")
		self.alert_choice.addItem("External Link (Youtube)")
		self.alert_choice.activated[str].connect(self.alert_choice_activated)
		self.alert_choice.setMinimumSize(100, 30)
		self.alert_choice.setStyleSheet("QComboBox { background-color: green }")
		# add C, D to B
		self.gb_layout.addWidget(self.entry1, False, QtCore.Qt.AlignLeft) # (widget, stretch, alignment)
		self.gb_layout.addWidget(self.alert_choice, False, QtCore.Qt.AlignLeft)
		# add widgets to layout
		self.layout.addWidget(self.gb)

		#_______________________________________METHODS______________________________________

	def alert_choice_activated(self, text):
		if text == "Local File (Song\\Video)":
			path, var2 = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a File")
			self.entry1.setText(path)
		if text == "External Link (Youtube)":
			self.entry1.clear()
			self.entry1.setPlaceholderText("PUT THE LINK HERE")



def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()