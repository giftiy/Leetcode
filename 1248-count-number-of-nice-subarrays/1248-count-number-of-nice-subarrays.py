class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(k: int) -> int:
            """Helper function to count subarrays with at most k odd numbers."""
            count = 0
            left = 0
            odd_count = 0
            
            for right in range(len(nums)):
                # If the current number is odd, increase the odd count
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                # If we have more than k odd numbers, move the left pointer
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                # Add the number of subarrays ending at right with at most k odd numbers
                count += right - left + 1
            
            return count
        
        # The number of subarrays with exactly k odd numbers is the difference
        # between the number of subarrays with at most k odd numbers and at most k-1 odd numbers.
        return atMostK(k) - atMostK(k - 1)