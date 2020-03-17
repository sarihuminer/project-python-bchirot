import sys
import party
import random
import db
from PySide2 import QtCore, QtWidgets, QtGui



class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.allParty_list=[]
        self.allParty = db.cursor.execute('select * from party ')
        for p in self.allParty:
            self.allParty_list.append(party.Party(p[0],p[1],p[2]))
        self.layout = QtWidgets.QVBoxLayout()

        for p in self.allParty_list:
            self.button = QtWidgets.QPushButton(p.char+' \n '+p.name)
            self.button.setStyleSheet("background-color: Blue ;color: white; border-style: outset;height:100;width:100")
           # self.text = QtWidgets.QLabel("Hello World")
            #self.text.setAlignment(QtCore.Qt.AlignCenter)
     #       self.layout.addWidget(self.text)
            self.layout.addWidget(self.button)
            self.button.clicked.connect(self.magic)

        self.setLayout(self.layout)
    def light_palette_ui(self):
        self.vertical_layout_main = QtWidgets.QVBoxLayout(self.mainWidget)
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.vertical_layout_main.addWidget(self.scroll)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll_widget = QtWidgets.QWidget()
        self.scroll.setWidget(self.scroll_widget)

        self.populate_lights()
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.window.show()

    def magic(self):

        self.button.setText(random.choice(self.hello))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)



    widget = MyWidget()
    widget.light_palette_ui()
    widget.show()



    sys.exit(app.exec_())