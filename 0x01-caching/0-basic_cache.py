#!/usr/bin/env python3
"""
basic cahing class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from base_caching system
    """
    def __init__(self):
        """
        initializes the class
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        assigns the given key to the given item
        """
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """
        return the value of the given key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
