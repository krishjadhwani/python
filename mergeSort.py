import sys

def mergeSortHelper(array, start, end):
    # Base Case
    if start == end:
        return
    mid = start + (end - start)//2

    # Recursion
    mergeSortHelper(array, start, mid)
    mergeSortHelper(array, mid + 1, end)

    start2 = mid + 1

    # Return early if largest element in first half
    # is smaller than smallest element in second half
    if (array[mid] < array[start2]):
        return

    # Merge
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

def mergeSort(array):
    mergeSortHelper(array, 0, len(array) - 1)

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    array = [] 
    for i in range(n):
        array.append(int(input("#{}:".format(i+1))))
    mergeSort(array)
    print(array)
