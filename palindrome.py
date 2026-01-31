#SOLUTION 1
# In Python Strings are immutable.
def is_palindrome(str):
    new_str = ''
    for i in reversed(range(len(str))):
        new_str += str[i]
    if str == new_str:
        return True
    return False

#time complexity: O(n^2) due to string concatenation in a loop
#space complexity: O(n) for the new string

#Second Solution
def is_palindrome(str):
    new_array = []
    for i in reversed(range(len(str))):
        new_array.append(str[i])
 
    if(''.join(new_array) == str):
        return True
    return False

#time complexity: O(n)
#space complexity: O(n) for the new array

#Third Solution
def is_palindrome(str):
    i = 0
    j = len(str)-1
    while i<j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

#time complexity: O(n)
#space complexity: O(1) 