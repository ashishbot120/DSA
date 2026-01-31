def sorted_squared(array):
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[i] = array[i] * array[i]
    new_array.sort()
    return new_array
# Example usage:
# input_array = [-4, -1, 0, 3, 10]
# output_array = sorted_squared(input_array)
# print(output_array)
# Output: [0, 1, 9, 16, 100]
#time complexity: O(n log n) due to the sorting step

#space complexity: O(n) for the new array
def sorted_squared_optimized(array):
    i= 0
    j = len(array) - 1
    new_array = [0] * len(array)
    for k in reversed(range(len(array))):
        sq_i = array[i]**2
        sq_j = array[j]** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array   