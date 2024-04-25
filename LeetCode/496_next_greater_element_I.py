class Solution:
    """
    beats 77.46%
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        m = {}
        for i, n in enumerate(nums1):
            m[n] = i

        stack = [nums2[len(nums2) - 1]]
        for i in range(len(nums2) - 2, -1, -1):
            cur = nums2[i]
            tmp = -1
            if stack and cur <= stack[-1]:
                tmp = stack[-1]
            else:
                while stack and stack[-1] < cur:
                    stack.pop()
                if stack:
                    tmp = stack[-1]

            stack.append(cur)

            if cur in m and tmp != -1:
                index = m[cur]
                res[index] = tmp

        return res
      
    """
    beats 52.36%
    """
    def nextGreaterElementV0(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        m = {}
        for i, n in enumerate(nums1):
            m[n] = i

        last = nums2[len(nums2) - 1]
        stack = [last]
        for i in range(len(nums2) - 2, -1, -1):
            cur = nums2[i]
            # print(f"index: {i}, num: {cur}")
            # if stack:
            #     print(f"stack top: {stack[-1]}")
            tmp = -1
            if stack and cur <= stack[-1]:
                tmp = stack[-1]
                stack.append(cur)
            else:
                while stack and stack[-1] < cur:
                    stack.pop()
                if stack:
                    tmp = stack[-1]
                stack.append(cur)
            

            # print(f"tmp: {tmp}")

            if cur in m and tmp != -1:
                index = m[cur]
                res[index] = tmp

        return res

    """
    https://www.youtube.com/watch?v=68a1Dc_qVq4
    
    beats 58.33%
    """
    def nextGreaterElementV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O (n + m)
        nums1Idx = { n:i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]

            # while stack exists and current is greater than the top of the stack
            while stack and cur > stack[-1]:
                val = stack.pop() # take top val
                idx = nums1Idx[val]
                res[idx] = cur

            if cur in nums1Idx:
                stack.append(cur)
        
        return res
    
    
        # O (n * m)
        nums1Idx = { n:i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        
        return res
