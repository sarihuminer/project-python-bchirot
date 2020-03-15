from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from pathlib import Path

from PySide2.QtCore import SIGNAL, QObject
from gover_ui import Ui_MainWindow
import db
import copy
from PyQt5 import QtGui

#from PyQt5.QtGui import *

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
        widget = QtGui.QWidget(self)
        self.setCentralWidget(widget)
        grid = QtGui.QGridLayout()
        for p in allParty:
            self.newbutton = copy.deepcopy(self.ui.pushButton)
            self.newbutton.setText(p.name)
            # self.ui.pushButton.clicked.connect(self.choose_party)
            self.widget.add
            # Cannot resize or maximize
            # self.setFixedSize(1045, 770)

            # Add button test
            # self.dateLabel = Ui_MainWindow.QLabel("Test")
            # self.pushButton = Ui_MainWindow.QPushButton('Test button')


            grid.addWidget(self.newbutton, 0, 0)
            # grid.addWidget(self.pushButton, 0, 1)


            self.pushButton.clicked.connect(self.closeEvent)
            # self.ui.p.name = newbutton
            #self.layout(self.newbutton)
        self.widget.setLayout(grid)
        # defa save_All(self):
    # self.ui.btnsave.clicked.connect(self.save_All)

    def choose_party(self):
        prti = self.ui.pushButton.text()
        count = db.cursor.execute('select countVoters from party where char==' + prti)
        if (count > 0):
            print(count)
        count = count + 1
        db.cursor.execute('update party set countVoters+=1 where char==' + prti)
        count = db.cursor.execute('select countVoters from party where char==' + prti)
        print('after update {}'.format(count))
        print(prti)
        # saveto db the selection.....





#        self.select_speed = self.ui.comboBoxSpeed.currentText()
#  c.Car(self.selection_color, self.select_speed)
# self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = selctionn()
    w.show()
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
