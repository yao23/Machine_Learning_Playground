class Solution(object):
    # @param num, a list of integer
    # @return an integer
    # beats 77.49%
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        maxLen=0
        while nums:
            n=nums.pop()
            i=n+1
            l1=0
            l2=0
            while i in nums:
                nums.remove(i)
                i+=1
                l1+=1
            i=n-1
            while i in nums:
                nums.remove(i)
                i-=1
                l2+=1
            maxLen=max(maxLen,l1+l2+1)
        return maxLen