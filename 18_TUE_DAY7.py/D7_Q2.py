#MERGE_SORT
# Here l is left, r is right, and m is middle element.
def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
    left_arr = [0]*n1
    right_arr = [0]*n2

    for i in range(n1):
        left_arr[i] = arr[l+i]

    for i in range(n2):
        right_arr[i] = arr[m+1+i]

    L = 0
    R = 0
    k = l

    while (L < n1 and R < n2):
        if (left_arr[L] <= right_arr[R]):
            arr[k] = left_arr[L]
            L += 1
        else:
            arr[k] = right_arr[R]
            R += 1
        k += 1

    while (L < n1):
        arr[k] = left_arr[L]
        L += 1
        k += 1

    while (R < n2):
        arr[k] = right_arr[R]
        R += 1
        k += 1

def mergeSortNew(arr, l, r):
    if(l < r):
        m = (l+r)//2
        mergeSortNew(arr, l, m)
        mergeSortNew(arr, m+1, r)

        # returns merged sorted list.
        merge(arr, l, m, r)

def mergeSort(arr, n):
    mergeSortNew(arr, 0, n-1)

    return arr