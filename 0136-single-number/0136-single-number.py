class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR each element with result
        return result
