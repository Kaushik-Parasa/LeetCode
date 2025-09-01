#find the sum of largest and least in the array
def sum_of_largest_and_least(arr):
    if not arr:
        return 0
    least = min(arr)
    largest = max(arr)
    return least + largest

list = [2,4, 5, 7, 8, 1, 9]
print(sum_of_largest_and_least(list))