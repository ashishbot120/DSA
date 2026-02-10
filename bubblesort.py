def bubble_sort(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                sorted = False
        counter += 1
    return array
# Example usage:
# input_array = [64, 34, 25, 12, 22, 11, 90]
# sorted_array = bubble_sort(input_array)
# print(sorted_array)   
# Output: [11, 12, 22, 25, 34, 64, 90]
#time complexity: O(n^2) in the worst and average case, O(n) in the best case when the array is already sorted
#space complexity: O(1) as it is an in-place sorting algorithm