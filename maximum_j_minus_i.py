def maxIndexDiff(arr, size):
    for i in range(0, size-1):
        for j in range(size-1, -1, -1):
            if arr[i] < arr[j]:
                break
    print(f"[{arr[i]},{arr[j]}]")


arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxIndexDiff(arr, n)
