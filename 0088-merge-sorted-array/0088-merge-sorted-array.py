class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Start from the end of nums1 and nums2
        i = m - 1  # Last initialized element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last index of nums1 (total length)

        # Merge nums1 and nums2 from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
