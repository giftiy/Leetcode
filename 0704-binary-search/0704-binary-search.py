class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if the target is at mid
            if nums[mid] == target:
                return mid
            # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1
            # If target is smaller, ignore right half
            else:
                right = mid - 1
        
        # Target was not found
        return -1