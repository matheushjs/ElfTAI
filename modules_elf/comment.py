
class Comment:
    def __init__(self):
        self.comment = "" # Could be a list

    def set_comment(self, comment):
        """Changes current comment of this Object.
        Returns the comment that was replaced by the new one."""
        if not isinstance(comment, str):
            raise TypeError
        temp = self.comment
        self.comment = comment
        return temp

    def get_comment(self):
        """Returns the comment in this Node."""
        return self.comment
