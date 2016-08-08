## Searching and Sorting

* Given an array with elements that are sorted in increasing order, a common task to search for a particular element in the array. Serially comparing with each element would lead to a time complexity of O(n) which is not useful for large datasets.
* An efficient searching algorithm is the binary search where we keep dividing the problem in half each time. This leads to a time complexity of $$O(log_2(n)+1)$$. Usually CS has log with base 2 and so its safe to assume the time complexity to be O(log(n)).
* The implementation of binary search was difficult. The key idea to the solution is to use 3 variables min,mid and max to keep track of the current search area. This leads to an efficient solution. Check the [code](binarysearch.py).

### Practice Problems

* [binarysearch.py](binarysearch.py): Implementation of binary search algorithm.
