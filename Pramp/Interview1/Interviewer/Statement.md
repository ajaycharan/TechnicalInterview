# Smallest Substring of All Characters

Given an array with unique characters arr and a string str, find the smallest substring of str containing all characters of arr.
### Example:
```
arr: [x,y,z], str: xyyzyzyx
result: zyx
```
Implement your solution and analyze the runtime complexity

### Hints & Tips
* If your peer is stuck, ask how can we determine if a given substring is valid (all chars from set are in it) and then ask how to apply that to a solution
* If your peer is using a naive solution of checking all possible substrings, try to ask how can you avoid duplicate work
* Make sure proper initializations are made
* Watch for unnecessary variables and steps
* For other solutions, make sure that any permutation of the characters in set can be found by the algorithm make sure your peer understand why we should increase tail only after head is increased.

### Solution
We iterate the string from left to right, while using two indices - `tailIndex` and `h`. At each iteration step, we examine the temp substring  `[str.charAt(tailIndex), str.charAt(tailIndex+1) ..., str.charAt(h)]`  and keep a copy of the shortest valid substring we've seen so far.

To examine substrings we use 2 counters:
* `uniqueCounter` (integer) - number of unique characters of arr in our temp substring
* `countMap` (map/object/associative array - depends of your language of choice) - number of occurrences of each char from arr in our substring

```python
def getShortestUniqueSubstring(arr, string):
    t = 0
    result = None
    countMap = {}
    uniqueCounter = 0

    # initialize countMap:
    for i in range(len(arr)):
        countMap[arr[i]] = 0

    # scan str
    for h in range(len(string)):
        # check the new head
        head = string[h]
        if head not in countMap.keys():
            continue

        # update counter
        if countMap[head] == 0:
            uniqueCounter += 1
        countMap[head] += 1

        # push tail forward
        while uniqueCounter == len(arr):
            # length of current substr
            tempLength = h - t + 1

            # best possible case, return string
            if tempLength == len(arr):
                return string[t:h+1]

            # check with previous result
            if (result == None or tempLength < len(result)):
                result = string[t:h+1]

            # update counter for new tail
            tail = string[t]
            if tail in countMap.keys():
                countMap[tail] -= 1
                if countMap[tail] == 0:
                    uniqueCounter -= 1
            t += 1

    return result
```
