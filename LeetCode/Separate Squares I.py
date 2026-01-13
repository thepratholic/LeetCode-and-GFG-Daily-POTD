from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(mid_y):
            bot_area = 0.0

            for x, y, l in squares:
                bot_y = y
                top_y = y + l

                if mid_y >= top_y:
                    bot_area += (l * l)
                
                elif mid_y >= bot_y:
                    bot_area += (mid_y - bot_y) * l

            return bot_area >= total / 2.0

        low = float('inf')
        high = float('-inf')
        total = 0.0

        for _, y, l in squares:
            total += l * l
            low = min(low, y)
            high = max(high, y + l)

        result_y = 0.0

        while high - low > 1e-5:
            mid_y = low + (high - low) / 2.0
            result_y = mid_y

            if check(mid_y):
                high = mid_y
            else:
                low = mid_y

        return result_y