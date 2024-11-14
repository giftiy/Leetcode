class Solution:
    def romanToInt(self, s: str) -> int:
        # Map Roman numerals to integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Iterate over the string, adding values to the total
        for i in range(n):
            # If we're not at the last character, and the current character
            # represents a smaller value than the next character, we subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total
