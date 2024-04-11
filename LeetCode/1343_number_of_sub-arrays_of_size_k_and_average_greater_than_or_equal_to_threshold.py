class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        https://www.youtube.com/watch?v=D8B4tKxMTnY

        beats 98.41%
        """
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res

    def numOfSubarraysV0(self, arr: List[int], k: int, threshold: int) -> int:
        """
        beats 94.42%
        """
        res = 0
        curSum = sum(arr[:k-1])
        threshold *= k # easier to compare with total sum instead of average

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if curSum >= threshold:
                res += 1
            curSum -= arr[L]
        return res
