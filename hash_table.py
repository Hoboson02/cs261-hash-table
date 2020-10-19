# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    def __init__(self, size=10): 
        self.data = [[] for __ in range(size)]
        self.size = size
        return None

    def __setitem__(self, key, value):
        self.data.append([key, value])
        return None

    def __getitem__(self, key):
        return 

    def hash(self, key):
        return hash(key) % len(self.data)
