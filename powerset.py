def power_set(nums):
    result = []
    
    def backtrack(start_index, current_subset):
        result.append(current_subset.copy())
        
        for i in range(start_index, len(nums)):
            current_subset.append(nums[i])
            
            backtrack(i + 1, current_subset)
            
            current_subset.pop()
            
    backtrack(0, [])
    return result

# Example usage:
arr = [1, 2, 3]  
result = power_set(arr)
print(result)
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
#time complexity: O(n*2^n) where n is the length of the input list
#space complexity: O(n) for the recursion stack and O(2^n) for                         
# the output list storing all subsets