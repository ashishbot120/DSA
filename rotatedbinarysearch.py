def search_rotated_sorted_array(nums,target):
    left = 0
    right = len(nums)- 1
    
    
    while (left <= right):
        middle = (left+right)//2
        if nums[middle] == target: 
            return middle
        if nums[left]<= nums[middle]:
            if target >= nums[left] and target < nums[middle] :
                right = middle -1
            else:
                left = middle + 1
        else:
            if target <= nums[right] and target > nums[middle]:
                left = middle +1 
            else:
                right = middle -1
    return -1    
            
# Example usage:
input_array = [4,5,6,7,0,1,2]   
target_value = 0    
result = search_rotated_sorted_array(input_array, target_value)
print(result)
# Output: 4
# time complexity: O(log n) where n is the number of elements in the array
# space complexity: O(1) as it uses constant space   
        
        
    
    