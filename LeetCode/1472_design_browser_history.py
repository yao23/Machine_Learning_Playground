class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    """
    https://www.youtube.com/watch?v=i1G-kKnBu8k
    
    beats 49.78%
    """
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

class BrowserHistoryV1:
    """
    https://www.youtube.com/watch?v=i1G-kKnBu8k
    
    beats 90.65%
    """
    def __init__(self, homepage: str):
        self.i = 0 # cur index
        self.len = 1 # cur array length
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2: # forward in tail
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1 # zero based index, so add one 

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0) # left starting from index zero
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)  # right ending to index self.len - 1
        return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
