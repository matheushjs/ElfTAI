import termcolor as tc
import csv

from TitleNode import TitleNode

# String stripping and trimming is done here.

class TitleManager:
    """Class that will manage a list of TitleNodes. Basically is supposed to do:
        1) Read a csv file, loading all Nodes in memory.
        2) Apply operations upon the list of Nodes.
        3) Saves the processed list of Nodes in a csv file."""
    
    def __init__(self, filename, bkfile=None):
        # nodes: list of existent nodes
        # filename: name of file from which to read all nodes
        # bkfile: name of file to which backup all nodes
        self.nodes = []
        self.filename = filename
        self.bkfile = bkfile
        self.read_from_csv(filename)

    def __enter__(self):
        # For use in 'with' statements
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # For use in 'with' statements
        self.finalize()

    def finalize(self):
        """If this TitleManager was given a name for a backup file upon instantiation, \
transfer contents of the old Nodes csv file to this backup.
        Then saves all nodes in the Nodes csv file, overwriting it."""
        if self.bkfile:
            self.write_to_csv(self.filename, self.bkfile)
        else:
            self.write_to_csv(self.filename)

    def print_summary(self):
        """Prints all nodes, each one occupying a single line.
        Information diplayed is only the Node's title and aliases."""
        for node in self.nodes:
            TitleManager._print_node_asLine(node, 40)

    def print_full(self, string=None):
        """Prints all information about nodes.
        If 'string' is given, prints full information about only the node identified by it.
        Otherwise, prints information for all nodes."""
        if string is not None:
            node = self._find_node_byName(string)
            TitleManager._print_node_asBlock(node)
        else:
            for node in self.nodes:
                TitleManager._print_node_asBlock(node)

    def add_node(self, title, aliases=None):
        """Adds a node to the list of Nodes.
        Node will have title 'title'. Make sure to get the case of this string correctly.
        If 'aliases' is given, either as a single string or a list of them, \
add them as aliases for the created Node."""
        node = self._find_node_byName(title)
        if node is not None:
            return False # Node with given title already exists
        
        node = TitleNode(title)

        if isinstance(aliases, list):
            for i in aliases:
                node.add_alias(i)
        elif isinstance(aliases, str):
            node.add_alias(i)
        else: raise TypeError

        self.nodes.append(node)
        self.nodes.sort()
        return True

    def rm_node(self, string):
        """Removes the node identified by 'string' from the list of Nodes.
        String comparison is made case-insensitively here."""
        node = self._find_node_byName(string)

        try:
            self.nodes.remove(node)
        except ValueError:
            return False
        return True

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

    def _find_node_byName(self, string):
        """Given a string, attemps to find the node with alias or title
        that is equivalent to the string. Comparison made case-insensitive and
        ignoring blank characters"""
        string = string.strip().lower()
        for node in self.nodes:
            l = []
            l.append(node.get_title().strip().lower())
            l.extend([i for i in node.get_alias()]) 
            if string in l:
                return node
        return None

    @staticmethod
    def _print_node_asLine(node, width=-1):
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
    def _print_node_asBlock(node, length=-1):
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
        tm._print_node_asBlock(tm._find_node_byName("math"))
        print(tm.add_node("Information", ["info", "inf"]))
