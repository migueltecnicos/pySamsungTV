import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MyWindowClass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindowClass()
    w.show()
    sys.exit(app.exec_())

