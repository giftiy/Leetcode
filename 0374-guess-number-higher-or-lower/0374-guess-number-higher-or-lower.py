class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)  # Guess the middle number
            
            if result == 0:
                return mid  # Correct guess
            elif result == -1:
                high = mid - 1  # Guess too high, adjust the range
            else:
                low = mid + 1  # Guess too low, adjust the range
