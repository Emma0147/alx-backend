#!/usr/bin/env python3
"""
Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache
    """
    def put(self, key, item):
        """If key or item is None, do nothing"""
        if key is None or item is None:
            return

        """Assign the item value to the key key in the cache dictionary"""
        self.cache_data[key] = item

    def get(self, key):
        """If key is None or doesn't exist in the cache, return Non"""
        if key is None or key not in self.cache_data:
            return None

        """Return the value associated with the key in the cache"""
        return self.cache_data[key]
