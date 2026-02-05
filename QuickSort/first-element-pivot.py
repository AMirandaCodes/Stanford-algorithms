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
        pivot_index = partition(array, low, high)
        # Left recursive call
        comparisons += quicksort(array, low, pivot_index - 1)
        # Right recursive call
        comparisons += quicksort(array, pivot_index + 1, high)

        return comparisons
    
    # Base case: low >= high
    return 0

if __name__ == "__main__":
    file = 'QuickSort.txt'
    with open(file) as f:
        arr = [int(line.rstrip()) for line in f]
    comparisons = quicksort(arr)
    # print(arr) # Uncomment this line if you want the sorted array printed
    print("Total comparisons (via Quicksort, first element as pivot):" , comparisons)