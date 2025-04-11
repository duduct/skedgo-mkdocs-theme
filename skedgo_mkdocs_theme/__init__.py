from os.path import dirname, abspath, join

def get_path():
    return abspath(dirname(__file__))

def get_theme_dir():
    return join(get_path(), 'templates')