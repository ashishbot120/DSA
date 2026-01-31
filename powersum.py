def power_sum(array,power=1):
    sum=0
    for i in array:
        if type(i)==list:
            sum = sum + power_sum(i,power+1)
        else:
            sum = sum + i
    return sum**power

# Example usage:
arr = [1, 2, [3, 4], [5, [6]]]
result = power_sum(arr, 2)
print(result)
# Output: 3025
#time complexity: O(n) where n is the total number of elements including nested ones
#space complexity: O(d) where d is the maximum depth of nesting in the array