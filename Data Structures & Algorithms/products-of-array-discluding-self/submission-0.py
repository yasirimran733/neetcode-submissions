class Solution:
    def productExceptSelf(self, nums):
        # Product from left side of i 
        prefix = [1] * len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        # Product from right of i
        suffix = [1] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        result = [prefix[i]*suffix[i] for i in range(len(nums))]
        return result   