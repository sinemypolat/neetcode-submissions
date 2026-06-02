class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        all_indices = set(list(range(length)))
        
        result = []
        for i, num in enumerate(nums):
            others = all_indices - set([i])
            prod = 1
            for other in others:
                prod *= nums[other]
            result.append(prod)
        return result


