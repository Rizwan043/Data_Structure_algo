def array_leader(arr, size):

    max_element = arr[size-1]
    print(max_element)
    for i in range(size-2 , -1, -1):
        if arr[i] > max_element:
            print(arr[i])
            max_element = arr[i]

arr = [16, 17, 4, 3, 5, 2]
size = len(arr)

array_leader(arr, size)
