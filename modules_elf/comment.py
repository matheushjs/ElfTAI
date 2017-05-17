
class Comment:
    """Class for managing comments.
    Manages a list of comments, allowing operations replace, add, remove.
    May provide user-interaction functions too, if needed."""

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
        elif isinstance(comment, list):
            if False in [isinstance(i, str) for i in comment]:
                raise TypeError
            self.comment.extend(comment)
        else: raise TypeError

    def get(self, index):
        """Returns a comment from this Object."""
        return self.comment[index]

    def get_list(self):
        """Returns the list with all comments"""
        return self.comment
