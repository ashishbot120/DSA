def all_permutations(nums):
    permutations=[]
    if len(nums)==0: return [[]]
    def helper(nums,i):
        if i==len(nums)-1:
            permutations.append(nums.copy())
            return
        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            helper(nums,i+1)
            nums[i],nums[j]=nums[j],nums[i]
    helper(nums,0)
    return permutations

# Example usage:
arr = [1, 2, 3]
result = all_permutations(arr)
print(result)
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
#time complexity: O(n*n!) where n is the length of the input list
#space complexity: O(n) for the recursion stack and the output list 