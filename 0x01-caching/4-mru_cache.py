#!/usr/bin/env python3
"""
MRU caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """"
    inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializing MRUCache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assign key and item
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            if key in self.stack:
                self.stack.remove(key)

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetch data with key
        """
        if not key or key not in self.cache_data:
            return None

        if key in self.stack:
            self.stack.remove(key)

        self.stack.append(key)
        return self.cache_data[key]
