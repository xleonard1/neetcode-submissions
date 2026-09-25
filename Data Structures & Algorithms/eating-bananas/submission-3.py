class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            current_speed = (left + right) // 2

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / current_speed)

            if total_hours <= h:
                res = current_speed
                right = current_speed - 1
            else:
                left = current_speed + 1
            
        return res
                
                    