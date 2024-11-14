class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            # Reversing the second half of the number
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # If the length of the number is odd, we can disregard the middle digit
        return x == reversed_half or x == reversed_half // 10
