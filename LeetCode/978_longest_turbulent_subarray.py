class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        beats 54.79%
        """
        length = len(arr)
        if length <= 1:
            return length

        i = 1
        while i < length and arr[i] == arr[i - 1]:
            i += 1

        if i == length:
            return 1

        res = 2
        cur = 2

        for j in range(i + 1, length):
            if cur == 1: # last 2 num are same
                cur += 1
                res = max(cur, res)
            # check with next number
            # if turbulent then continue
            elif (arr[j] > arr[j - 1] and arr[j - 2] > arr[j - 1]) or (arr[j] < arr[j - 1] and arr[j - 2] < arr[j - 1]):
                cur += 1
                res = max(cur, res)
            else: # else start from current number
                if arr[j] == arr[j - 1]: # cur and last number are same
                    res = max(cur, res)
                    cur = 1
                else: # inconsistent and keep cur and last number
                    res = max(cur, res)

        return res


    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=V_iHUhR8Dek

        beats 42.76%
        """
        l, r = 0, 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""
        return res

                    cur = 2
            
