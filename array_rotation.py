def reverse_array(arr, start, end):

    while start < end :
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1


def rotate_array(arr, d):
    if d == 0:
        return
    n = len(arr)

    d = d%n

    reverse_array(arr, 0 , d-1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)

def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i],end=' ')


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2

rotate_array(arr, d)  # Rotate array by 2
printArray(arr)