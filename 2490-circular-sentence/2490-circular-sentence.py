class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Use the split function to store the words in a list.
        words = sentence.split(" ")
        n = len(words)

        # Start comparing from the last character of the last word.
        last = words[n - 1][-1]

        for i in range(n):
            # If this character is not equal to the first character of current word, return
            # false.
            if words[i][0] != last:
                return False
            last = words[i][-1]

        return True