## Caching

This project is about learning to work with caching.

### Files

* [base_caching.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/base_caching.py), an abstract class implementing a base to create a cache class.

* [0-basic_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/0-basic_cache.py), a class implementing a basic cache.

* [1-fifo_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/1-fifo_cache.py), a class implementing a FIFO cache.

* [2-lifo_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/2-lifo_cache.py), a class implementing a LIFO cache.

* [3-lru_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/3-lru_cache.py), a class implementing a LRU cache.

* [4-mru_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/4-mru_cache.py), a class implementing a MRU cache.

### Policies

A caching system usually implements a [Cache Replacement Policy](https://en.wikipedia.org/wiki/Cache_replacement_policies). The chosen policy will define which element to discard in the cache when the maximum allowed size is reached, to optimize memory usage. The most common policies are the following:

| **Name** | **Description** |
| :------- | :-------------- |
| [FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_in_first_out_(FIFO)) | **First In First Out**, a policy that disards the oldest modified element. |
| [LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_in_first_out_(LIFO)_or_First_in_last_out_(FILO)) | **Last In First Out**, a policy that disards the most recently modified element. |
| [LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU)) | **Least Recently Used**, a policy that disards the least recently retrieved element. |
| [MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU)) | **Most Recently Used**, a policy that disards the most recently modified element. |
