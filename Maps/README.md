## Maps and Hashing

* Maps or dictionaries are a data structure that have (key,value) pairs. A map relies on a set which is an unordered collection of items. The keys of a dictionary are usually implemented as a set.
* Hashing is usually used to implement a constant time lookup when we have a large dataset. It relies on the implementation of a hash function to remap the values to a hash value. This hash value can be used to look up the element.
* However, depending on the data and the hash function there can be collisions and so we need to handle. It can be done either by using a better hash function or using buckets at each hash value location. There can also be a cascade of hash functions for buckets with many values.
* Its a popular question to ask in interviews. We need to discuss all such considerations when answering the question.
* Hash maps is a combination of hashing and dictionaries. If we are using string keys then we use the ascii values of a subset of the characters to generate the hash value.

### Practice Problems

* [dictionary.py](dictionary.py): Practice working with dictionaries.
* [hashmap.py](hashmap.py): Implementation of a hash map.
