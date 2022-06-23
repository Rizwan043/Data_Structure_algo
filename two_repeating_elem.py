def repeating_elem(arr, size):
    m = {}

    for i in range(size):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    for key in m:
        if m[key] == 2:
            print(key)


arr = [4, 2, 4, 5, 2, 3, 1]
size = len(arr)
repeating_elem(arr, size)