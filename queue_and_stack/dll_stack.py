import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # we are going to add a value to the head of the stack
        self.storage.add_to_head(value)


    def pop(self):
        # we are going to remove the head of the stack
        if self.len() > 0:
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return len(self.storage)
