"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmap, maping key to nodes
        self.left, self.right = Node(0,0), Node(0,0) # dummy nodes, left dummy node = least recently used, right dummy node = most recently used
        self.left.next, self.right.prev = self.right, self.left # connect the two dummy nodes together

    # helper function 1, remove from the list
    def remove(self, node):
        previous, nextNode = node.prev, node.next
        previous.next, nextNode.prev = nextNode, previous

    # helper function 2, insert at right position
    def insert(self, node):
        previous, nextNode = self.right.prev, self.right
        previous.next = nextNode.prev = node
        node.next, node.prev = nextNode, previous


    def get(self, key: int) -> int:
        if key in self.cache:
            # first remove it from the linked list, then update lru and mru, then return the value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # if it does not exist
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the linked list and evict the lru from the hashmap cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
