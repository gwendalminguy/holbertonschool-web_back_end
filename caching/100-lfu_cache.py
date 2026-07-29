#!/usr/bin/python3
"""
5-lfu_caching.py
LFU Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a simple LFU cache.
    """
    def print_cache(self):
        """
        Print the cache
        Overwrite the BaseCaching method to adapt to LFU dictionary.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key).get("data")))

    def put(self, key, item, access_count=0):
        """
        Add or update an element to the cache.
        """
        if key is not None and item is not None:
            current_size = len(self.cache_data)

            # Discard only if item is new and maximum cache size is reachded
            if key not in self.cache_data and current_size >= self.MAX_ITEMS:
                self.discard()

            # Recreate element on update to keep cache order right
            if key in self.cache_data:
                content = self.cache_data.pop(key)
                access_count += content["access_count"]

            self.cache_data[key] = {
                "data": item,
                "access_count": access_count
            }

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        content = self.cache_data.get(key, None)

        if content is None:
            return None

        item = content["data"]

        # Recreate element to keep use order right
        self.put(key, item, access_count=1)

        return item

    def discard(self):
        """
        Discard least frequently accessed element in cache.
        """
        item = sorted(self.cache_data.items(), key=lambda item: item[1]["access_count"])[0][0]

        if item is not None:
            self.cache_data.pop(item)
            print(f"DISCARD: {item}")
