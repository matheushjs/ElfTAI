
class NamedEntity:
    """Class that represents an object that has the properties:

    1) Title - Proper name of the entity
    2) Aliases - Short names by which the entity can be referred to.

    Exceptions:
        TypeError - When any argument received has invalid type.
                    Most arguments are expected to be strings.
                    Even list of strings are type-checked.
        ValueError - When a value given as argument is ignored for any reason,
                     forcing the function not to do what its name suggests.
                     Happens when trying to add an alias that already exists, for example.
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
        Raises:
            ValueError if alias already existed."""
        if not isinstance(alias, str):
            raise TypeError
        if self.has_alias(alias):
            raise ValueError
        self.alias.add(alias.lower())

    def rm_alias(self, alias):
        """Removes given 'alias' from this Node.
        Alias is converted to lowercase before searching for it.
        Raises:
            ValueError if alias does not exist."""
        if not isinstance(alias, str):
            raise TypeError
        if not self.has_alias(alias):
            raise ValueError
        self.alias.remove(alias.lower())

    def get_alias(self):
        """Returns a list with all aliases of this Node.
        List is returned in no particular order."""
        return [i for i in self.alias]
