from PySide2 import QtCore, QtWidgets
from functools import partial
import db
import party
import gover


class Test:
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.mainWidget = QtWidgets.QWidget()
        self.allParty_list = []
        self.allParty = db.cursor.execute('select * from party ')
        for p in self.allParty:
            self.allParty_list.append(party.Party(p[0], p[1], p[2]))
        self.window.setCentralWidget(self.mainWidget)

    def populate_lights(self):
        self.light_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        light_label = QtWidgets.QLabel("מערכת בחירות רביעיות של מדינת ישראל הדמוקרטית???")
        light_label.setStyleSheet("color: Blue;font-size:27px")
        self.light_layout.addWidget(light_label)
        for p in self.allParty_list:
            light_label = QtWidgets.QPushButton()
            light_label.setStyleSheet("background-color: blue ;color: blue; border-style: outset;height:100")
            light_label.setCheckable(True)
            text1 = QtWidgets.QLabel(p.char, light_label)
            text1.setStyleSheet("color:white;font-weigth:bold; ;font-size:16px")
            text1.setGeometry(580, 20, 120, 40)
            text2 = QtWidgets.QLabel(p.name, light_label)
            text2.setStyleSheet("color:white;font-weigth:bold; ;font-size:12px")
            text2.setGeometry(580, 60, 120, 40)
            # light_label.clicked.connect(partial(name=p.name, charp=p.char))
            # button1.clicked.connect(partial(self.on_button, 1))
            light_label.setCheckable(True)
            light_label.clicked.connect(partial(gover.selctionn.choose_party, p,light_label,text1,text2,self.window))
            self.light_layout.addWidget(light_label)
        self.light_layout.addStretch()

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


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    t = Test()
    t.light_palette_ui()
    sys.exit(app.exec_())
