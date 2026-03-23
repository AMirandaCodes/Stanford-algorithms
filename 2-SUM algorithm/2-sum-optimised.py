import bisect

# Returns file as a list
def load_file(file):
    array = []
    with open(file) as f:
        for line in f:
            array.append(int(line))
    return array

# 2-SUM: Restrict valid y range
def two_sum(array):
    nums = sorted(set(array))
    valid_targets = set()

    for i in range(len(nums)):
        x = nums[i]

        # Gives the valid range for y
        # −10,000 ≤ x+y ≤ 10,000
        low = -10000 - x
        high = 10000 - x

        # Where do numbers ≥ low start
        left = bisect.bisect_left(nums, low)
        # Where do numbers ≤ high end
        right = bisect.bisect_right(nums, high)

        # Loops over valid range only
        for j in range(left, right):
            y = nums[j]
            # Distinct numbers and stores target
            if x != y:
                valid_targets.add(x + y)
    
    return len(valid_targets)

if __name__ == "__main__":
    array = load_file("algo1-programming_prob-2sum.txt")
    total = two_sum(array)
    print(total)