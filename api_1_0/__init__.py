import json
import htmlPy

from config import config
from .uart import Uart
from .database import Database

class API(htmlPy.Object):

    # init varables
    def __init__(self, app, mode='default'):
        super(API, self).__init__()
        self.app = app
        self.uart = Uart(port=config[mode].uart_port, baud=config[mode].uart_baud)
        self.db = Database(dbpath=config[mode].db_path)

    @htmlPy.Slot()
    def say_hello_world(self):
        self.app.html = u"Hello World"
