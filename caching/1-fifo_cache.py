#!/usr/bin/python3
"""
1-fifo_cache.py
FIFO Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a simple FIFO cache.
    """
    def put(self, key, item):
        """
        Add or update an element to the cache.
        """
        if key and item:
            current_size = len(self.cache_data)

            # Discard only if item is new and maximum cache size is reachded
            if key not in self.cache_data and current_size >= self.MAX_ITEMS:
                self.discard()

            # Recreate element on update to keep cahce order right
            if key in self.cache_data:
                self.cache_data.pop(key)

            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        item = self.cache_data.get(key, None)

        return item

    def discard(self):
        """
        Discard oldest element created or updated in cache.
        """
        item = next(iter(self.cache_data), None)

        if item:
            self.cache_data.pop(item)
            print(f"DISCARD: {item}")
