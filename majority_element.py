def majority_element(arr, size):
    m = {}

    for i in range(size):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    count = 0
    for key in m:
        if m[key] > size/2:
            count = 1
            print(key)
            break
        else:
            if count == 0:
                print("no element found")



arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
size = len(arr)

majority_element(arr, size)