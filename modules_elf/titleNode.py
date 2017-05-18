#    ElfTAI specific CSV file manager.
#    Copyright (C) 2017 Matheus Henrique Junqueira Saldanha
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Contact: matheus.saldanha@usp.br

import csv
import termcolor as tc

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
        title_row = [self.get_title(),]
        title_row.extend(self.get_alias())
        writer.writerows([title_row, self.comment.get_list(), self.items])

    def read_from_csv(self, reader):
        """Reads a Node from a csv file, overwriting the current Node instance.
        Returns self. 
        Raises:
            ValueError - if node could not be read from 'reader'."""
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

    def print_line(self, width=0):
        """Prints a TitleNode in a line, with colors.
        TitleNode's title will span 'width' characters.
        Intentionally not implemented as __str__"""
        if not isinstance(width, int):
            raise TypeError
        
        print("{name} ({alias})".format(
                name=tc.colored(self.get_title().center(width), 'cyan', attrs=['bold', 'dark']),
                alias=tc.colored(','.join(self.get_alias()), color='yellow')
            )
        )

    def print_block(self, length=-1):
        """Prints a TitleNode as a block, with all information desired.
        Only latest 'length' items will be printed, if it's given.
        If it's not given, will print all items."""
        title = self.get_title()
        alias = self.get_alias()
        comm = self.get_comment()
        items = self.get_items(length)

        print(tc.colored("{}".format(title), 'magenta', attrs=['bold']))

        i = 0
        for c in comm.get_list():
            print(tc.colored("\t[{}] - '{}'".format(i, c), 'yellow'))
            i = i + 1
        if i == 0:
            print(tc.colored("Empty", 'yellow'))

        if len(items) == 0:
            print(tc.colored("Empty", attrs=['bold']))
        else:
            print(tc.colored(', '.join([ str(i) for i in items]), attrs=['bold']))
