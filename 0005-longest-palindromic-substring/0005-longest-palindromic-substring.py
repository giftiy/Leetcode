class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome found (excluding the last invalid indices)
            return s[left+1:right]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center at i)
            odd_palindrome = expand_around_center(i, i)
            # Check for even-length palindromes (center between i and i+1)
            even_palindrome = expand_around_center(i, i + 1)
            
            # Update the longest palindrome if necessary
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        
        return longest_palindrome
