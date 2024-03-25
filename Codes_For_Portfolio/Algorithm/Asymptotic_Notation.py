#Big Θ(1) - Constant Time
#this function return the first element of the list
def get_first_element(lst):
    return lst[0]

#Big Θ(n) - Linear Time
#this function search for the maximum value in the list
def find_maximum(lst):
    max_value = lst[0]
    for value in lst:
        if value > max_value:
            max_value = value
    return max_value

#Big Θ(n^2) - Quadratic Time
#this function print all the pairs of the list
def print_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)
            
#Big O(logN) - Logarithmic Time
#This function implements binary search, an algorithm that continuously divides the input in half until it finds the target value              
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Big O(nlogn) - Linearithmic Time
#This function implements merge sort, an algorithm that divides the input in half and sorts each half before merging them back together
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged



#test the functions
lst = [1, 2, 3, 4, 5]
print(get_first_element(lst))
print(find_maximum(lst))
print_pairs(lst)
print(merge(lst, lst))





