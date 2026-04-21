class Solution:
    def isAnagram(self, s, t):
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1
        for char in t:    
            count[char] = count.get(char,0) - 1
            if not count[char]:
                del count[char]
        return count == {}  