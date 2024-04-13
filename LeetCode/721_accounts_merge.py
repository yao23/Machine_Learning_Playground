class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    """
    https://www.youtube.com/watch?v=6st4IxEF-90

    beats 71.52%
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccnt = {} # email => accountId
        for i, accnt in enumerate(accounts):
            for email in accnt[1:]: # emails starting from index 1
                if email in emailToAccnt:
                    uf.union(i, emailToAccnt[email])
                else:
                    emailToAccnt[email] = i

        accntToEmails = defaultdict(list) # accounId => email list
        for email, i in emailToAccnt.items():
            leader = uf.find(i) # find parent of account i
            accntToEmails[leader].append(email)

        res = []
        for i, emails in accntToEmails.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails)) # construct name and emails as result
        return res
