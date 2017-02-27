import os

class Config():

    uart_port = 'COM1'
    uart_baud = 115200

    db_name = 'test.db'
    db_path = os.path.join(os.getcwd(), 'data', db_name)

    @classmethod
    def init_app(cls):
        pass

class DevelopmentConfig(Config):

    db_name = 'dev.db'
    db_path = os.path.join(os.getcwd(), 'data', db_name)

    @classmethod
    def init_app(self):
        Config.init_app()

class ProductionConfig(Config):

    @classmethod
    def init_app(self):
        Config.init_app()

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}