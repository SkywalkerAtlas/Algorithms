from linked_lists.doubly_linked_base import _DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(_DoublyLinkedBase):
    """Deque implementation based on a doubly linked list"""

    def first(self):
        """Return the first element of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """Return the last element of the deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add the element e to the front of deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add the element e to the last of the deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the front element
        Raise Empty Error if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove the return the last element
        Raise Empty Error if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)

    def __str__(self):
        s = 'header -> '
        cursor = self._header._next
        while cursor._next is not None:
            s += '{} -> '.format(cursor._element)
            cursor = cursor._next
        return s + 'trailer'

if __name__ == '__main__':
    lq = LinkedDeque()

    # Check length
    print(lq.is_empty())

    # Insert element and check
    lq.insert_first(1)
    print(lq)
    lq.insert_first(2)
    print(lq)
    lq.insert_last(4)
    print(lq)

    # Delete element and check
    lq.delete_first()
    print(lq)
    lq.delete_last()
    print(lq)
