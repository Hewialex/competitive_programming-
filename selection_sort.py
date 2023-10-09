def select(arr, i):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    return min_idx

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = select(arr, i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage:
arr = [4, 1, 3, 9, 7]
selectionSort(arr)
print("Sorted array:", arr)  # Output: [1, 3, 4, 7, 9]
