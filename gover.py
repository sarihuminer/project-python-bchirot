from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from pathlib import Path

from PySide2.QtCore import SIGNAL, QObject
from gover_ui import Ui_MainWindow
import db
import copy
#from PyQt5 import QtGui

from PySide2.QtWidgets import QApplication, QPushButton


# from PyQt5.QtGui import *

class selctionn(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selection_color = None
        self.select_speed = None
        self.ui.pushButton.clicked.connect(self.choose_party)
        print(5)
        allParty = db.cursor.execute('select * from party ')
        for p in allParty:
            button = QPushButton("Click me")
            button.clicked.connect(self.choose_party)
            button.show()
        # widget = QtGui.QWidget(self)

    # self.setCentralWidget(widget)
    # grid = QtGui.QGridLayout()

    # self.newbutton = copy.deepcopy(self.ui.pushButton)
    # .newbutton.setText(p.name)
    # self.ui.pushButton.clicked.connect(self.choose_party)
    #            # Cannot resize or maximize
    # self.setFixedSize(1045, 770)

    # Add button test
    # self.dateLabel = Ui_MainWindow.QLabel("Test")
    # self.pushButton = Ui_MainWindow.QPushButton('Test button')

    # grid.addWidget(self.newbutton, 0, 0)
    # grid.addWidget(self.pushButton, 0, 1)

    # self.pushButton.clicked.connect(self.closeEvent)
    # self.ui.p.name = newbutton
    # self.layout(self.newbutton)
    # self.widget.setLayout(grid)
    # defa save_All(self):
    # self.ui.btnsave.clicked.connect(self.save_All)

    def choose_party(p, light_label,text1,text2,window):
        light_label.setStyleSheet("background-color: yellow ;color: blue; border-style: outset;height:100")
        text1.setStyleSheet("color:black;font-weigth:bold; ;font-size:16px")
        text2.setStyleSheet("color:black;font-weigth:bold; ;font-size:12px")
        c = p.char
        n = p.name
        # count = db.cursor.execute(
        #   "select countvoters from [bchirot].[dbo].[Party] where charParty='ג'").fetchone()[0]
        count = db.cursor.execute(
            "select countvoters from [bchirot].[dbo].[Party] where charParty=? and nameParty=?", p.char,
            p.name).fetchone()[0]
        if (count > 0):
            print(count)
        count = count + 1
        db.cursor.execute(
            "update [dbo].[Party] set [countVoters]=[countVoters]+1 where [nameParty]=? and [charParty]=? ",
            p.name, p.char)
        db.conn.commit()
        count = db.cursor.execute(
            'select countVoters from [bchirot].[dbo].[Party] where charParty=? and nameParty=?', p.char,
            p.name).fetchone()[0]
        print('after update {}'.format(count))
        print(p.name)


        reply = QMessageBox.question(window, 'להמשיך?',
                                     'האם אתה בטוח בבחירתך?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
        # do something if yes
        #else:

            window.close()
    #        self.select_speed = self.ui.comboBoxSpeed.currentText()
    #  c.Car(self.selection_color, self.select_speed)
    # self.hide()
    def creatButtons(self):
        allParty = db.cursor.execute('select * from party ')
        for p in allParty:
            button = QPushButton("Click me")
            button.clicked.connect(self.choose_party)
            button.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = selctionn()
    w.show()
    w.creatButtons()

    app.exec_()
    # app = QApplication(sys.argv)
    # MainWindow =QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

# app = QApplication(sys.argv)
# w = selctionn()
# w.show()
# app.exec_()