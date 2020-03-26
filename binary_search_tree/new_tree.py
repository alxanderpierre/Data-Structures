import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BinarySearchTree(Tree)
            else:
                self.left.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.left.contains(target)

    def get_max(self):
        if self.right:
            return self.right.get_max():
        else:
            return self.value

    def for_each(self,cd):
        cb(self.value)

        if slef.left:
            self.left.for_each(cb)
        if  self.right:
            self.right.for_each(cb)
