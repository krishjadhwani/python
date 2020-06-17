import sys

def getArrays(fileName):
    file = open(fileName)
    lines = []
    for line in file:
        lines.append(line.split(','))
    return lines

def mergeSortHelper(array, start, end):
    # Base Case
    if start == end:
        return
    mid = start + (end - start)//2

    # Recursion
    mergeSortHelper(array, start, mid)
    mergeSortHelper(array, mid + 1, end)

    # Merge
    start2 = mid + 1

    # Return early if largest element in first half
    # is smaller than smallest element in second half
    if (array[mid] < array[start2]):
        return
    while (start <= mid and start2 <= end):
        if (array[start] < array[start2]):
            start +=1
        else:
            value = array[start2]
            index = start2
            while (index > start):
                array[index] = array [index - 1]
                index -= 1
            array[start] = value
            start += 1
            mid += 1
            start2 += 1
    print(array)

def mergeSort(array):
    mergeSortHelper(array, 0, len(array) - 1)

if __name__ == '__main__':
    #fileName = sys.argv[1]
    #arrays = getArrays(fileName)
    arrays = [[
        12,33,4,21,155,56,4,9
    ]]
    for array in arrays:
        mergeSort(array)
