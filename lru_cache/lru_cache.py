import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    # it has the max number that is prob to be inside of it
    # it has the current number that is in side of it
    # a dll that the {0-?: value} pairs
    def __init__(self, limit=10):
        self.limit = limit
        # what is the max
        self.size = 0
        # how are we going to access it.
        self.order = DoublyLinkedList()
        # how is it stored. direction are saying by a dictionary
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # so we first have to see if the key is in the storage
        if key in self.storage:
        # now if key is in the storage we are going to have to assign it to
        # an object.
            object = self.storage[key]
        # once i assign it to an object then i have to "move the key-value
        # pair to the end of the order". I wonder why they dont want us to
        # move it to the head tho?
            self.order.move_to_end(object)
        # Next i will need to return the node value
            return object.value[1]
        # and prob do a else None
        # statment
        else:
            return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache.

    If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room.

    Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
    # i have to add the key:value pair to self.storage
    # self.storage is the only one that is in a dict formate
    if key in self.storage:
        # set node to the key
        node = self.storage[key]
        # and set the value of the node to the value
        node.value = (key, value)
        # now we have to move the key value pair to the end/begining of the line
        self.order.move_to_end(node)

    # if number of key:value pair is at self.storage max self.limits
    if self.limit == self.limit:
        # then remove oldest key:value pair remove from tail

    # now if key already is in cache
    # set the old key = to the new key
        pass
