"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    quicksort2(array,0,len(array)-1)

def quicksort2(array,first,last):

    if first < last:
        splitPoint = partition(array,first,last)

        quicksort2(array,first,splitPoint-1)
        quicksort2(array,splitPoint+1,last)

def partition(array,first,last):
    p = first
    lM = first+1
    rM = last

    done = False
    while not done:
        while array[lM] <= array[p] and lM <= rM:
            lM += 1

        while array[rM] >= array[p] and rM >= lM:
            rM -= 1

        if rM < lM:
            done = True
        else:
            temp = array[lM]
            array[lM] = array[rM]
            array[rM] = temp

    temp = array[p]
    array[p] = array[rM]
    array[rM] = temp

    return rM

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test)
print test
