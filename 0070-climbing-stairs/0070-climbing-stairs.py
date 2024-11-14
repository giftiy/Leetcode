class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        
        # Initialize the first two steps
        prev1, prev2 = 1, 1
        
        # Calculate the number of ways for each step from 2 to n
        for i in range(2, n + 1):
            current = prev1 + prev2  # The number of ways to reach the current step
            prev2 = prev1  # Update prev2 for the next iteration
            prev1 = current  # Update prev1 for the next iteration
        
        return prev1  # prev1 holds the number of ways to reach step n

    