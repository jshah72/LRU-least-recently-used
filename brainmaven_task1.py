# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 07:19:51 2020

@author: JEET
"""

from collections import OrderedDict
 
class LRUCache:
 
    # initialising the maximum size
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
 
 # Return the value of the key that is queried in O(1) and return -1 if we don't find the key in our dictionary.
 # And also move the key to the end to show that it was recently used.
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
   
 # Initially, we add / update the key and  move the key to the end to show that it was recently used.
 # Here we will also check whether the length of dictionary has exceeded the capacity,if so we remove the first key (least recently used)
   
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        print("Adding :" , (key,value))
        if len(self.cache) > self.capacity:
            print("Removing:", self.cache.popitem(last = False))
            self.cache.popitem(last = False)
           
   
    def reset(self) -> None:
        print("Reset Prompted")
        self.cache.clear()
        
 
 # Initializing our cache with the capacity of 4
cache = LRUCache(4) 
 
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.put(5, 5)
print(cache.cache)
cache.put(6, 6)
print(cache.cache)
cache.put(7, 7)
print(cache.cache)
cache.put(8, 8)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(8)
print(cache.cache)
cache.reset()
cache.put(4, 4)
print(cache.cache)
cache.put(1, 1)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)


from unittest import mock

import pytest


@pytest.mark.parametrize(
    'ordinary_object',
    [
        'quill',
        'cushion',
        'cauldron',
    ],
)

def test_levitate_casts_a_spell(ordinary_object):
    with mock.patch(
        'levitation.cast_spell',
        autospec=True,
    ) as patched_cast_spell:        
        levitate(ordinary_object)

        patched_cast_spell.assert_called_once_with(target=ordinary_object)
        
        

from functools import lru_cache

@lru_cache(maxsize=None)
def f(x):
    return (x, x)


def test(mocker):
    ret = f(mocker.sentinel.DATA)
    assert ret == (mocker.sentinel.DATA, mocker.sentinel.DATA)