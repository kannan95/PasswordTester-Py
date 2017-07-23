from qt5 import Ui_PassWordTester
from password_brute import main
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys
import os


class dashboard(QMainWindow, Ui_PassWordTester):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_input)

    def get_input(self):
        import re
        try:
            self.user_passwd = list(self.lineEdit.text())
            self.user_passwd_check = self.lineEdit.text()
            if not self.user_passwd:
                self.error_dialog = QtWidgets.QErrorMessage()
                self.error_dialog.showMessage('Please give some input!!')
            elif not re.search('^[a-z]+$', self.user_passwd_check):
                self.error_dialog_2 = QtWidgets.QErrorMessage()
                self.error_dialog_2.showMessage(
                    'Please enter lower case character only!')
            self.length = len(self.user_passwd)
            self.time_taken, self.count = main(self.length, self.user_passwd)
            self.label_3.setAlignment(Qt.AlignCenter)
            self.label_3.setText("The password \"{0}\" took {1:5f}secs to crack \n It took {2} guesses!!!".format(
                self.user_passwd_check, self.time_taken, self.count))
            self.label_3.setScaledContents(True)

        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = dashboard()
    game.show()
    app.exec_()
