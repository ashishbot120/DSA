def insertion_sort(array):
    for i in range(1,len(array)):
        j=i-1
        temp = array[i]
        while j>=0 and array[j]>temp:
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp
    return array
# Example usage:
# input_array = [12, 11, 13, 5, 6]
# sorted_array = insertion_sort(input_array)
# print(sorted_array)
# Output: [5, 6, 11, 12, 13]
# time complexity: O(n^2) in the worst and average case, O(n) in the best case when the array is already sorted
# space complexity: O(1) as it is an in-place sorting algorithm
