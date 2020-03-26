import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

def __init__(self, limit =10):
    self.limit = limit
    self.size = 0
    self.order = DouplyLinkedList()
    self.storage = dict()

def get(selt,key):
    # key is not in cache  - return none
    if key not in self.storage:
        return None
    else:
        # Key is in cache
            #return value 
        node = self.storage[key]
        self.order.move_to_end(node)
        return node.value[1]
            #move it to most recently used









    pass




def set(self, key, value):
    if key in self.storage:
        #overwrite it the value
        # where is the value stored
        node = self.storage[key]
        node.value = (key,value)

        # move to the tail (the most recently used )
        self.order.move_to_end(node)
        return
    # size is at limit
    if len(self.order) == self.limit:
        #evict the oldest one
        index_of_oldest = self.order.head.value[0]
        del self.storage[index_of_olderst]
        self.order.remove_from_head()

        # add to order
    self.order.add_to_tail((key,value))
    # add it to storage
    self.storage[key] = self.order.tail
    # if item/key already exists
