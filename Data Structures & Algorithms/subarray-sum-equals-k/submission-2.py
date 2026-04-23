class Solution:
    def subarraySum(self, nums, k):
        prefixSum = [0] * (len(nums) + 1)

        for i in range(1,len(nums)+1):
            prefixSum[i] = prefixSum[i-1]+nums[i-1]

        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(prefixSum[j+1] - prefixSum[i] == k):
                    count += 1    

        return count 