

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