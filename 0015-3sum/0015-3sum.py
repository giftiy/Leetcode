class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First, sort the array to handle duplicates and enable two-pointer technique
        nums.sort()
        result = []
        
        # Loop through the array, considering each element as the first element of the triplet
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element to avoid repeated triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set up two pointers for the other two elements
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # If we find a valid triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer to the right, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Move the right pointer to the left, skipping duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to continue searching
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # If the sum is too small, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is too large, move the right pointer to the left
                    right -= 1
        
        return result
