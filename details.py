from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from pathlib import Path
import sqlite3
from PySide2.QtCore import SIGNAL, QObject
from details_p_ui import Ui_Form
import db
import copy
# from PyQt5 import QtGui
from PySide2.QtWidgets import QApplication, QPushButton
from try_code import Test
from PySide2 import QtGui
# from PyQt5.QtGui import *
import db


# from try_code import *


class selctionn(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit_id.setText('315013565')
        self.ui.lineEdit_fn.setText('שרה')
        self.ui.lineEdit_ln.setText('שטרן')
        self.ui.lineEdit_nh.setText('68')
        self.ui.lineEdit_c.setText('בני ברק')
        self.ui.lineEdit_s.setText('רבי עקיבא')
        self.ui.pushButton.clicked.connect(self.check_if_exsist)

    def convert_to_bool(v):
        return str(v).lower() in ("yes", "true", "t", "1")

    def check_if_exsist(self):
        staus = db.cursor.execute(
            "select status from Persons where id=? and first_name=? and last_name=? and num_house=? and street=? and city=? ",
            self.ui.lineEdit_id.text(),
            self.ui.lineEdit_fn.text(),
            self.ui.lineEdit_ln.text(),
            self.ui.lineEdit_nh.text(),
            self.ui.lineEdit_s.text(),
            self.ui.lineEdit_c.text(),
        ).fetchall()
        print(staus)
        # for w in s:
        #    print(w)
        # s = self.convert_to_bool(status)
        w.hide()
        if db.cursor.rowcount == 0:
            return
        if (staus[0][0] == False):
            db.cursor.execute(
                "update Persons set status=? where id=?  ", True, self.ui.lineEdit_id.text())
            db.conn.commit()
            t = Test()
            t.light_palette_ui(w)
        else:
            print("שקרן-הצביע כבר!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = selctionn()
    w.show()

    app.exec_()
