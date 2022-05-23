class NumArray:

    def __init__(self, nums: List[int]):
        cumsum = [0]
        for i, num in enumerate(nums):
            cumsum.append(num + cumsum[i])
        self.cumsum = cumsum
        print(cumsum)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right + 1] - self.cumsum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)