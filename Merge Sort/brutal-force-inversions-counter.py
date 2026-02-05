def inversionCount(arr):
    
    n = len(arr) 
    invCount = 0  

    for i in range(n - 1):
        for j in range(i + 1, n):
          
            # If the current element is greater than the next,
            # increment the count
            if arr[i] > arr[j]:
                invCount += 1
            
    return invCount  

if __name__ == "__main__":
    file = 'ReversedArray.txt'
    arr = []
    with open(file) as f:
        arr = [int(line.rstrip()) for line in f]
    print("Number of inversions: " + str(inversionCount(arr)))