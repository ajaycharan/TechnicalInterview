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
            tempLength = h-t+1

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
