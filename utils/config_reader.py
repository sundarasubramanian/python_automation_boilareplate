import configparser


def read_config(path='config.ini'):
    config = configparser.ConfigParser()
    config.read(path)
    return config['DEFAULT']
