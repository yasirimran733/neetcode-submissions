class Solution:
    def plusOne(self, digits):
        length = len(digits)-1
        for i in range(length,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0,1)
        return digits        


        



        