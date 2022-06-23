def majority_element(arr, size, key):
    if (arr[size//2]) == key:
        return True
    else:
        return  False


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 3, 3, 10]
    n = len(arr)
    x = 3
    if (majority_element(arr, n, x)):
        print(x, " appears more than ",
              n // 2, " times in arr[]")
    else:
        print(x, " does not appear more than",
              n // 2, " times in arr[]")

