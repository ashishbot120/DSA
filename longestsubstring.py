def max_unique_length(str):
    seen={}
    start=0
    max_len=0
    for i in range(len(str)):
        char = str[i]
        if char in seen:
            start = max(start,seen[char]+1)
        max_len= max(max_len,i-start+1)
        seen[char] = i
    return max_len
# Example usage:
input_str = "abcabcbb"
result = max_unique_length(input_str)
print(result)
# Output: 3
#time complexity: O(n) where n is the length of the string
#space complexity: O(min(m,n)) where m is the size of the character set and n is the length of the string