#!/usr/bin/env python

# Implementation to find smallest substring containing all desired chars.
# Pramp Interview 1

def getShortestUniqueSubstring(arr, string):
    t = 0
    substr = None
    charFreq = {}
    uniqueChar = 0

    # fill up the dict
    for char in arr:
        charFreq[char] = 0

    # loop over the string
    for h in range(len(string)):
        # check for head
        head = string[h]
        if head not in charFreq.keys():
            continue

        # update counters
        if charFreq[head] == 0:
            uniqueChar += 1
        charFreq[head] += 1

        # check for substring if all chars are there
        while uniqueChar == len(arr):
            # update substr
            tempLength = h-t+1
            if tempLength == len(arr):
                return string[t:h+1]
            if substr == None or tempLength < len(substr):
                substr = string[t:h+1]

            # update tail
            tail = string[t]
            if tail in charFreq.keys():
                charFreq[tail] -= 1
                if charFreq[tail] == 0:
                    uniqueChar -= 1
            t += 1

    return substr

array = ['x','y','z']
string = "xyyzyzyx"
print getShortestUniqueSubstring(array, string)
