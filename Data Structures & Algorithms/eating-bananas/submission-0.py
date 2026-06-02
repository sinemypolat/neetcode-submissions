class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ordered_piles = sorted(piles)
        low = 1
        high = max(piles)

        answer = high

        while low <= high:
            mid = (low + high) // 2
            
            total_time = 0
            
            for p in piles:
                total_time += math.ceil(float(p) / mid)
            if total_time <= h:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer



        