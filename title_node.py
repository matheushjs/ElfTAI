import sys
import csv

def die(string):
    print(string)
    sys.exit(1)

class TitleNode:
    """This class will represent a single Title, and handle Title-specific queries.
    Inner data: [Title, Aliases, Comment, Strings]"""
    def __init__(self, title):
        self.title = title
        self.alias = set([])
        self.comment = ""
        self.strings = []

    # TitleNodes will be compared by their titles.
    def __eq__(self,other): return self.title.lower() == other.title.lower()
    def __ne__(self,other): return self.title.lower() != other.title.lower()
    def __lt__(self,other): return self.title.lower() < other.title.lower()
    def __le__(self,other): return self.title.lower() <= other.title.lower()
    def __gt__(self,other): return self.title.lower() > other.title.lower()
    def __ge__(self,other): return self.title.lower() >= other.title.lower()

    def add_alias(self, alias):
        pass

    def rm_alias(self, alias):
        pass

    def has_alias(self, alias):
        pass

    def set_comment(self, comment):
        pass

    def add_string(self, string):
        pass

    def has_string(self, string):
        pass

    def rm_string(self, string):
        pass

    def write_to_csv(self, writer):
        pass

    def read_from_csv(self, reader):
        pass
