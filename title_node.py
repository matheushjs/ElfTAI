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
