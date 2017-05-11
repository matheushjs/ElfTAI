import csv

# Lowercasing should be done in this class, when it is essential (adding aliases, comparison functions)
# Any other String treatment is up to the user

class TitleNode:
    """This class will represent a single Title, and handle Title-specific queries.
    
    Each Title contains:
        1) Title
        2) Aliases
        3) Comment
        4) Items
        
    No string treatment is done in this class.
    String comparisons are done case-insentively, though."""

    def __init__(self, title="Null"):
        self.title = title
        self.alias = set([])
        self.comment = ""
        self.items = []

    # TitleNodes will be compared by their titles.
    def __eq__(self,other): return self.title.lower() == other.title.lower()
    def __ne__(self,other): return self.title.lower() != other.title.lower()
    def __lt__(self,other): return self.title.lower() < other.title.lower()
    def __le__(self,other): return self.title.lower() <= other.title.lower()
    def __gt__(self,other): return self.title.lower() > other.title.lower()
    def __ge__(self,other): return self.title.lower() >= other.title.lower()

    def get_title(self):
        """Returns the Title's name."""
        return self.title

    def has_alias(self, alias):
        """Checks if this Node contains the given alias.
        Aliases are case-insentively compared."""
        if not isinstance(alias, str):
            raise TypeError
        if alias.lower() in self.alias:
            return True
        return False

    def add_alias(self, alias):
        """Adds given 'alias' as an alias to this Node.
        'alias' is converted to lowercase before adding.
        Returns False if it already existed."""
        if not isinstance(alias, str):
            raise TypeError
        if self.has_alias(alias):
            return False
        self.alias.add(alias.lower())
        return True

    def rm_alias(self, alias):
        """Removes given 'alias' from this Node.
        Alias is converted to lowercase before searching for it.
        Returns True if it existed and was successfully removed"""
        if not isinstance(alias, str):
            raise TypeError
        if not self.has_alias(alias):
            return False
        else:
            self.alias.remove(alias.lower())
            return True

    def get_alias(self):
        """Returns a list with all aliases of this Node.
        List is returned in no particular order."""
        return [i for i in self.alias]

    def set_comment(self, comment):
        """Changes current comment of this Node.
        Returns the comment that was replaced by the new one."""
        if not isinstance(comment, str):
            raise TypeError
        temp = self.comment
        self.comment = comment
        return temp

    def get_comment(self):
        """Returns the comment in this Node."""
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
            [comment]
            [item1],[item2],..."""
        title_row = [self.title,]
        title_row.extend(self.alias)
        writer.writerows([title_row, [self.comment,], self.items])

    def read_from_csv(self, reader):
        """Reads a Node from a csv file, overwriting the current Node instance.
        Returns self if reading was successful. None if end-of-file was reached"""
        try:
            l = next(reader)
            self.title = l[0]
            for i in range(1, len(l)):
                self.alias.add(l[i])
            l = next(reader)
            if l: self.comment = l[0] 
            l = next(reader)
            self.items = [i for i in l]
            return self
        except StopIteration:
            return None


if __name__ == "__main__":
    tn = TitleNode("Mathematics")
    tn.add_alias("Math")
    for i in tn.get_alias():
        print(i)
    tn.add_item("1134")
    tn.add_item("1135")
    tn.add_item("1136")
    tn.add_item("1137")
    tn.add_item("1138")
    tn.add_item("1139")
    tn.add_item("1139")
    tn.rm_item("2")
    tn.rm_item("1134")
    tn.rm_alias("math")
    tn.set_comment("Left 1135 at Page 72")
    for i in tn.get_alias():
        print(i)
    print(tn.get_comment())
    for i in tn.get_items(4):
        print(i)


    with open("test_out.csv", "w") as fp:
        tn.write_to_csv(csv.writer(fp))

    with open("test_out.csv") as fp:
        rd = csv.reader(fp)
        tn.read_from_csv(rd)
