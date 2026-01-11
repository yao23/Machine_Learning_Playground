class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p1 = 1 # product without zero
        p2 = 1 # product with zero
        c = 0 # count of zero
        
        for n in nums:
            if n == 0:
                c += 1
                p2 = 0
            else:
                p1 *= n
        
        if p2 == 1:
            p2 = p1

        for n in nums:
            if n == 0:
                if c == 1:
                    res.append(p1)
                else:
                    res.append(0)
            else:
                res.append(p2 // n)

        return res
