def sum_pair(arr, x):
    size = len(arr)

    for i in range(size-1):
        for j in range(i+1,size):
            if arr[i] + arr[j] == x:
                print(f"The index pair of sum are [{arr[i]},{arr[j]}]")
                return 1
    return 0
if __name__ == '__main__':
    arr = [0, -1, 2, -3, 1]
    x = -2
    sum_pair(arr, x)


