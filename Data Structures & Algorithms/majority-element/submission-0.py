class Solution:
    def majorityElement(self, nums):
        values = {}
        for num in nums:
            values[num] = values.get(num,0) + 1
        for element,count in values.items():
            if count >= len(nums)/2:
                return element 