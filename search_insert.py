"""
 find index of given number in sorted array

 for example in this array [1,2,3,4,5,6,12,13,14] we want to find index of 7

"""


def search_insert(arr, val):
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:
        if val > arr[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid

    return low


print(search_insert([1, 2, 3, 4, 5, 6, 12, 13, 14], 7))


