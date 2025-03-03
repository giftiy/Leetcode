class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        return less + equal + greater
