from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from TV import TV

form_main_class = uic.loadUiType("mainwindow.ui")[0]


class MyWindowClass(QMainWindow, form_main_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        form_main_class.__init__(self)

        self.setupUi(self)

        self.tv = TV('10.0.1.64')

        self.cmd_conectar.clicked.connect(self.cmd_conectar_click)
        self.cmd_subir_volumen.clicked.connect(self.cmd_subir_volumen_click)
        self.cmd_bajar_volumen.clicked.connect(self.cmd_bajar_volumen_click)
        self.cmd_mute.clicked.connect(self.cmd_mute_click)
        self.cmd_encender.clicked.connect(self.cmd_encender_click)
        self.cmd_apagar.clicked.connect(self.cmd_apagar_click)

    def cmd_conectar_click(self):
        self.tv.conectar()

    def cmd_subir_volumen_click(self):
        self.tv.subir_volumen()

    def cmd_bajar_volumen_click(self):
        self.tv.bajar_volumen()

    def cmd_mute_click(self):
        self.tv.mute()

    def cmd_encender_click(self):
        self.tv.encender()

    def cmd_apagar_click(self):
        self.tv.apagar()