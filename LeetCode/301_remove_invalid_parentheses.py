class Solution(object):
    # `self` check
    # beats 35.33%
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0

        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}

    # `eval` check
    # beats 9.32%
    def removeInvalidParentheses1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        level = {s}
        while True:
            valid = []
            for s in level:
                try:
                    eval('0,' + filter('()'.count, s).replace(')', '),'))
                    valid.append(s)
                except:
                    pass
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

    # mix above two
    # beats 7.71%
    def removeInvalidParentheses2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            try:
                eval('0,' + filter('()'.count, s).replace(')', '),'))
                return True
            except:
                pass

        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}

    # beats 13.23%
    def removeInvalidParentheses3(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            s = filter('()'.count, s)
            while '()' in s:
                s = s.replace('()', '')
            return not s

        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}