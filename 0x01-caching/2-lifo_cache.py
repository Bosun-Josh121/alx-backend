#!/usr/bin/env python3
"""
LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializing LIFO caching
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Assigning key and item
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        if key and item:
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetch data with key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
