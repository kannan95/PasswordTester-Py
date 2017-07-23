# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brute.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PassWordTester(object):
    def setupUi(self, PassWordTester):
        PassWordTester.setObjectName("PassWordTester")
        PassWordTester.setEnabled(True)
        PassWordTester.resize(383, 236)
        PassWordTester.setMinimumSize(QtCore.QSize(383, 236))
        PassWordTester.setMaximumSize(QtCore.QSize(383, 236))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PassWordTester.setWindowIcon(icon)
        PassWordTester.setStyleSheet("background-image: url(:/Icons/Icons/image.jpg);\n"
"color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(PassWordTester)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("background-color: rgb(153, 255, 142);\n"
"color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"selection-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu\";\n"
"alternate-background-color: rgb(184, 255, 202);\n"
"color: rgb(158, 255, 241);\n"
"background-color: rgb(155, 255, 187);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 57 italic 12pt \"Ubuntu\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(210, 247, 255);")
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.raise_()
        self.pushButton.raise_()
        PassWordTester.setCentralWidget(self.centralwidget)

        self.retranslateUi(PassWordTester)
        QtCore.QMetaObject.connectSlotsByName(PassWordTester)

    def retranslateUi(self, PassWordTester):
        _translate = QtCore.QCoreApplication.translate
        PassWordTester.setWindowTitle(_translate("PassWordTester", "PasswordTester"))
        self.label.setText(_translate("PassWordTester", "Enter the password"))
        self.lineEdit.setToolTip(_translate("PassWordTester", "<html><head/><body><p><span style=\" font-style:italic;\">Please enter lower case charcters!</span></p></body></html>"))
        self.pushButton.setText(_translate("PassWordTester", "Brute!"))

import Background_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PassWordTester = QtWidgets.QMainWindow()
    ui = Ui_PassWordTester()
    ui.setupUi(PassWordTester)
    PassWordTester.show()
    sys.exit(app.exec_())

