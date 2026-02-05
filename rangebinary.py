
#Iterative Solution
def find_left_extreme(array,target):
    left = 0
    right = len(array)-1
    while(left<=right):
        middle = (left + right)//2
        if array[middle]==target:
            if middle == 0: return 0
            elif array[middle -1 ] == target:
                right = middle -1
            else: return middle
        elif target< array[middle] : right = middle -1
        else: left = middle +1
    return -1
 
def find_right_extreme(array,target):
    left = 0
    right = len(array)-1
    while(left<=right):
        middle = (left+right)//2
        if array[middle] == target:
            if middle == len(array)-1 : return middle
            elif array[middle+1] == target:
                left = middle+1
            else: return middle
        elif target<array[middle]: right = middle-1
        else: left = middle+1
    return -1
 
 
def search_for_range(array,target):
    left_extreme = find_left_extreme(array,target)
    right_extreme = find_right_extreme(array,target)
    return [left_extreme,right_extreme]

# Example usage:
input_array = [5,7,7,8,8,10]
target_value = 8
result = search_for_range(input_array, target_value)
print(result)
# Output: [3, 4]
# time complexity: O(log n) where n is the number of elements in the array
# space complexity: O(1) as it uses constant space
