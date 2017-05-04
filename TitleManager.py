import termcolor as tc
import csv

from TitleNode import TitleNode

class TitleManager:
    """Class that will manage a list of TitleNodes. Basically does:
    1) Read a csv file, loading all Nodes in memory.
    2) Apply to the Nodes in memory whatever the user of this Object asks for.
    3) Saves the processed list of Nodes in a csv file."""
    
    def __init__(self):
        self.nodes = []

    def read_from_csv(self, path):
        """Reads all TitleNodes on a csv file, and store them internally."""
        if not isinstance(path, str):
            raise TypeError

        with open(path) as fp:
            rd = csv.reader(fp)
            while True:
                node = TitleNode().read_from_csv(rd)
                if not node: break
                self.nodes.append(node)

    def write_to_csv(self, path, bkpath=""):
        """Writes all TitleNodes to the csv file.
        If 'bkpath' is given, backup the main file before overwriting it."""
        if not isinstance(path, str):
            raise TypeError

        # Saves a backup before overwriting the main file.
        if bkpath != "":
            with open(path, 'r') as infile, open(bkpath, 'w') as outfile:
                outfile.write(infile.read())

        with open(path, 'w') as fp:
            wr = csv.writer(fp)
            for node in self.nodes:
                node.write_to_csv(wr)


if __name__ == "__main__":
    tm = TitleManager()
    tm.read_from_csv("test.csv")
    tm.write_to_csv("test_out.csv")
