from random import random

"""
Student Id: 1064689
Student Name: Pingzhou Li
"""
# reference https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/treap.py
# a very interesting implementation without rotation

class TreapNode:
    def __init__(self, key):
        self.priority = random()
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return "({}:{}, left:{}, right:{})".format(self.priority, self.key, self.left, self.right)

def split(rootNode:TreapNode, key):
    if rootNode is None:  # None root return None for left and right
        return None, None
    elif rootNode.key is None: # for special occasion
        return None, None
    else:
        if key[1] < rootNode.key[1] or (key[1] == rootNode.key[1] and key[0] < rootNode.key[0]):
            """
            key should in left subtree
            split left subtree with key into l-tree and r-tree
            concatenate r-tree to root's left sub tree (all nodes are with bigger keys)
            l-tree to be the left part (all nodes are with smaller keys)
            """
            left, rootNode.left = split(rootNode.left, key)
            return left, rootNode
        else:
            """
            node with equal key will be in the left tree
            split right subtree with key into l-tree and r-tree
            concatenate l-tree to root's right sub tree (all nodes are with smaller keys)
            r-tree to be the right part (all nodes are with equal or bigger keys)
            """
            rootNode.right, right = split(rootNode.right, key)
            return rootNode, right

def merge(leftNode:TreapNode, rightNode:TreapNode):
    """
    left tree's nodes key must be less than right tree's nodes key
    """
    if (not leftNode) or (not rightNode):  # If one node is None, return the other
        return leftNode or rightNode
    elif leftNode.priority < rightNode.priority:
        """
        if left node's priority is less than right node's priority
        merge right tree to left tree's right subtree (all nodes with bigger priority than the root of left tree)
        then concatenate new tree to left tree's right subtree
        """
        leftNode.right = merge(leftNode.right, rightNode)
        return leftNode
    else:
        """
        if left node's priority is more than or equal to right node's priority
        merge left tree to right tree's left subtree (all nodes with smaller priority than the root of right tree)
        then concatenate new tree to right tree's left subtree
        """
        rightNode.left = merge(leftNode, rightNode.left)
        return rightNode


# x (id, key)
def insert(root: TreapNode, x):
    """
    Split root tree with newNode's key into left, right,
    Merge left, node, right into root
    """
    new_node = TreapNode(x)
    key = new_node.key
    left, right = split(root, key)
    return merge(merge(left, new_node), right)


def delete(root: TreapNode, key):
    """
    Split all nodes with keys less than key into left,
    Split all nodes with keys greater than key into right.
    Merge left and right
    """
    left, right = split(root, (0, key))
    _, right = split(right, (10000000, key))
    return merge(left, right)


def search(rootNode: TreapNode, key):
    if rootNode is None:
        return None
    elif rootNode.key[1] == key[1]:
        return rootNode
    else:
        if key[1] < rootNode.key[1]:
            # search key in left subtree
            return search(rootNode.left, key)
        else:
            # otherwise in right subtree
            return search(rootNode.right, key)


