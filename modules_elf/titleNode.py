import csv

from .namedEntity import NamedEntity
from .comment import Comment

class TitleNode(NamedEntity):
    """This class will represent a single Title, and handle Title-specific queries.
    
    Each Title contains:
        1) Title & Aliases (inherited from NamedEntity)
        2) Comment
        3) Items
        
    No string treatment is done in this class.
    String comparisons are done case-insentively, though.
    
    Exceptions:
        TypeError - When any argument received has invalid type.
                    Most arguments are expected to be strings.
                    Even list of strings are type-checked.
        ValueError - When a value given as argument is ignored for any reason,
                     forcing the function not to do what its name suggests.
                     Happens when trying to add an alias that already exists, for example."""

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
        Raises:
            ValueError - Item already existed"""
        if not isinstance(item, str):
            raise TypeError
        if self.has_item(item) >= 0:
            raise ValueError
        self.items.append(item)

    def rm_item(self, item):
        """Removes an item from this Node.
        Searching for 'item' is done case-insensitively.
        Raise:
            ValueError - Item does not exist within this node, thus could not be removed."""
        if not isinstance(item, str):
            raise TypeError
        idx = self.has_item(item)
        if idx < 0:
            raise ValueError
        self.items.pop(idx)

    def get_items(self, howmany=-1):
        """Returns a list with the last 'howmany' items added to this Node.
        If 'howmany' is negative, returns all items.
        If 'howmany' is higher than the number of items, returns all of them."""
        if howmany < 0:
            return [i for i in self.items]
        else:
            return [i for i in self.items[-howmany:]]

    def write_to_csv(self, writer):
        """Appends this Node to the csv file.
        The format is as described in README.md:
            [title],[alias1],[alias2],...
            [comment1],[comment2],[comment3],...
            [item1],[item2],..."""
        if not isinstance(writer, csv.writer):
            raise TypeError

        title_row = [self.get_title(),]
        title_row.extend(self.get_alias())
        writer.writerows([title_row, self.comment.get_list(), self.items])

    def read_from_csv(self, reader):
        """Reads a Node from a csv file, overwriting the current Node instance.
        Returns self. 
        Raises:
            ValueError - if node could not be read from 'reader'."""
        if not isinstance(reader, csv.reader):
            raise TypeError

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
            raise ValueError
