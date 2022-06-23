def odd_number_time(arr, size):
    m = {}

    for i in range(size):
        if arr[i] in m :
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    count = 0

    for key in m:
        if(m[key]) % 2 !=0:
            count = 1
            print(key)
            break

arr = []
n = len(arr)

odd_number_time(arr, n)