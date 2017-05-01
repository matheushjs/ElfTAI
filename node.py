class Title:
    """This class will represent a single Title, and handle Title-specific queries.
    Inner data: [Name, Aliases, Comment, Strings]"""
    def __init__(self):
        self.name = None
        self.alias = set([])
        self.comment = ""
        self.ids = []
