def partition(array, low, high):
    pivot = array[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        comparisons = high - low

        # Correct middle index
        mid = low + (high - low) // 2

        # Median-of-three by value
        candidates = [
            (array[low], low),
            (array[mid], mid),
            (array[high], high)
        ]
        candidates.sort(key=lambda x: x[0])
        median_index = candidates[1][1]

        # Swap median into first position
        array[low], array[median_index] = array[median_index], array[low]

        pivot_index = partition(array, low, high)
        comparisons += quicksort(array, low, pivot_index - 1)
        comparisons += quicksort(array, pivot_index + 1, high)

        return comparisons

    return 0


if __name__ == "__main__":
    with open("QuickSort.txt") as f:
        arr = [int(line.rstrip()) for line in f]

    comparisons = quicksort(arr)
    print("Total comparisons (median-of-three):", comparisons)


"""
def partition (array, low, high):
    pivot = array[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[low], array[i-1] = array[i-1], array[low]
    return i - 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        comparisons = high - low

        # Get the median-of-three
        middle = low + (high - low) // 2
        candidates = [array[low], array[middle], array[high]]
        candidates.sort()

        median = candidates[1]

        #comparisons = high - median + 1
        #comparisons += median - low

        # Swap median with first
        array[low], array[median] = array[median], array[low]

        pivot_index = partition(array, low, high)
        comparisons += quicksort(array, low, pivot_index - 1)
        comparisons += quicksort(array, pivot_index + 1, high)

        return comparisons
    
    # Base case: low >= high
    return 0

if __name__ == '__main__':
    file = 'QuickSort.txt'
    with open(file) as f:
        arr = [int(line.rstrip()) for line in f]
    comparisons = quicksort(arr)
    print(arr) # Uncomment this line if you want the sorted array printed
    print("Total comparisons (via Quicksort, median-of-three as pivot):", comparisons)
"""