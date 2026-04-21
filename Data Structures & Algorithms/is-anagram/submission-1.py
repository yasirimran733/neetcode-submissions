
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False;
        countS = {}
        countT = {}

        for char in s:
            countS[char] = countS.get(char,0) + 1
        for char in t:    
            countT[char] = countT.get(char,0) + 1
        for char in s:
            if countS[char] != countT.get(char,0):
                return False   
        return True 