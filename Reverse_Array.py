"""
i) Iterative way
start =0 and end=end-1
swap the first value with the end value and increase start with 1 and decrease end with -1
start=start+1 and end=end-1
Time complexity will be O(n)
"""

def reverse_list(A,start,end):
    while start <=end:
        A[start], A[end] = A[end], A[start]
        start = start+1
        end = end-1

A = [1, 2, 3, 4, 5, 6]
print(A)
reverse_list(A, 0, 5)
print("Reversed list is")
print(A)

"""
ii)recursive Approach
start =0 and end =end -1
recursively call the function every time
complexity O(n)
"""
def reverse_list2(B,start,end):
    while start <=end:
        B[start], B[end] = B[end], B[start]
        reverse_list2(B, start+1, end-1)

B = [1, 2, 3, 4, 5, 6]
print(B)
reverse_list2(B, 0, 5)
print("Reversed list is")
print(B)

"""
iii) String slicing in Python
"""
# Driver function to test above function
C = [1, 2, 3, 4, 5, 6]
print(C)
print("Reversed list is")
print(C[::-1])




