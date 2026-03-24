import heapq

def median_maintenance(file):
    # Max-heap (negative values)
    lower = []
    # Min-heap
    upper = []

    # Sum of all medians
    median_sum = 0

    with open(file) as f:
        for line in f:
            x = int(line.strip())

            # Insert into correct heap
            if not lower or x <= -lower[0]:
                heapq.heappush(lower, -x)
            else:
                heapq.heappush(upper, x)

            # Rebalance heaps
            if len(lower) > len(upper) + 1:
                moved = -heapq.heappop(lower)
                heapq.heappush(upper, moved)
            elif len(upper) > len(lower):
                moved = heapq.heappop(upper)
                heapq.heappush(lower, -moved)

            # Get median (highest value from lower)
            median = -lower[0]

            # Add to running total
            median_sum += median
    
    # Modulo 10000 of sum (as instructed)
    return median_sum % 10000

if __name__ == "__main__":
    total = median_maintenance("Median.txt")
    print(total)
