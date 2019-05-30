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
        
        # For debug
        def __str__(self):
            return 'key: {}, value: {}, N: {}, color: {}'.format(self.key, self.value, self.N, 'Red' if self.isRed else 'Black')

    def __init__(self):
        self.root = None
    
    # ---------------------------------------------------- Node Helper Method -----------------------------------------------------
    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x is None:
            return 0
        else:
            return x.N
    
    def _isEmpty(self):
        return (self.root is None)

    def _isRed(self, h):
        if h is None:
            return False
        else:
            return h.isRed == True
    
    # -------------------------------------------------- Ordered Symbol Table Helper Method ---------------------------------------------
    def rank(self, key):
        """Return the number of keys in the symbol table strictly less than key"""
        return self._rank(self.root, key)
    
    def _rank(self, h, key):
        if h is None:
            return 0
        if key < h.key:
            return self._rank(h.left, key)
        elif key > h.key:
            return self._rank(h.right, key) + self._size(h.left) + 1
        else:
            return self._size(h.left)
        
    def select(self, k):
        """Return (k+1)th smallest key in the tree"""
        h = self._select(self.root, k)
        return h

    def _select(self, h, k):
        t = self._size(h.left)
        if t > k:
            return self._select(h.left, k)
        elif t < k:
            return self._select(h.right, k-t-1)
        else:
            return h
    
    # --------------------------------------------------- BST Search ---------------------------------------------------------
    def get(self, key):
        return self._get(self.root, key)
    
    def _get(self, h, key):
        x = h
        while x is not None:
            if key > x.key:
                x = x.right
            elif key < x.key:
                x = x.left
            else:
                return x.value
        return None

    def min(self):
        return self._min(self.root)

    def _min(self, h):
        if h.left is None:
            return h
        else:
            return self._min(h.left)
    
    def max(self):
        return self._max(self.root)
    
    def _max(self, h):
        if h.right is None:
            return h
        else:
            return self._max(h.right)

    # ------------------------------------------------ Red Black Tree Helper Methods --------------------------------------------

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

    def _flipColors(self, h):
        h.isRed = not h.isRed
        h.left.isRed, h.right.isRed = not h.left.isRed, not h.right.isRed

    def _moveRedLeft(self, h):
        self._flipColors(h)
        if self._isRed(h.right.left):
            h.right = self._rotateRight(h.right)
            h = self._rotateLeft(h)
            self._flipColors(h)
        return h

    def _moveRedRight(self, h):
        self._flipColors(h)
        if self._isRed(h.left.left):
            h = self._rotateRight(h)
        return h


    def _balance(self, h):
        if self._isRed(h.right):
            h = self._rotateLeft(h)
        if self._isRed(h.left) and self._isRed(h.left.left):
            h = self._rotateRight(h)
        if self._isRed(h.left) and self._isRed(h.right):
            self._flipColors(h)
        
        h.N = self._size(h.left) + self._size(h.right) + 1
        return h
    
    # ----------------------------------------------------- Red Black Tree Insertion ---------------------------------------------
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
            self._flipColors(h)

        h.N = self._size(h.right) + self._size(h.left) + 1

        return h

    # -------------------------------------------------- Red Black Tree Deletion -----------------------------------------------
    def deleteMin(self):
        if self._isEmpty():
            raise NoSuchElementException('Empty RedBlackBST')
        
        if not self._isRed(self.root.left) and not self._isRed(self.root.right):
            self.root.isRed = True
        
        self.root = self._deleteMin(self.root)
        if not self._isEmpty():
            self.root.isRed = False

    def _deleteMin(self, h):
        if h.left is None:
            return None
        if not self._isRed(h.left) and not self._isRed(h.left.left):
            h = self._moveRedLeft(h)
        
        h.left = self._deleteMin(h.left)
        return self._balance(h)

    def deleteMax(self):
        if self._isEmpty():
            raise NoSuchElementException('Empty RedBlackBST')

        if not self._isRed(self.root.left) and not self._isRed(self.root.right):
            self.root.isRed = True
        
        self.root = self._deleteMax(self.root)
        if not self._isEmpty():
            self.root.isRed = False

    def _deleteMax(self, h):
        if self._isRed(h.left):
            h = self._rotateRight(h)
        
        if h.right is None:
            return None
        
        if not self._isRed(h.right) and not self._isRed(h.right.left):
            h = self._moveRedRight(h)
        
        h.right = self._deleteMax(h.right)
        return self._balance(h)
    
    def delete(self, key):
        if self._isEmpty():
            raise NoSuchElementException('Empty RedBlackBST')
        if not self._contains(key):
            return
        
        if not self._isRed(self.root.left) and not self._isRed(self.root.right):
            self.root.isRed = True
        
        self.root = self._delete(self.root, key)
        if (not self._isEmpty()):
            self.root.isRed = False
    
    def _delete(self, h, key):
        if key < h.key:
            if not self._isRed(h.left) and not self._isRed(h.left.left):
                h = self._moveRedLeft(h)
            h.left = self._delete(h.left, key)
        else:
            if self._isRed(h.left):
                h = self._rotateRight(h)
            if key == h.key and (h.right is not None):
                return None
            if not self._isRed(h.right) and not self._isRed(h.right.left):
                h = self._moveRedRight(h)
            
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.value = x.value
                h.right = self._deleteMin(h.right)
            else:
                h.right = self._delete(h.right, key)
            
        return self._balance(h)
        
    # -------------------------------------------- Integrity Checker ----------------------------------
    def _contains(self, key):
        return self.get(key) is not None

    def check(self):
        if not self.isBST():
            print('Not in symmetric order')
        if not self.isSizeConsistent():
            print('Subtree counts not consistent')
        if not self.is23():
            print('Not a 2-3 tree')
        if not self.isBalanced():
            print('Not Balanced')
        return self.isBST() and self.isSizeConsistent() and self.is23() and self.isBalanced()

    def isBST(self):
        return self._isBST(self.root, None, None)

    def _isBST(self, h, min_, max_):
        if h is None:
            return True
        if (min_ is not None) and h.key < min_:
            return False
        if (max_ is not None) and h.key > max_:
            return False
        return self._isBST(h.left, min_, h.key) and self._isBST(h.right, h.key, max_)

    def isSizeConsistent(self):
        return self._isSizeConsistent(self.root)
    
    def _isSizeConsistent(self, h):
        if h is None:
            return True
        if h.N != self._size(h.left) + self._size(h.right) + 1:
            return False
        return self._isSizeConsistent(h.left) and self._isSizeConsistent(h.right)
    
    def is23(self):
        return self._is23(self.root)
    
    def _is23(self, h):
        if h is None:
            return True
        if self._isRed(h.right):
            return False
        if h != self.root and self._isRed(h) and self._isRed(h.left):
            return False
        return self._is23(h.left) and self._is23(h.right)
    
    def isBalanced(self):
        black = 0
        h = self.root
        while h is not None:
            if not self._isRed(h):
                black += 1
            h = h.left
        
        return self._isBalanced(self.root, black)
    
    def _isBalanced(self, h, black):
        if h is None:
            return black == 0
        if (not self._isRed(h)):
            black -= 1
        return self._isBalanced(h.left, black) and self._isBalanced(h.right, black)

    # def show(self):
    #     g = Digraph("RedBlackBST")
    #     self._show(self.root, g)
    #     g.view()


    # def _show(self, h, g):
    #     g.node(str(h.key), label = str(h.key))
    #     if h.left is not None:
    #         h_left = self._show(h.left, g)
    #         g.node(str(h_left.key), label = str(h_left.key))
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
    random.seed(1024)
    tr_item = set(random.randint(1, 2000) for _ in range(500))
    for i in tr_item:
        tr[i] = i
    # print(tr)

    rbTree = RedBlackBST()
    for k, v in tr.items():
        rbTree.put(k, v)

    # print(rbTree.get(124))
    rbTree.deleteMin()
    rbTree.deleteMin()
    rbTree.deleteMin()
    rbTree.deleteMin()
    rbTree.deleteMin()
    rbTree.deleteMax()
    print(rbTree.check())
    # rbTree.show()
