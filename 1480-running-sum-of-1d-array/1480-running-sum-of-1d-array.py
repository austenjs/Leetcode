class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            if len(output):
                output.append(num + output[-1])
            else:
                output.append(num)
        return output