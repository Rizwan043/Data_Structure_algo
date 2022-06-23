
def k_element(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[: mid]
        r = arr[mid:]
        #sorting first half
        k_element(l)
        #sorting second half
        k_element(r)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i = i+1
            else:
                arr[k] = r[j]
                j = j+1
            k = k+1

        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i = i+1
            k = k+1
        while j < len(r):
            arr[k] = r[j]
            j = j+1
            k = k+1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    k = 3
    print("Given array is", end="\n")
    printList(arr)
    k_element(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    print(arr[k-1])


