class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        N = len(nums)
        left, right = 0, N - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = right = mid
                break
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        
        if left >= N or right >= N or nums[left] != target or nums[right] != target:
            return ans
        
        # Left boundary
        left_boundary_l, left_boundary_r = 0, left
        while left_boundary_l + 1< left_boundary_r:
            left_mid = left_boundary_l + (left_boundary_r - left_boundary_l) // 2
            if nums[left_mid] == target:
                left_boundary_r = left_mid
            else:
                left_boundary_l += 1
        
        if nums[left_boundary_l] == target:
            left_boundary = left_boundary_l
        else:
            left_boundary = left_boundary_r
        
        # Right boundary
        right_boundary_l, right_boundary_r = right, N - 1
        while right_boundary_l + 1< right_boundary_r:
            right_mid = right_boundary_l + (right_boundary_r - right_boundary_l) // 2
            if nums[right_mid] == target:
                right_boundary_l = right_mid
            else:
                right_boundary_r -= 1
        
        if nums[right_boundary_r] == target:
            right_boundary = right_boundary_r
        else:
            right_boundary = right_boundary_l
        return [left_boundary, right_boundary]