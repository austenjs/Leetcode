class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_amount = max(candies)
        bool_array = []
        for candy in candies:
            bool_array.append(candy + extraCandies >= max_amount)
        return bool_array