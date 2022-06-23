def array_prod(arr , size):

    left = [0]*size
    right = [0]*size

    prod = [0]*size

    left[0] = 1
    right[size-1] = 1

    for i in range(1, size):
        left[i] = arr[i-1] * left[i-1]
    print(left)

    for j in range(size-2, -1, -1):
        right[j] = arr[j+1] * right[j+1]
    print(right)

    for i in range(0, size):
        prod[i] = left[i] * right[i]

    print("constructed array", prod)


arr = [10, 3, 5, 6, 2]
n = len(arr)
array_prod(arr, n)