class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip leading/trailing spaces and split the string into words
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1]) if words else 0

    