import random

class Treap():
    def __init__(self):
        self.root = None

    def split(self, x):
        if self.root is None:
            return None, None
        elif self.root.key is None:
            return None, None
        else:
            


    def insert(self, x):
        node = TreapNode(x[0], x[1])
        left, right = split(root, x)

    def delete(self, key):
        i=3

    def search(self, key):
        i=4

class TreapNode():
    def __init__(self, priority, key):
        self.priority = priority
        self.key = key
        self.left = None
        self.right = None
