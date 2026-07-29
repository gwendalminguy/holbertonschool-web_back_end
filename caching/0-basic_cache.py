#!/usr/bin/python3
""" 
0-basic_cache.py
Basic Cache
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Add or update an element to the cache.
        """
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        item = self.cache_data.get(key, None)

        return item
