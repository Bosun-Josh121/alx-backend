#!/usr/bin/env python3
"""
LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """"
    inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializing LRUCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assign key and item
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.queue:
            discard = self.queue.pop(0)  # Dequeue key
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)  # remove from the queue
            self.queue.append(key)  # enqueue key
            self.cache_data[key] = item

    def get(self, key):
        """Fetch data with key
        """
        if not key or key not in self.cache_data:
            return None
        # Remove from any position in the queue and add to the back
        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
