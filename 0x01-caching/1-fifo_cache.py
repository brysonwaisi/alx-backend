#!/usr/bin/env python3
'''First In First Out'''
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Represents an object that allows storing
    and retrieving items from dict with FIFO
    mechanism when limit is attained'''
    def __init__(self):
        '''Initializes cache'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add item to cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print('DISCARD:', first_key)

    def get(self, key):
        '''Retrieves an item by key'''
        return self.cache_data.get(key, None)
