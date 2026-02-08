def search_in_matrix(matrix,target):
    if len(matrix)==0: return False
    columns = len(matrix[0])
    rows = len(matrix)
    #Binary search to identify the relevant row
    top = 0
    bottom = rows-1
    while(top<=bottom):
        middle = (top + bottom)//2
        if target < matrix[middle][0]: bottom = middle -1
        elif target > matrix[middle][columns-1]: top = middle+1
        else: break
    if top > bottom: return False
    left =0
    right = columns -1
    while(left<=right):
        middle_val = (left+right)//2
        if target == matrix[middle][middle_val]:return True
        elif target < matrix[middle][middle_val]: right = middle_val-1
        else:left = middle_val+1
    return False

# Example usage:
input_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target_value = 3
result = search_in_matrix(input_matrix, target_value)
print(result)
# Output: True
# time complexity: O(log m + log n) where m is the number of rows and n is the number of columns in the matrix
# space complexity: O(1) as it uses constant space