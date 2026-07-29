#!/usr/bin/python3
""" 
0-basic_cache.py
Basic Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache defines a simple cache.
    """
    def put(self, key, item):
        """
        Add or update an element to the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        item = self.cache_data.get(key, None)

        return item
