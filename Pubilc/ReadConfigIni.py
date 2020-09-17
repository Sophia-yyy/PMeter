import configparser


class ReadConfigIni():
    """
    实例化configparser
    """

    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfigValue(self, config, name):
        value = self.cf.get(config, name)
        return value
