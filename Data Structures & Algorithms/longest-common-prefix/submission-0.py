class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(1,len(strs)):
            j = 0
            while j < min(len(strs[i]),len(prefix)):
                if strs[i][j] == prefix[j]:
                    j += 1
                else:
                    break
            prefix = prefix[:j]
        return prefix