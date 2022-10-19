def merge(arr, left, middle, right):

    n1 = middle - left + 1
    n2 = right - middle
    left_arr = [0]*n1
    right_arr = [0]*n2

    for i in range(n1):
        left_arr[i] = arr[left+i]

    for i in range(n2):
        right_arr[i] = arr[middle+1+i]

    ptrLeft = 0
    ptrRight = 0
    k = left

    while (ptrLeft < n1 and ptrRight < n2):
        if (left_arr[ptrLeft] <= right_arr[ptrRight]):
            arr[k] = left_arr[ptrLeft]
            ptrLeft += 1
        else:
            arr[k] = right_arr[ptrRight]
            ptrRight += 1
        k += 1

    # Copy the remaining elements of leftHalves if there are any.
    while (ptrLeft < n1):
        arr[k] = left_arr[ptrLeft]
        ptrLeft += 1
        k += 1

    # Copy the remaining elements of rightHalves if there are any.
    while (ptrRight < n2):
        arr[k] = right_arr[ptrRight]
        ptrRight += 1
        k += 1

def mergeSortNew(arr, left, right):
    if(left < right):
        middle = (left+right)//2
        mergeSortNew(arr, left, middle)
        mergeSortNew(arr, middle+1, right)

        # returns merged sorted list.
        merge(arr, left, middle, right)

def mergeSort(arr, n):
    mergeSortNew(arr, 0, n-1)

    return arr