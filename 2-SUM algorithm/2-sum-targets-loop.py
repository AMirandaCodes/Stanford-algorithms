# Returns file as a list
def load_file(file):
    array = []
    with open(file) as f:
        for line in f:
            array.append(int(line))
    return array

# 2-SUM: Loop over all given targets
def twoSums_counter(array, targets):
    numbers = set(array)
    valid_targets = set()

    for x in numbers:
        for t in targets:
            y = t - x
            if y != x and y in numbers:
                valid_targets.add(t)

    return len(valid_targets)

if __name__ == "__main__":
    array = load_file("algo1-programming_prob-2sum.txt")
    targets = list(range(-10000, 10001))
    total = twoSums_counter(array, targets)
    print(total)