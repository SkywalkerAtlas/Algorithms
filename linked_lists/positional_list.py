from linked_lists.doubly_linked_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

    # --------------------------------- Nested Position Class ---------------------------------------
    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)


    # --------------------------------- utility method ---------------------------------------------
    def _validate(self, p):
        """Return p's node if position is validated
        else raise error
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be Position type, got {} instead'.format(type(p)))
        if p._container is not self:
            raise ValueError('p dose not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position for given node (if node is sentinel, return None)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ------------------------------------ accessors ------------------------------------------------
    def first(self):
        """Return first position in the list (None if list is empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return last position in the list (None if list is empty)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return position before p (None if p is the first)"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return position after p (None if p is the last)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the element in the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------------- mutators ------------------------------------------------
    def _insert_between(self, e, predecessor, successor):
        """Add element between two nodes and return new Position"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of list and return new Position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of list and return ner Position"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e before Position p and return new Position"""
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        """Insert element e after Position p and return new Position"""
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        """Remove and return element e at position p"""
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        """Replace element e at position p with new element e', and return e"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    # Print
    def __str__(self):
        s = ''
        cursor = self.first()
        while cursor is not None:
            s += '{} -> '.format(cursor.element())
            cursor = self.after(cursor)
        return s[:-4]

if __name__ == '__main__':
    pl = PositionalList()

    # Add
    cursor = pl.add_first(5)
    print(pl)
    cursor = pl.add_after(cursor, 10)
    print(pl)
    cursor = pl.add_before(cursor, 7)
    print(pl)
    cursor = pl.add_last(8)
    print(pl)

    # Replace
    e = pl.replace(cursor, 9)
    print(pl)

    # Iter
    print('----------------- iter test --------------------')
    for e in pl:
        print(e)
    print('------------------------------------------------')

    # Delete
    e = pl.delete(cursor)
    print(pl)
    cursor = pl.last()
    cursor = pl.before(cursor)
    e = pl.delete(cursor)
    print(pl)
    # cursor = pl.before(cursor)

