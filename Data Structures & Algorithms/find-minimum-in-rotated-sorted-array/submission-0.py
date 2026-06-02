class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = 9999
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            smallest = min(nums[mid], smallest)

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return smallest

        