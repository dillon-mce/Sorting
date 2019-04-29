# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    current_index = 0
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr[current_index] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[current_index] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[current_index] = arrA.pop(0)
        else:
            merged_arr[current_index] = arrB.pop(0)
        current_index += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr
    midpoint = len(arr)//2

    return merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
