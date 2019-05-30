import random
# from graphviz import Digraph


class NoSuchElementException(Exception):
    """
    Error trying access an empty tree
    """
    pass


class RedBlackBST:

    class _Node:
        __slots__ = 'key', 'value', 'right', 'left', 'N', 'isRed'

        def __init__(self, key, value, N, isRed, right=None, left=None):
            self.key = key
            self.value = value
            self.N = N
            self.isRed = isRed
            self.right = right
            self.left = left

    def __init__(self):
        self.root = None
        self.size = 0
    
    def isEmpty(self):
        return (self.root is None)

    def _size(self, x):
        if x is None:
            return 0
        else:
            return x.N

    def _isRed(self, h):
        if h is None:
            return False
        else:
            return h.isRed == True

    def _rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.isRed = h.isRed
        h.isRed = True
        x.N = h.N
        h.N = 1 + self._size(h.left) + self._size(h.right)
        return x

    def _rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.isRed = h.isRed
        h.isRed = True
        x.N = h.N
        h.N = 1 + self._size(h.left) + self._size(h.right)
        return x

    def _filpColors(self, h):
        h.isRed = True
        h.left.isRed, h.right.isRed = False, False

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.isRed = False

    def _put(self, h, key, value):
        if h is None:
            return self._Node(key, value, 1, isRed=True)
        if key < h.key:
            h.left = self._put(h.left, key, value)
        elif key > h.key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value

        if self._isRed(h.right) and not self._isRed(h.left):
            h = self._rotateLeft(h)
        elif self._isRed(h.left) and self._isRed(h.left.left):
            h = self._rotateRight(h)
        elif self._isRed(h.left) and self._isRed(h.right):
            self._filpColors(h)

        h.N = self._size(h.right) + self._size(h.left) + 1

        return h

    # TODO: compelete deletion

    def deleteMin(self):
        if self.isEmpty():
            raise NoSuchElementException('Empty RedBlackBST')

    # def show(self):
    #     g = Digraph("RedBlackBST")
    #     self._show(self.root, g)
    #     g.view()


    # def _show(self, h, g):
    #     g.node(str(h.key), lable = str(h.key))
    #     if h.left is not None:
    #         h_left = self._show(h.left, g)
    #         g.node(str(h_left.key), lable = str(h_left.key))
    #         if h_left.isRed:
    #             g.edge(str(h.key), str(h_left.key), color='red')
    #         else:
    #             g.edge(str(h.key), str(h_left.key), color='black')
    #     if h.right is not None:
    #         h_right = self._show(h.right, g)
    #         g.node(str(h_right.key), label = str(h_right.key))
    #         if h_right.isRed:
    #             g.edge(str(h.key), str(h_right.key), color='red')
    #         else:
    #             g.edge(str(h.key), str(h_right.key), color='black')
    #     return h

if __name__ == '__main__':
    tr = {}
    tr_item = set(random.randint(1, 200) for _ in range(100))
    for i in tr_item:
        tr[i] = i
    # print(tr)

    rbTree = RedBlackBST()
    for k, v in tr.items():
        rbTree.put(k, v)

    # rbTree.show()
