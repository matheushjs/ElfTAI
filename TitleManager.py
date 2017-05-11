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

    def print_full(self, string=None):
        """Prints all information about nodes.
        If 'string' is given, prints only the node identified by it."""
        if string is not None:
            node = self.find_node_byName(string)
            TitleManager.print_node_asBlock(node)
        else:
            for node in self.nodes:
                TitleManager.print_node_asBlock(node)

    def find_node_byName(self, string):
        """Given a string, attemps to find the node with alias or title
        that is equivalent to the string. Comparison made case-insensitive and
        ignoring blank characters"""
        string = string.strip().lower()
        for node in self.nodes:
            l = []
            l.append(node.get_title().strip().lower())
            l.extend([i.strip().lower() for i in node.get_alias()]) 
            if string in l:
                return node
        return None

    def add_node(self, string, aliases=None):
        #Don't forget to previously check existence of that node.
        pass

    def rm_node(self, string):
        pass

    def add_alias(self, string, alias):
        pass

    def rm_alias(self, alias):
        pass

    def set_comment(self, comm):
        pass

    def add_comment(self, comm):
        #Consider making it possible to add multiple comments, as in a csv
        #Or just append... but that's shitty
        #If we did as suggested above, comments could be indexed and removed by index
        pass

    def erase_comment(self, comm):
        pass
    
    def add_item(self, item):
        pass

    def rm_item(self, item):
        pass

    def find_item(self, item):
        #return a list of nodes that contain item
        pass

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

    @staticmethod
    def print_node_asBlock(node, length=-1):
        """Prints a TitleNode as a block, with all information wanted"""
        title = node.get_title()
        alias = node.get_alias()
        comm = node.get_comment()
        items = node.get_items(length)

        print(
            tc.colored("{name} - '{comment}'".format(
                name = title,
                comment = comm
            ),
            'magenta',
            attrs=['bold'])
        )

        if len(items) == 0:
            print(tc.colored("Empty", 'white', attrs=['bold', 'dark']))
        else:
            print(tc.colored(', '.join([ str(i) for i in items]), 'white', attrs=['bold', 'dark']))


if __name__ == "__main__":
    with TitleManager("test.csv", "test_out.csv") as tm:
        tm.print_summary()
        tm.print_full()
        tm.print_node_asBlock(tm.find_node_byName("math"))
