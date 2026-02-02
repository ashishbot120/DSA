
def group_anagrams(strings):
    if len(strings) == 0:
        return []
    sorted_string = [''.join(sorted(i)) for i in strings]
    hash = {}
    for i in range(len(sorted_string)):
        if sorted_string[i] in hash:
            hash[sorted_string[i]].append(strings[i])
        else:
            hash[sorted_string[i]] = [strings[i]]
    return list(hash.values())
# Example usage:
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_strings)
print(result)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
#time complexity: O(n*klogk) where n is the number of strings and k is the maximum length of a string
#space complexity: O(n) where n is the number of strings
