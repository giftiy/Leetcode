class Solution:
    def makeFancyString(self, s: str) -> str:
        # If size of string is less than 3, return it.
        if len(s) < 3:
            return s

        # Convert the string to a list for mutability.
        s_list = list(s)
        j = 2

        # Iterate through the string from index 2.
        for i in range(2, len(s)):
            # If the current character is not equal to the previously inserted
            # two characters, then we can add it to the result.
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        # Resize the list to the number of valid characters and join it back into a string.
        return "".join(s_list[:j])