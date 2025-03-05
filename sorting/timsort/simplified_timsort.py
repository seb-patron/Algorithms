# from ..insertion_sort.insertion_sort import insertion_sort



def find_min_run(n):
    if n == 0:
        return 1
    
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r



def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        # move elements of arr[0..i-1], that are greater than temp, to one position ahead of their current position
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        # insert key into correct position
        arr[j + 1] = temp

    return arr

def merge(arr, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid

    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    i = 0 # index for left_arr
    j = 0 # index for right_arr
    k = left # index for merged array

    while i < left_size and j < right_size:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < left_size:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < right_size:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    # return arr

def simplified_timsort(arr):
    n = len(arr)
    min_run = find_min_run(n)
    # min_run = 32
    
    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        arr[start:end] = insertion_sort(arr[start:end])
        # insertion_sort(arr[start:end])

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n-1, left + size - 1)
            right = min(n-1, left + 2 * size - 1)

            if mid < right:
                # arr[left:right+1] = merge(arr, left, mid, right)
                merge(arr, left, mid, right)

        size *= 2

    return arr

