import configparser


class AtxConfig:
    def __init__(self, path='config/atx.ini'):
        self.cfg = configparser.ConfigParser()
        if not self.cfg.read(path):
            raise Exception("config file {} is not unreadable.".format(path))

    def get_log_path(self):
        return self.cfg.get('log', 'path')

    def get_log_config(self):
        return self.cfg.get('log', 'config')

