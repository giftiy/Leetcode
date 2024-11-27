class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        intersection = []
        
        for num in nums2:
            if counts[num] > 0:
                intersection.append(num)
                counts[num] -= 1
        
        return intersection