# importing libraries
from cgitb import text
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowIcon(QtGui.QIcon('Logo.png'))
    
		# setting title
		self.setWindowTitle("Paint calculator")
		# setting window geometry
		self.setGeometry(100, 100, 725, 350)
		# calling method
		self.UiComponents()
		# showing all the widgets
		self.show()
		# method for widgets
	def UiComponents(self):
		# creating a label
		self.label = QLabel(self)
		# setting geometry to the label
		self.label.setGeometry(5, 5, 710, 35)
		# creating label multi line
		self.label.setWordWrap(True)
		# setting style sheet to the label
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 1px solid black;"
								"background : white;"
								"}")
		self.setStyleSheet("background-color: gray;")

		# setting alignment to the label
		self.label.setAlignment(Qt.AlignRight)
		# setting font
		self.label.setFont(QFont('Arial', 15))
#####################################################################################################################

		# adding number button to the screen
		push1 = QPushButton("1", self)# creating a push button
		push1.setGeometry(5, 150, 80, 40)# setting geometry
		push1.setStyleSheet("QPushButton"
                             "{"
                             "background-color : white;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : grey;"
                             "}"
                             )

		push2 = QPushButton("2", self)
		push2.setGeometry(95, 150, 80, 40)

		push3 = QPushButton("3", self)
		push3.setGeometry(185, 150, 80, 40)

		push4 = QPushButton("4", self)
		push4.setGeometry(5, 200, 80, 40)

		push5 = QPushButton("5", self)
		push5.setGeometry(95, 200, 80, 40)

		push6 = QPushButton("6", self)
		push6.setGeometry(185, 200, 80, 40)

		push7 = QPushButton("7", self)
		push7.setGeometry(5, 250, 80, 40)

		push8 = QPushButton("8", self)
		push8.setGeometry(95, 250, 80, 40)

		push9 = QPushButton("9", self)
		push9.setGeometry(185, 250, 80, 40)

		push0 = QPushButton("0", self)
		push0.setGeometry(5, 300, 80, 40)

		# adding operator push button
		# creating push button
		push_equal = QPushButton("=", self) #to creat a button
		push_equal.setGeometry(275, 300, 170, 40) #to place a button (x,y,L,l)

		# adding equal button a color effect
		c_effect = QGraphicsColorizeEffect()
		c_effect.setColor(Qt.gray)
		push_equal.setGraphicsEffect(c_effect)

		push_plus = QPushButton("+", self)
		push_plus.setGeometry(275, 250, 80, 40)

		push_minus = QPushButton("-", self)
		push_minus.setGeometry(275, 200, 80, 40)

		push_mul = QPushButton("*", self)
		push_mul.setGeometry(275, 150, 80, 40)

		push_div = QPushButton("/", self)
		push_div.setGeometry(185, 300, 80, 40)

		push_parenthesis1 = QPushButton("(", self)
		push_parenthesis1.setGeometry(455, 300, 80, 40)

		push_parenthesis2 = QPushButton(")", self)
		push_parenthesis2.setGeometry(545, 300, 80, 40)

		push_percentage = QPushButton("%", self)
		push_percentage.setGeometry(635, 300, 80, 40)

		push_point = QPushButton(".", self)
		push_point.setGeometry(95, 300, 80, 40)

		push_clear = QPushButton("Clear", self)
		push_clear.setGeometry(5,45, 200, 40)
		

		push_del = QPushButton("Del", self)
		push_del.setGeometry(210, 100, 145, 40)

		#Srface Button
		push_doors1 = QPushButton("D 0.7x2.2", self)
		push_doors1.setGeometry(365, 100, 80, 40)

		push_doors2 = QPushButton("D 0.9x2.2", self)
		push_doors2.setGeometry(455, 100, 80, 40)

		push_doors3 = QPushButton("D 1.2x2.2", self)
		push_doors3.setGeometry(545, 100, 80, 40)

		push_doors4 = QPushButton("D 1.4x2.2", self)
		push_doors4.setGeometry(635, 100, 80, 40)

		push_windows1 = QPushButton("W 0.4x0.5", self)
		push_windows1.setGeometry(365, 150, 80, 40)

		push_windows2 = QPushButton("W 1x1.2", self)
		push_windows2.setGeometry(455, 150, 80, 40)

		push_windows3 = QPushButton("W 1.2x1.2", self)
		push_windows3.setGeometry(545, 150, 80, 40)

		push_windows4 = QPushButton("W 1.6x1.2", self)
		push_windows4.setGeometry(635, 150, 80, 40)

		push_door_windows1 = QPushButton("WD1.2x2.2", self)
		push_door_windows1.setGeometry(365, 200, 80, 40)

		push_door_windows2 = QPushButton("WD1.6x2.2", self)
		push_door_windows2.setGeometry(455, 200, 80, 40)

		push_door_windows3 = QPushButton("WD2.4x2.2", self)
		push_door_windows3.setGeometry(545, 200, 80, 40)

		push_door_windows4 = QPushButton("WD2.7x2.2", self)
		push_door_windows4.setGeometry(635, 200, 80, 40)

		#Price button
		push_enduit = QPushButton("Enduit", self)
		push_enduit.setGeometry(365, 250, 80, 40)

		push_peinture = QPushButton("Peinture", self)
		push_peinture.setGeometry(455, 250, 80, 40)

		push_lacquer = QPushButton("Lacquer", self)
		push_lacquer.setGeometry(545, 250, 80, 40)

		push_eau = QPushButton("A eau", self)
		push_eau.setGeometry(635, 250, 80, 40)
     
####################################################################################################################
		
        # adding action to each of the button
		push_minus.clicked.connect(self.action_minus)
		push_equal.clicked.connect(self.action_equal)
		push0.clicked.connect(self.action0)
		push1.clicked.connect(self.action1)
		push2.clicked.connect(self.action2)
		push3.clicked.connect(self.action3)
		push4.clicked.connect(self.action4)
		push5.clicked.connect(self.action5)
		push6.clicked.connect(self.action6)
		push7.clicked.connect(self.action7)
		push8.clicked.connect(self.action8)
		push9.clicked.connect(self.action9)
		push_div.clicked.connect(self.action_div)
		push_mul.clicked.connect(self.action_mul)
		push_plus.clicked.connect(self.action_plus)
		push_point.clicked.connect(self.action_point)
		push_clear.clicked.connect(self.action_clear)
		push_del.clicked.connect(self.action_del)
		push_parenthesis1.clicked.connect(self.action_parent1)
		push_parenthesis2.clicked.connect(self.action_parent2)
		push_percentage.clicked.connect(self.action_perc)
		push_doors1.clicked.connect(self.action_dr1)
		push_doors2.clicked.connect(self.action_dr2)
		push_doors3.clicked.connect(self.action_dr3)
		push_doors4.clicked.connect(self.action_dr4)
		push_windows1.clicked.connect(self.action_wn1)
		push_windows2.clicked.connect(self.action_wn2)
		push_windows3.clicked.connect(self.action_wn3)
		push_windows4.clicked.connect(self.action_wn4)
		push_door_windows1.clicked.connect(self.action_dw1)
		push_door_windows2.clicked.connect(self.action_dw2)
		push_door_windows3.clicked.connect(self.action_dw3)
		push_door_windows4.clicked.connect(self.action_dw4)
		push_enduit.clicked.connect(self.action_en)
		push_peinture.clicked.connect(self.action_pt)
		push_lacquer.clicked.connect(self.action_pt_lac)
		push_eau.clicked.connect(self.action_pt_eau)
#########################################################################################################################################""
	def action_equal(self):
		# get the label text
		equation = self.label.text()

		try:
			# getting the ans
			ans = eval(equation)
			# setting text to the label
			self.label.setText(str(ans))
		except:# setting text to the label
			self.label.setText("Wrong Input")

	def action_plus(self):# appending label text
		text = self.label.text()
		self.label.setText(text + " + ")

	def action_minus(self):# appending label text
		text = self.label.text()
		self.label.setText(text + " - ")

	def action_div(self):# appending label text
		text = self.label.text()
		self.label.setText(text + " / ")

	def action_mul(self):# appending label text
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_point(self):# appending label text
		text = self.label.text()
		self.label.setText(text + ".")
	
	def action_parent1(self):
		text=self.label.text()
		self.label.setText(text + "(")

	def action_parent2(self):
		text=self.label.text()
		self.label.setText(text + ")")

	def action_perc(self): #a revoir avec younes
		text=self.label.text()
		a=(float(text)*0.1)
		self.label.setText(str(a))

	def action0(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "9")

	def action_dr1(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "1.63")

	def action_dr2(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "2.1")

	def action_dr3(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "2.73")

	def action_dr4(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "3.2")

	def action_wn1(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "0.2")

	def action_wn2(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "1.2")

	def action_wn3(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "1.44")

	def action_wn4(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "1.92")

	def action_dw1(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "2.64")

	def action_dw2(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "3.52")

	def action_dw3(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "5.3")

	def action_dw4(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "5.94")

	def action_en(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "2500")

	def action_pt(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "3500")

	def action_pt_lac(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "4000")

	def action_pt_eau(self):# appending label text
		text = self.label.text()
		self.label.setText(text + "3000")

	def action_clear(self):# clearing the label text
		self.label.setText("")

	def action_del(self):# clearing a single digit
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])

App = QApplication(sys.argv)# create pyqt5 app
window = Window()# create the instance of our Window
sys.exit(App.exec())# start the app
