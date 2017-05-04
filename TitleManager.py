import sys
from os import path

from TitleNode import TitleNode

# User can change the database filenames here.
# Name should be set only when starting a new database.
_global_name='database'

class TitleManager:
    """Class that will manage a list of TitleNodes"""
    
    _csvfile = path.join(sys.path[0], _global_name + '.csv')
    _bkfile = path.join(sys.path[0], _global_name + 'csv.bk')

    def __init__(self):
        self.nodes = []


if __name__ == "__main__":
    tm = TitleManager()
    print(tm._csvfile)
