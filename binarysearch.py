def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target: 
        return binary_search(arr, target, mid + 1, right)
    else:               
        return binary_search(arr, target, left, mid - 1)    
# Example usage:
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result = binary_search(input_array, target_value, 0, len(input_array) - 1)
print(result)
# Output: 4
#time complexity: O(log n) where n is the number of elements in the array
#space complexity: O(log n) due to recursive stack space

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Example usage:
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 7
result = binary_search_iterative(input_array, target_value)
print(result)
# Output: 6
#time complexity: O(log n) where n is the number of elements in the array
#space complexity: O(1) as it uses constant space
