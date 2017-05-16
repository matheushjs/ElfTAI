
class NamedEntity:
    """Class that represents an object that has the properties:

    1) Title - Proper name of the entity
    2) Aliases - Short names by which the entity can be referred to.
    """

    def __init__(self, title="Null"):
        self.title = title
        self.alias = set([])

    # Objects will be compared by their titles.
    def __eq__(self,other): return self.title.lower() == other.title.lower()
    def __ne__(self,other): return self.title.lower() != other.title.lower()
    def __lt__(self,other): return self.title.lower() < other.title.lower()
    def __le__(self,other): return self.title.lower() <= other.title.lower()
    def __gt__(self,other): return self.title.lower() > other.title.lower()
    def __ge__(self,other): return self.title.lower() >= other.title.lower()

    def get_title(self):
        """Returns the Title's name."""
        return self.title

    def set_title(self, string):
        """Changes current Title"""
        if not isinstance(string, str):
            raise TypeError
        if string != "":
            self.title = string
        else:
            self.title = "Null"

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
