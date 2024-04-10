class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        beats 5.05%
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
        # flag = arr[i - 1] > arr[i] # True
        # print("flag before: ", flag)

        for j in range(i + 1, length):
            print("j: ", j)
            print("cur: ", cur)
            if cur == 1: # last 2 num are same
                cur += 1
                # flag = arr[j - 1] > arr[j]
                res = max(cur, res)
            # check with next number
            # if turbulent then continue
            elif (arr[j] > arr[j - 1] and arr[j - 2] > arr[j - 1]) or (arr[j] < arr[j - 1] and arr[j - 2] < arr[j - 1]):
                cur += 1
                res = max(cur, res)
            else: # else start from current number
                if arr[j] == arr[j - 1]:
                    res = max(cur, res)
                    cur = 1
                else:
                    res = max(cur, res)
                    cur = 2
                    # flag = arr[j - 1] > arr[j]
            # print("flag after: ", flag)
            
        return res
