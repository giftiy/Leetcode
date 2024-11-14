class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num
