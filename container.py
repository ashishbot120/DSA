def max_area(array):
    if len(array) <=1:
        return 0
    
    max_area=0
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            area=min(array[i],array[j])*(j-i)
            max_area=max(max_area,area)
    return max_area

heights=[1,8,6,2,5,4,8,3,7]
print(max_area(heights))  #output: 49
#time complexity: O(n^2) where n is the length of the array space complexity: O(1)

def max_area_optimal(array):
    if len(array) <=1:
        return 0
    
    left=0
    right=len(array)-1
    max_area=0

    while left<right:
        area=min(array[left],array[right])*(right-left)
        max_area=max(max_area,area)

        if array[left]<array[right]:
            left+=1
        else:
            right-=1

    return max_area
heights=[1,8,6,2,5,4,8,3,7]
print(max_area_optimal(heights))  #output: 49
#time complexity: O(n) where n is the length of the array space complexity: O(1)