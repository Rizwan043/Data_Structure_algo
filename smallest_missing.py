def missing_elem(arr, start, end):
    if start > end :
        return start
    if start != arr[start]:
        return start

    mid = int((start + end) / 2)

    if arr[mid] == mid:
        return missing_elem(arr, mid+1, end)
    return missing_elem(arr, start, mid)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
n = len(arr)
print("Smallest missing element is",
      missing_elem(arr, 0, n-1))
