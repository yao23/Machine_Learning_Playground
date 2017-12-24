import collections


class Solution(object):
    # beats 42.97%
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        current window is s[cur_left:cur_right] and the result window is s[res_left:res_right].
        In need[c] I store how many times I need character c (can be negative) and missing tells how many characters
        are still missing. In the loop, first add the new character to the window.
        Then, if nothing is missing, remove as much as possible from the window start and then update the result.
        """
        need, missing = collections.Counter(t), len(t)
        cur_left = res_left = res_right = 0
        for cur_right, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:  # find string t
                while cur_left < cur_right and need[s[cur_left]] < 0:
                    need[s[cur_left]] += 1
                    cur_left += 1
                if not res_right or cur_right - cur_left <= res_right - res_left:  # find smaller window
                    res_left, res_right = cur_left, cur_right
        return s[res_left:res_right]
