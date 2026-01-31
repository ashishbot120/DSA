# Find the first non-repeating character in a string
# brute-force approach
def non_repeating_char(str):
    for i in range(len(str)):
        repeat = False
        for j in range(len(str)):
            if i!=j and str[i]==str[j]:
                repeat = True
        if repeat == False:
            return i
    return None

# time complexity: O(n^2)
# space complexity: O(1)
print(non_repeating_char("aabbccdeef"))  # Output: 6 (index of 'd')
print(non_repeating_char("aabbcc"))      # Output: None (no non-repeating character)

# optimized approach using a dictionary
def non_repeating_char_optimized(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for i in range(len(str)):
        if char_count[str[i]] == 1:
            return i
    return None
# time complexity: O(n)
# space complexity: O(1) - since the character set is fixed (e.g., ASCII)
print(non_repeating_char_optimized("aabbccdeef"))  # Output: 6 (index of 'd')
print(non_repeating_char_optimized("aabbcc"))      # Output: None (no non-repeating character)
