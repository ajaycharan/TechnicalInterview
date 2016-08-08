## Searching and Sorting

* Given an array with elements that are sorted in increasing order, a common task to search for a particular element in the array. Serially comparing with each element would lead to a time complexity of O(n) which is not useful for large datasets.
* An efficient searching algorithm is the binary search where we keep dividing the problem in half each time. This leads to a time complexity of O(log_2(n)+1). Usually CS has log with base 2 and so its safe to assume the time complexity to be O(log(n)).
* The implementation of binary search was difficult. The key idea to the solution is to use 3 variables min,mid and max to keep track of the current search area. This leads to an efficient solution. Check the [code](binarysearch.py).
* Recursion is a powerful tool used in implementation of several algorithms. A recursive function requires a base case and a recursive call with altered input for running. The base case needs to be carefully set to avoid infinite recursion.
* Sorting: There are several algorithms with each having their own pros and cons. It is better to remember these points for an interview. The considerations are in-place v. copy, time complexity v. space complexity and best, average, worst time complexities.
* Bubble sort: Naive approach to sorting. This is inplace sorting and has worst, avg time complexity of O(n^2) and best of O(n) when the array is already sorted. It also has a space complexity of O(1).
* Merge sort: Divide and conquer approach. It has an average time complexity of O(n logn) without much variations. However, it also has a space complexity of O(n).
* Quick sort: It does in-place sorting using a pivot. It has worst case time complexity of O(n^2) and avg, best time complexity of O(n logn). The best advantage is it has a space complexity of O(1). There can also be several heuristics to improve performance.

### Practice Problems

* [binarysearch.py](binarysearch.py): Implementation of binary search algorithm.
* [quicksort.py](quicksort.py): Implementation of quick sort algorithm.
