# You're given a calendar year represented as a char array that contains
# either H or W where:
#
# H = Holiday W = Workday
#
# Given a number of Personal Time-Off days (PTO), maximize the length of
# the longest vacation you can take. No rollovers.
#
# Example:
# [W, H, H, W, W, H, W], PTO = 2 --> Your maximum vacation is 5 days.
#
# FB
#
# https://leetcode.ca/all/568.html#google_vignette
# https://leetcode.ca/2017-06-20-568-Maximum-Vacation-Days/#google_vignette
# https://leetcode.com/discuss/interview-experience/2122483/find-max-number-of-days-for-which-a-person-can-go-for-vacation
# https://github.com/grandyang/leetcode/issues/568

def maxVacation(self, input, numPTO):
    # condition (empty, len(input) <= numPTO)
    res = 0
    if len(input) <= numPTO:
        return len(input)
    # left, right
    cur = 0 # cur work day
    l, r = 0, 0
    while r < len(input):
        c = input[r] # w, H, W
        if c == "H":
            res = max(res, r - l + 1) # 2, 3,  5 - 1 + 1 = 5
            r += 1 # 6
        else:
            if cur + 1 <= numPTO: # 2, 3
                res = max(res, r - l + 1) # 4 - 1 + 1, 6 - 2 + 1
                r += 1 # 5
                cur += 1 # 2
            else:
                while input[l] != "W": # pass holiday until workday
                    l += 1
                l += 1 # 1
                cur -= 1 # 1                

    return res
