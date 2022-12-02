import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon

from ui.ui_designer import Ui_MainWindow


class MainClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Экзамены ПДД')
        self.setWindowIcon(QIcon('icon.png'))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton.clicked.connect(self.goto_page)

    def goto_page(self):
        self.setWindowTitle('123')


app = QtWidgets.QApplication([])
application = MainClass()
application.show()

sys.exit(app.exec())
