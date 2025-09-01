# find the second largest number in the array
#brute force method
def second_largest(arr):
    sorted_arr = sorted(arr, reverse=True)
    if len(sorted_arr) < 2:
        raise ValueError("Array must contain at least two distinct elements.")
    return sorted_arr[1]

list = [2,4, 5, 7, 8, 1, 9]
print(second_largest(list))
