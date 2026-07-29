## Caching

This project is about learning to work with caching.

### Files

* [base_caching.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/base_caching.py), an abstract class implementing a base to create a cache class.

* [0-basic_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/0-basic_cache.py), a class implementing a basic cache.

* [1-fifo_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/1-fifo_cache.py), a class implementing a FIFO cache.

* [2-lifo_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/2-lifo_cache.py), a class implementing a LIFO cache.

* [3-lru_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/3-lru_cache.py), a class implementing a LRU cache.

* [4-mru_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/4-mru_cache.py), a class implementing a MRU cache.

* [100-lfu_cache.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/caching/100-lfu_cache.py), a class implementing a LFU cache.

### Policies

A caching system usually implements a [Cache Replacement Policy](https://en.wikipedia.org/wiki/Cache_replacement_policies). The chosen policy will define which element to discard in the cache when the cache reaches its maximum capacity. The goal is to make the best use of the available memor, while maximizing cache efficiency.

| **Name** | **Description** |
| :------- | :-------------- |
| [FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_in_first_out_(FIFO)) | **First In First Out**: discarding the oldest inserted element. |
| [LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_in_first_out_(LIFO)_or_First_in_last_out_(FILO)) | **Last In First Out**: discarding the most recently inserted element. |
| [LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU)) | **Least Recently Used**: discarding the least recently accessed element. |
| [MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU)) | **Most Recently Used**: discarding the most recently accessed element. |
| [LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_frequently_used_(LFU)) | **Least Frequently Used**: discarding the least frequently accessed element. |
