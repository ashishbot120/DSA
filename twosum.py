#Solution 1, Brute force
def two_sum(array,target):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                return [i,j]
    return []
 


#Solution 2
#Time Complexity O(n), Space Complexity O(n)
def two_sum(array,target):
    num_available = {}
    for i in range(len(array)):
        needed_val = target - array[i]
        if needed_val in num_available:
            return [i,num_available[needed_val]]
        else:
            num_available[array[i]]=i
    return []  
