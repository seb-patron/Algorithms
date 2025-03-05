

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

def merge(left, right):
    new_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else: # right smaller than left
            new_arr.append(right[j])
            j += 1

    return new_arr + left[i:] + right[j:]