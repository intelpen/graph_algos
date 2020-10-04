"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) <= 1:
            return 0
        minimum, maximum, delta = prices[0], None, 0
        max_delta = 0
        for element in prices[1:]:
            if element < minimum:
                minimum = element
                maximum = None
                delta = 0
            elif element > minimum:
                if maximum is None or element > maximum:
                    maximum = element
                    delta = maximum - minimum
                    if delta > max_delta:
                        max_delta = delta
        return max_delta


if __name__ == "__main__":
    prices_list = [[1, 2], [7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 2, 1]]
    solution = Solution()
    for prices in prices_list:
        print(f"{prices} : {solution.maxProfit(prices)}")

