class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = prices[:]
        stack = []  

        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                _, j = stack.pop()
                result[j] -= price
            stack.append((price, i))

        return result