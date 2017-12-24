import collections
import sys

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

    # https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
    # "a", "a" => "a"
    # "a", "b" => ""
    # beats 57.82%
    def minWindow1(self, s, t):
        need_char_counter = collections.Counter(t)
        s_len = len(s)
        need_len = len(t)
        start = 0
        end = 0
        min_len = sys.maxint  # maxsize in python3
        res_start = 0
        while end < s_len:
            if need_char_counter[s[end]] > 0:  # find t char in s
                need_len -= 1
            need_char_counter[s[end]] -= 1
            end += 1  # move right pointer to right (expand window)

            while need_len == 0:  # find t in s
                if end - start < min_len:  # update min_len
                    res_start = start
                    min_len = end - start

                if need_char_counter[s[start]] == 0:  # t char in s (pass a valid char and need one more)
                    need_len += 1
                need_char_counter[s[start]] += 1
                start += 1  # move left pointer to right (narrow window)

        return "" if (min_len == sys.maxint) else s[res_start:res_start + min_len]
