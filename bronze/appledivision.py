def binSearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binSearch(arr, low, mid-1, x)
        else:
            return binSearch(arr, mid+1, high, x)
    else:
        return -1

print(binSearch([1,2,3,4,5,6,7], 0, 6, 7))