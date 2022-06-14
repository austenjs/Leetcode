class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        i = 0
        length = N
        while i < N:
            if nums[i] == val:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop()
                N = len(nums)
            else:
                i += 1
        return len(nums)