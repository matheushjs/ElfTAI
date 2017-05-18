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

class Comment:
    """Class for managing comments.
    Encapsulates a list of comments, allowing operations within it.
    
    Exceptions:
        TypeError: When any given argument has the wrong type.
        IndexError: When an inexistent element is accessed.
        Exception: Any other exception is to be considered a fatal bug.
    """

    def __init__(self):
        self.comment = []

    def __getitem__(self, idx):
        return self.get(idx)
    
    def __setitem__(self, idx, new):
        self.set(idx, new)

    def __len__(self):
        """Returns the number of comments in this Object."""
        return len(self.comment)

    def set(self, index, comment):
        """Changes one comment of this Object.
        Returns the comment that was replaced by the new one."""
        if not isinstance(comment, str):
            raise TypeError
        temp = self.comment[index]
        self.comment[index] = comment
        return temp

    def add(self, comment):
        """Appends a comment to the list of comments.
        'comment' can be a string or a list of these."""
        if isinstance(comment, str):
            self.comment.append(comment)
        elif isinstance(comment, list) \
        and False not in [isinstance(i, str) for i in comment]:
            self.comment.extend(comment)
        else: raise TypeError

    def get(self, index):
        """Returns a comment from this Object."""
        return self.comment[index]

    def get_list(self):
        """Returns the list with all comments"""
        return [i for i in self.comment]

    def rm(self, index):
        """Removes comment of index 'index'.
        Returns the removed comment."""
        return self.comment.pop(index)
