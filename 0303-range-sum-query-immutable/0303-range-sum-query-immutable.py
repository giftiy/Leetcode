class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix =[]
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)