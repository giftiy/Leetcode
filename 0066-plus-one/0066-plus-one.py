class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start from the last digit
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just add 1 and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and continue to the next left digit
            digits[i] = 0
        
        # If we exit the loop, all digits were 9, so we need an additional leading 1
        return [1] + digits
