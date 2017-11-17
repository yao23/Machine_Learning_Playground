def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """

    # beats 23.59%
    return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))