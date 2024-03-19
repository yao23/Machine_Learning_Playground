class StockSpanner:
    """
    https://www.youtube.com/watch?v=slYh0ZNEqSw&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=12
    
    beats 29.17%
    """
    def __init__(self):
        self.stack = [] # pair [price, span]

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
