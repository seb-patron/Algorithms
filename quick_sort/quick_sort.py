import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        # less = [i for i in arr[:pivot_index] + arr[pivot_index + 1:] if i <= pivot]
        # greater = [i for i in arr[:pivot_index] + arr[pivot_index + 1:] if i > pivot]

        less = [i for i in arr if i < pivot]
        equal = [i for i in arr if i == pivot]
        greater = [i for i in arr if i > pivot]

        return quick_sort(less) + equal + quick_sort(greater)