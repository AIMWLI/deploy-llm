def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def dual_pivot_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        lp, rp = dual_pivot_partition(arr, low, high)
        dual_pivot_quicksort(arr, low, lp - 1)
        dual_pivot_quicksort(arr, lp + 1, rp - 1)
        dual_pivot_quicksort(arr, rp + 1, high)
    return arr


def dual_pivot_partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    left_pivot = arr[low]
    right_pivot = arr[high]
    i = low + 1
    lt = low + 1
    gt = high - 1
    while i <= gt:
        if arr[i] < left_pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
        elif arr[i] > right_pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
            i -= 1
        i += 1
    lt -= 1
    gt += 1
    arr[low], arr[lt] = arr[lt], arr[low]
    arr[high], arr[gt] = arr[gt], arr[high]
    return lt, gt
# Utility: check if array is sorted

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def benchmark_sort(fn, size=1000):
    import random, time
    data = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    fn(data)
    return time.perf_counter() - start
