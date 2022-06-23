def surrogate_key(arr, size):

    count = 0
    for i in range(0, size):
        if arr[i] == 0:
            count += 1

    for i in range(0,count):
        arr[i] = 0

    for i in range(count, size-1):
        arr[i] = 1


arr = [0, 1, 0, 1, 1, 1]
n = len(arr)

surrogate_key(arr, n)
print(arr)
