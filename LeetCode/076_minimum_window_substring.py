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
        target_char_counter = collections.Counter(t)
        s_len = len(s)
        need_str_num, start, end, d, head = len(t), 0, 0, sys.maxint, 0
        # print("conter: %s" % target_char_counter)
        while end < s_len:
            # print("New round:")
            # print("step0: %d, %d, %d, %d, %d" % (head, start, end, d, need_str_num))
            # print("cur char: %s, %d" % (s[end], target_char_counter[s[end]]))
            if target_char_counter[s[end]] > 0:
                need_str_num -= 1
            target_char_counter[s[end]] -= 1
            end += 1
            # print("step1: %d, %d, %d, %d, %d" % (head, start, end, d, need_str_num))

            while need_str_num == 0:
                # print("New round inside:")
                # print("step2: %d, %d, %d, %d, %d" % (head, start, end, d, need_str_num))
                if end - start < d:
                    head = start
                    d = end - start
                    # print("min len: %d" % d)
                # print("step3: %d, %d, %d, %d, %d" % (head, start, end, d, need_str_num))
                if target_char_counter[s[start]] == 0:
                    need_str_num += 1
                target_char_counter[s[start]] += 1
                start += 1
                # print("step4: %d, %d, %d, %d, %d" % (head, start, end, d, need_str_num))

        # print("min len (finally): %d" % d)
        # print("step5: %d, %d, %d, %d, %d" % (head, start, end, d, need_str_num))
        return "" if (d == sys.maxint) else s[head:head + d]
