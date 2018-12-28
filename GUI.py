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
		self.gb = QtWidgets.QGroupBox("Type Of Alert")
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
		self.alert_choice.setFixedSize(140, 30)
		self.alert_choice.setStyleSheet("QComboBox { background-color: blue }")
		# add C, D to B
		self.gb_layout.addWidget(self.entry1, False, QtCore.Qt.AlignLeft) # (widget, stretch, alignment)
		self.gb_layout.addWidget(self.alert_choice, False, QtCore.Qt.AlignLeft)
		# E) gb2
		self.gb2 = QtWidgets.QGroupBox("Duration Between Alerts")
		self.gb2.setFixedSize(530, 120)
		self.gb2.setStyleSheet("""QGroupBox {
								 border: 1px solid red; 
								 border-radius: 5px;
								 margin: 30px;
								 font-size: 20px;
								 color: red }

						         QGroupBox:title {
				                 subcontrol-origin: margin;
				                 subcontrol-position: top left;
				                 padding: 0 10px 0 10px }""")
		# F) gb2_layout: layout for the group box
		self.gb2_layout = QtWidgets.QHBoxLayout()
		self.gb2.setLayout(self.gb2_layout)
		# G) entry2
		self.entry2 = QtWidgets.QLineEdit()
		self.entry2.setMinimumSize(300, 30) 
		self.entry2.setStyleSheet("QLineEdit {background-color: white}")
		# H) alert_choice
		self.time_choice = QtWidgets.QComboBox(self)
		self.time_choice.addItem("Hours")
		self.time_choice.addItem("Minutes")
		self.time_choice.addItem("Seconds")
		self.time_choice.activated[str].connect(self.time_choice_activated)
		self.time_choice.setFixedSize(140, 30)
		self.time_choice.setStyleSheet("QComboBox { background-color: Blue }")
		# add G, H to F
		self.gb2_layout.addWidget(self.entry2, False, QtCore.Qt.AlignLeft) # (widget, stretch, alignment)
		self.gb2_layout.addWidget(self.time_choice, False, QtCore.Qt.AlignLeft)
		# I) start_btn
		self.start_btn = QtWidgets.QPushButton("Start Timer")
		self.start_btn.setFixedSize(140, 30)
		self.start_btn.setStyleSheet("QPushButton { background-color: Red }")
		self.start_btn.clicked.connect(self.start_timer)
		# add widgets to layout
		self.layout.addWidget(self.gb)
		self.layout.addWidget(self.gb2)
		self.layout.addWidget(self.start_btn, False, QtCore.Qt.AlignCenter)

		#_______________________________________METHODS______________________________________

	def alert_choice_activated(self, text):
		if text == "Local File (Song\\Video)":
			path, var2 = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a File")
			self.entry1.setText(path)
		elif text == "External Link (Youtube)":
			self.entry1.clear()
			self.entry1.setPlaceholderText("PUT THE LINK HERE")

	def time_choice_activated(self, text):
		self.time_unit = text

	def start_timer(self):
		pass


def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()