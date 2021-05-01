from samsungtvws import SamsungTVWS
import wakeonlan

class TV:
    def __init__(self, ip):
        self.ip = ip
        self.port = 8002
        self.token_file = 'tv-token.txt'
        self.tv = None

    def conectar(self):
        self.tv = SamsungTVWS(host=self.ip, port=self.port, token_file=self.token_file)
        #self.tv.shortcuts().

    def subir_volumen(self):
        self.tv.shortcuts().volume_up()

    def bajar_volumen(self):
        self.tv.shortcuts().volume_down()

    def mute(self):
        self.tv.shortcuts().mute()

    def open(self):
        self.tv.open()

    def apagar(self):
        self.tv.shortcuts().power()

    def encender(self):
        wakeonlan.send_magic_packet('bc:7e:8b:56:dd:68')

