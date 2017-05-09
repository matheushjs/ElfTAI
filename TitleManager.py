import termcolor as tc
import csv

from TitleNode import TitleNode

class TitleManager:
    """Class that will manage a list of TitleNodes. Basically does:
    1) Read a csv file, loading all Nodes in memory.
    2) Apply to the Nodes in memory whatever the user of this Object asks for.
    3) Saves the processed list of Nodes in a csv file."""
    
    def __init__(self, filename, bkfile=None):
        """
        nodes: list of existent nodes
        filename: name of file from which to read all nodes
        bkfile: name of file to which backup all nodes"""

        self.nodes = []
        self.filename = filename
        self.bkfile = bkfile
        self.read_from_csv(filename)

    def __enter__(self):
        """For use in 'with' statements"""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """For use in 'with' statements"""
        self.finalize()

    def finalize(self):
        """Makes a backup and saves all nodes"""
        if self.bkfile:
            self.write_to_csv(self.filename, self.bkfile)
        else:
            self.write_to_csv(self.filename)

    def print_summary(self):
        """Prints nodes, one per line, colored"""
        for node in self.nodes:
            TitleManager.print_node_asLine(node, 40)

    def read_from_csv(self, path):
        """Reads all TitleNodes on a csv file, and store them internally."""
        if not isinstance(path, str):
            raise TypeError

        with open(path) as fp:
            rd = csv.reader(fp)
            while True:
                node = TitleNode().read_from_csv(rd)
                if not node: break #read failed
                self.nodes.append(node)

    def write_to_csv(self, path, bkpath=None):
        """Writes all TitleNodes to the csv file.
        If 'bkpath' is given, backup the main file before overwriting it."""
        if not isinstance(path, str):
            raise TypeError

        # Saves a backup before overwriting the main file.
        if bkpath:
            with open(path, 'r') as infile, open(bkpath, 'w') as outfile:
                outfile.write(infile.read())

        with open(path, 'w') as fp:
            wr = csv.writer(fp)
            for node in self.nodes:
                node.write_to_csv(wr)

    @staticmethod
    def print_node_asLine(node, width=-1):
        """Prints a TitleNode in a line, with colors"""
        if not isinstance(node, TitleNode):
            raise TypeError

        title = node.get_title()
        alias = node.get_alias()
        if width == -1:
            width = 0

        print("{name} ({alias})".format(
                name=tc.colored(title.center(width), 'cyan', attrs=['bold', 'dark']),
                alias=tc.colored(','.join(alias), color='yellow')
            )
        )

if __name__ == "__main__":
    with TitleManager("test.csv", "test_out.csv") as tm:
        tm.print_summary()
