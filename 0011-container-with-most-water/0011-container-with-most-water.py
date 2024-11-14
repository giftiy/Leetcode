class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Initialize two pointers
        max_area = 0  # Variable to store the maximum area
        
        while left < right:
            # Calculate the area formed by the current left and right pointers
            width = right - left
            current_area = min(height[left], height[right]) * width
            
            # Update the maximum area if the current one is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
