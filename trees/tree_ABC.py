class TreeABC:
    """Abstract base class representing a tree structure"""

    # -------------------------------- nested Position class ------------------------------
    class Position:

        def element(self):
            """Return the element stored in this position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    # --------------------------------- abstract methods ----------------------------------
    def root(self):
        """Return Position representing the tree's root (None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (None if p is root)"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children Position p has"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Return the iteration of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return total number of element in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    # --------------------------------- concrete methods ----------------------------------
    def is_root(self, p):
        """Return true if Position p is tree's root"""
        return p == self.root()

    def is_leaf(self, p):
        """Return true if Position p does NOT have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree is empty"""
        return len(self) == 0

    # --------------------------------- depth and height ---------------------------------
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """Return height of subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        """Return height of subtree rooted at Position p
        if p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height(p)
