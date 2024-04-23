"""
Given a string with alpha-numeric characters and parentheses, return a string with balanced parentheses by removing the fewest characters possible. You cannot add anything to the string.

balance("()") -> "()"
balance("a(b)c)") -> "a(b)c" -> "a(bc)"
balance("(a(b)c)") -> "(a(b)c)"
balance("ab)c)") -> "abc"
balance("(a(bc") -> "abc"
"""

# T: O(n)
# S: O(1)
def balace(input):
    res = ""
    cntLeft = 0
    cntRight = 0
    for i in range(len(input)):
        if input[i] == "(":
            res += input[i]
            cntLeft += 1
        elif input[i] == ")":
            if cntRight < cntLeft:
                res += input[i]
                cntRight += 1
        else:
            res += input[i]

    if cntLeft > cntRight: # process more left parentheses
        tmp = ""
        for i in range(len(res)):
            if res[i] == "(":
                if cntLeft > cntRight:
                    cntLeft -= 1
                else:
                    tmp += res[i]
            else:
                tmp += res[i]
        return tmp
    else:
        return res

