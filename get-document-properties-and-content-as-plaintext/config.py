from configparser import ConfigParser

config_relative_filepath = 'config.ini'
config = ConfigParser()
config.read(config_relative_filepath)

class Config(object):
  def __init__(self):
    self.panviva = config['panviva']
