# Q56. Create a function to rotate a list left by k positions.

lst = [1, 2, 3, 4, 5, 6, 7]   # if k=3, ANS --> [4, 5, 6, 7, 1, 2, 3]
k = 3

def rotate_list_left(lst, k):
    n = len(lst)
    def reverse(start, end):  # reverse a list between a range
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
    
    reverse(0, n-1)     # reverse the whole list
    reverse(k+1, n-1)   # reverse last k elements
    reverse(0, k)       # reverse remaining elements

rotate_list_left(lst, k)
print(lst)



# rotate a list right by k positions.
lst2 = [1, 2, 3, 4, 5, 6, 7]   # if k=3, ANS --> [5, 6, 7, 1, 2, 3, 4]
k = 3

def rotate_list_right(lst2, k):
    n = len(lst2)
    def reverse(start, end):  # reverse a list between a range
        while start < end:
            lst2[start], lst2[end] = lst2[end], lst2[start]
            start += 1
            end -= 1
    
    reverse(0, n-1)    # reverse whole list
    reverse(0, k-1)    # reverse starting k elements
    reverse(k, n-1)    # reverse remaining elements

rotate_list_right(lst2, k)
print(lst2)

