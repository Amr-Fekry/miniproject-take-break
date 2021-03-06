import sys, time, webbrowser, os, subprocess
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import threading

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Take a break")
		self.setWindowIcon(QtGui.QIcon("logo.png"))
		# add a hidden status bar with a reference
		self.status = self.statusBar()
		self.status.hide()

		self.initUI()

	#_______________________________________VIEWS______________________________________

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
		self.entry1.setPlaceholderText("Select link type first ->")
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
		self.entry2.setPlaceholderText("Add a number here then select time unit ->")
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
		self.start_btn.setStyleSheet("QPushButton { background-color: Green }")
		self.start_btn.clicked.connect(self.start_timer)
		# J) stop_btn
		self.stop_btn = QtWidgets.QPushButton("Stop Timer")
		self.stop_btn.setFixedSize(140, 30)
		self.stop_btn.setStyleSheet("QPushButton { background-color: Red }")
		self.stop_btn.clicked.connect(self.stop_timer)
		# add widgets to layout
		self.layout.addWidget(self.gb)
		self.layout.addWidget(self.gb2)
		self.layout.addWidget(self.start_btn, False, QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.stop_btn, False, QtCore.Qt.AlignCenter)
		# hide stop_btn
		self.stop_btn.hide()

	#_______________________________________METHODS______________________________________

	def alert_choice_activated(self, text):
		if text == "Local File (Song\\Video)":
			path, var2 = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a File")
			self.entry1.setText(path)
			self.link_type = "Local"
		if text == "External Link (Youtube)":
			self.entry1.clear()
			self.entry1.setPlaceholderText("PUT THE LINK HERE")
			self.link_type = "External"

	def time_choice_activated(self, text):
		self.time_unit = text

	def start_timer(self):
		# get the link entry
		self.link_entry = self.entry1.text()
		# get the time entry
		self.time_entry = self.entry2.text()
		# check if entries are valid
		if self.valid_inputs():
			# show status bar with the start time
			self.status.show()
			self.status.showMessage("Started at " + time.ctime()[11:19])
			# hide start_btn and show stop_btn
			self.start_btn.hide()
			self.stop_btn.show()
			# convert time entry to seconds if needed
			self.time_in_seconds = self.convert_to_seconds(int(self.time_entry))
			# start a timer in a new thread
			self.thread = threading.Timer(self.time_in_seconds, self.start_thread)
			self.thread.start()

	# helper for start_timer()
	def valid_inputs(self):
		# link type selected
		try: self.link_type
		except:
			QtWidgets.QMessageBox.warning(self, "Warning", "No alert type selected!")
			return False
		# link is valid
		if self.link_type == "Local":
			if not os.path.exists(self.link_entry):
				QtWidgets.QMessageBox.warning(self, "Warning", "Path to local file is not valid!")
				return False
		elif self.link_type == "External":
			if "http" not in self.link_entry and "www." not in self.link_entry:
				QtWidgets.QMessageBox.warning(self, "Warning", "URL is not valid!")
				return False
		# time unit selected
		try: self.time_unit
		except:
			QtWidgets.QMessageBox.warning(self, "Warning", "No time unit selected!")
			return False
		# integer value for time
		try: int(self.time_entry)
		except:	
			QtWidgets.QMessageBox.warning(self, "Warning", "Entry in duration field must be an integer!")
			return False
		return True			

	# helper for start_timer()
	def convert_to_seconds(self, time):
		if self.time_unit == "Hours":
			return time * 60 * 60
		elif self.time_unit == "Minutes":
			return time * 60
		elif self.time_unit == "Seconds":
			return time

	# called when thread is activated
	def start_thread(self):
		if self.link_type == "Local":
			# open local link in corresponding operating system type
			self.all_os_open(self.link_entry)
		elif self.link_type == "External":
			webbrowser.open(self.link_entry, 2)
		
		self.thread = threading.Timer(self.time_in_seconds, self.start_thread)
		self.thread.start()

	# helper for start_thread()
	def all_os_open(self, link):
		# https://stackoverflow.com/questions/434597/open-document-with-default-application-in-python
		if sys.platform.startswith('darwin'):
			subprocess.call(('open', link))
		elif os.name == 'nt': # For Windows
			os.startfile(link)
		elif os.name == 'posix': # For Linux, Mac, etc.
			subprocess.call(('xdg-open', link))

	def stop_timer(self):
		# add stop time to status bar
		start_time = self.status.currentMessage()
		self.status.showMessage(start_time + " | Stopped at " + time.ctime()[11:19])
		# hide start_btn and show stop_btn
		self.stop_btn.hide()
		self.start_btn.show()
		self.thread.cancel()

	#_______________________________________END______________________________________

def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()