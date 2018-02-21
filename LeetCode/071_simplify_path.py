class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str

        beats 37.22%
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
