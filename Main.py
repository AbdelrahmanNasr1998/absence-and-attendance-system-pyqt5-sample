import os
import sys
import mysql.connector
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QSizeGrip
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAction
import design
import G1
import G2
import B1
import B2

# ===================== Main =========================

class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.icon = "cs-icon.ico"
        self.title = "مدارس سيتي الخاصة"

        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setFixedSize(350,500)
        self.setWindowTitle(self.title)
        self.setObjectName("main_window")
        self.setStyleSheet(design.stylesheet)

        self.body()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox1)
        self.setLayout(self.vbox)
        self.show()

    def body(self):
        self.groupBox1 = QGroupBox()
        self.gridLayout1 = QGridLayout()

        self.gridLayout1.addWidget(self.Choose_Button(), 0, 0)
        self.groupBox1.setLayout(self.gridLayout1)

    def About(self):
        self.About = About()
        self.About.show()
    def Choose_G1(self):
        self.G1 = G1.g1()
        self.G1.show()
    def Choose_G2(self):
        self.G2 = G2.g2()
        self.G2.show()
    def Choose_B1(self):
        self.B1 = B1.b1()
        self.B1.show()
    def Choose_B2(self):
        self.B2 = B2.b2()
        self.B2.show()

    def Choose_Button(self):
        self.groupBox = QGroupBox("")

        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout = QGridLayout()

        self.labelimage = QLabel(self)
        self.pixmap = QPixmap("cs-header.jpg")
        self.labelimage.setPixmap(self.pixmap)
        self.gridLayout.addWidget(self.labelimage, 0, 0)

        self.button20 = QPushButton("الصف الأول الثانوي - بنات",self)

        self.button20.clicked.connect(self.Choose_G1)
        self.gridLayout.addWidget(self.button20,1,0)

        self.button21 = QPushButton("الصف الثاني الثانوي - بنات",self)
        self.button21.clicked.connect(self.Choose_G2)
        self.gridLayout.addWidget(self.button21,2,0)

        self.button22 = QPushButton("الصف الأول الثانوي - أولاد",self)
        self.button22.clicked.connect(self.Choose_B1)
        self.gridLayout.addWidget(self.button22,3,0)

        self.button23 = QPushButton("الصف الثاني الثانوي - أولاد",self)
        self.button23.clicked.connect(self.Choose_B2)
        self.gridLayout.addWidget(self.button23,4,0)

        self.button24 = QPushButton("عن البرنامج",self)
        self.button24.clicked.connect(self.About)
        self.gridLayout.addWidget(self.button24,5,0)

        self.groupBox.setLayout(self.gridLayout)
        return self.groupBox


# ==================== About =========================
class About(QWidget):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.icon = "cs-icon.ico"
        self.title = "مدارس سيتي الخاصة"
        self.top = 100
        self.left = 100
        self.width = 250
        self.height = 200

        self.initwindow()

    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setFixedSize(400,280)
        self.setWindowTitle(self.title)
        self.setStyleSheet(design.stylesheet)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.body()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox1)
        self.setLayout(self.vbox)
        self.show()

    def body(self):
        self.groupBox1 = QGroupBox()
        self.gridLayout1 = QGridLayout()

        self.gridLayout1.addWidget(self.A(), 0, 0)
        self.groupBox1.setLayout(self.gridLayout1)
    def A(self):
        self.groupBox = QGroupBox("")
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout = QGridLayout()

        self.about1 = QLabel("تم تطوير البرنامج بفكرة")
        self.about1.setFont(QtGui.QFont("sanserif",15))
        self.about1.setStyleSheet('color:white')
        self.gridLayout.addWidget(self.about1, 1, 0)

        self.about1 = QLabel("من مستر محمد عبدالعاطي")
        self.about1.setFont(QtGui.QFont("sanserif",15))
        self.about1.setStyleSheet('color:white')
        self.gridLayout.addWidget(self.about1, 2, 0)

        self.about1 = QLabel("تم تطوير البرنامج")
        self.about1.setFont(QtGui.QFont("sanserif",15))
        self.about1.setStyleSheet('color:white')
        self.gridLayout.addWidget(self.about1, 3, 0)

        self.about1 = QLabel("من طرف عبدالرحمن نصر")
        self.about1.setFont(QtGui.QFont("sanserif",15))
        self.about1.setStyleSheet('color:white')
        self.gridLayout.addWidget(self.about1, 4, 0)

        self.about1 = QLabel("2020 ©")
        self.about1.setFont(QtGui.QFont("sanserif",15))
        self.about1.setStyleSheet('color:white')
        self.gridLayout.addWidget(self.about1, 5, 0)

        self.groupBox.setLayout(self.gridLayout)
        return self.groupBox

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setLayoutDirection(Qt.RightToLeft)
    Main = Main()
    Main.show()
    sys.exit(App.exec())