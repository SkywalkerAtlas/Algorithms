from trees.tree_ABC import TreeABC

class BinaryTreeABC(TreeABC):
    """Abstract base class representing a binary tree structure"""

    # ------------------------------ abstract methods ---------------------------------------
    def left(self, p):
        """Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError('must be implemented by subclass')

    # ------------------------------- concrete method --------------------------------------
    def sibling(self, p):
        """Return a Position representing p's sibling
        Return None if no sibling
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
