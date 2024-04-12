class NumArray:
    """
    https://www.youtube.com/watch?v=2pndAmo_sMA
    
    beats 66.70%
    """
    def __init__(self, nums: List[int]):
        self.prefix = [] # prefix sum, sum from first to current
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
        
        
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right] 
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum


class NumArrayV0(object):
    """
    Your NumArray object will be instantiated and called as such:
    obj = NumArray(nums)
    param_1 = obj.sumRange(i,j)

    beats 93.01%
    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]
