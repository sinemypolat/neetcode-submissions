class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [item for items in matrix for item in items]
        left = 0
        right = len(flat) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if target == flat[mid]:
                return True
            elif target < flat[mid]:
                right = mid - 1
            elif target > flat[mid]:
                left = mid + 1
            else:
                return True
        return False