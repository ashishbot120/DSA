class Solution(object):
    def isomorphic_strings(self, s, t):
        if len(s) != len(t):
            return False
    
        hash_s,hash_t = {},{}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s not in hash_s:
                hash_s[char_s] = char_t
            if char_t not in hash_t:
                hash_t[char_t] = char_s
            if hash_s[char_s] != char_t or hash_t[char_t] != char_s:
                return False
        return True
    
# Example usage:
sol = Solution()    
s = "egg"
t = "add"
print(sol.isomorphic_strings(s, t))
# Output: True
#time complexity: O(n) where n is the length of the strings
#space complexity: O(1) since the hash maps will at most store 26 characters if we consider only lowercase letters