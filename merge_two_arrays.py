def merge_two(a, b):
    len_a = len(a)
    len_b = len(b)
    arr = [None] * (len_a + len_b)
    i=j=k=0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j +=1
        k +=1

    while i < len_a:
            arr[k] = a[i]
            i += 1
            k +=1
    while j < len_b:
            arr[k] = b[j]
            j +=1
            k +=1

    print(arr)

a = [2, 8, 11, 20]
b = [5, 7, 9, 25]

merge_two(a, b)
