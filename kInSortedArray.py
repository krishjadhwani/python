def binarySearch(arr, start, end, query, side):
    # Base Case
    if (start == end):
        if(arr[start] == query):
            return start
        return -1
    # Recurse
    mid = int(start + (end - start)//2)
    # Search Left
    if (query < arr[mid]):
        return binarySearch(arr, start, mid - 1, query, side)
    # Search Right
    elif(query > arr[mid]):
        return binarySearch(arr, mid + 1, end, query, side)
    # Found query, search for left most or right most based on side
    else:
        search = binarySearch(arr, start, mid - 1, query, side) if side else binarySearch(arr, mid + 1, end, query, side)
        return search if search != -1 else mid

def findKInSortedArray(array, k):
    start = binarySearch(array, 0, len(array) - 1, k, True)
    if (start == -1):
        return 0
    end = binarySearch(array, 0, len(array) - 1, k, False)
    return end - start + 1

if __name__ == '__main__':
    array = [1,2,3,3,5,7,7]
    print(array)
    print(3, findKInSortedArray(array, 3))
    print(7, findKInSortedArray(array, 7))
