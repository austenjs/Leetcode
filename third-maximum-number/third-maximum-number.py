class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = -2147483649
        
        # First max
        for num in nums:
            if num > first_max:
                first_max = num
        
        # Second max
        for num in nums:
            if num > second_max and num != first_max:
                second_max = num

        ## All is same number
        if second_max == third_max:
            return first_max

        # Third max
        for num in nums:
            if num > third_max and num != second_max and num != first_max:
                third_max = num
        
        ## Doesnt found third max
        if third_max == -2147483649:
            return first_max

        return third_max