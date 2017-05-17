import csv

from .namedEntity import NamedEntity
from .comment import Comment

# Lowercasing should be done in this class, when it is essential (adding aliases, comparison functions)
# Any other String treatment is up to the user

class TitleNode (NamedEntity):
    """This class will represent a single Title, and handle Title-specific queries.
    
    Each Title contains:
        1) Title & Aliases (inherited from NamedEntity)
        2) Comment
        3) Items
        
    No string treatment is done in this class.
    String comparisons are done case-insentively, though."""

    def __init__(self, title="Null"):
        super(TitleNode, self).__init__(title)
        self.comment = Comment()
        self.items = []

    def get_comment(self):
        """Returns the Comment object in this Node."""
        return self.comment

    def has_item(self, item):
        """Checks if this Node contains 'item'.
        Comparisons between strings are case-insensitive.
        Returns:
            the index of the item, if it exists.
            -1 otherwise."""
        if not isinstance(item, str):
            raise TypeError
        temp = [i.lower() for i in self.items]
        if item.lower() in temp:
            return temp.index(item.lower())
        else:
            return -1

    def add_item(self, item):
        """Adds a unique item to this Node.
        Comparisons between strings are not case-sensitive.
        Returns
            False if item already existed
            True otherwise."""
        if not isinstance(item, str):
            raise TypeError
        if self.has_item(item) >= 0:
            return False
        else:
            self.items.append(item)
            return True

    def rm_item(self, item):
        """Removes an item from this Node.
        Searching for 'item' is done case-insensitively.
        Returns True if item existed and was removed"""
        if not isinstance(item, str):
            raise TypeError
        idx = self.has_item(item)
        if idx < 0:
            return False
        else:
            self.items.pop(idx)
            return True

    def get_items(self, howmany=-1):
        """Returns a list with the last 'howmany' items added to this Node.
        If 'howmany' is negative, returns all items.
        If 'howmany' is higher than the number of items, returns all of them."""
        if howmany < 0:
            return self.items
        else:
            return [i for i in self.items[-howmany:]]

    def write_to_csv(self, writer):
        """Appends this Node to the csv file.
        The format is as described in README.md:
            [title],[alias1],[alias2],...
            [comment1],[comment2],[comment3],...
            [item1],[item2],..."""
        title_row = [self.get_title(),]
        title_row.extend(self.get_alias())
        writer.writerows([title_row, self.comment.get_list(), self.items])

    def read_from_csv(self, reader):
        """Reads a Node from a csv file, overwriting the current Node instance.
        Returns self if reading was successful. None if end-of-file was reached"""
        try:
            l = next(reader)
            self.set_title(l[0])
            for i in range(1, len(l)):
                self.alias.add(l[i])

            l = next(reader)
            if l:
                self.comment.add(l)
            
            l = next(reader)
            self.items = [i for i in l]
            return self
        except StopIteration:
            return None
