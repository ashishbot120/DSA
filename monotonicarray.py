def monotonic_array(array):
    # Edge cases (though the loop below handles these naturally, 
    # keeping them is fine for clarity)
    if len(array) <= 1:
        return True

    # Assume both are true to start
    is_non_decreasing = True
    is_non_increasing = True

    # Loop through the array up to the second to last element
    for i in range(len(array) - 1):
        curr_num = array[i]
        next_num = array[i+1]

        # If current is greater than next, it can't be non-decreasing
        if curr_num > next_num:
            is_non_decreasing = False
        
        # If current is less than next, it can't be non-increasing
        if curr_num < next_num:
            is_non_increasing = False

    # Return True if it is EITHER entirely increasing OR entirely decreasing
    return is_non_decreasing or is_non_increasing


#first tried to make by myself then took little help of the ai 
#time complexity: O(n) where n is the length of the array