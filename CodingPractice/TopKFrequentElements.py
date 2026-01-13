class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) +1

        tmp = []
        for num, cnt in count.items():
            tmp.append([cnt, num])
        tmp.sort()

        res = []
        while len(res) < k:
            res.append(tmp.pop()[1])
        
        return res
