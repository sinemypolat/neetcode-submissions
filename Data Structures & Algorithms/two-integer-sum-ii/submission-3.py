class Solution:
    # O(nlogn)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    # O(n)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # mp = defaultdict(int)
        # for i in range(len(numbers)):
        #     tmp = target - numbers[i]
        #     if mp[tmp]:
        #         return [mp[tmp], i + 1]
        #     mp[numbers[i]] = i + 1
        # return []