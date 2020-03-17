from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from pathlib import Path

from PySide2.QtCore import SIGNAL, QObject
from details_p_ui import Ui_Form
import db
import copy
# from PyQt5 import QtGui
from PySide2.QtWidgets import QApplication, QPushButton

from PySide2 import QtGui
# from PyQt5.QtGui import *
import db
from try_code import *


class selctionn(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.check_if_exsist)

    def check_if_exsist(self):
       # status = db.cursor.execute(
        #    'select status from Persons where id=? and first_name=? and last_name=? and num_house=? and '
        #    'street=? and city=?', self.ui.lineEdit_id, self.ui.lineEdit_fn, self.ui.lineEdit_ln,
        #    self.ui.lineEdit_nh, self.ui.lineEdit_s, self.ui.lineEdit_c)
        # if(status=='False'):
        print('yes')
        w.hide()
        t = Test()
        t.light_palette_ui(w)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = selctionn()
    w.show()

    app.exec_()
