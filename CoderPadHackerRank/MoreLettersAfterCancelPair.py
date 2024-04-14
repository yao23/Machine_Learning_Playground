# Your previous Plain Text content is preserved below:

# Come up with code that will take two words, cancel out pairs of letters between the words, and then tell me which string has more letters. The two words can be of any length. The letters only cancel out in pairs. 

# For example, BLAMES and NIMBLE, "B", "L", "M", and "E" cancel to become "AS" and "NI". 
# Display: "They're the same length."  

# For example, JUST and CAUSE, "U", and "S" cancel to become JT and CAE. 
# Display: “CAE has more.”

# ("The letters only cancel out in pairs." which means in HELLO and HELP, only one L would cancel leaving you with LO and P)


# B: 1, L:1, A:1, M: 1, , E:1, S:1 => (AS)
# NIMBLE => NI (2)

# H:1, E:1,L:2, O:1 => LO
# H:1, E:1, L:1, P:1 => P

def getFreq(word):
    cnt = {}
    for w in word:
        if w in cnt:
            cnt[w] += 1
        else:
            cnt[w] = 1
    return cnt

def constructRes(word, cnt):
    res = ""
    for w in word:
        if cnt[w] > 0:
            res += w
            cnt[w] -= 1
    return res

def solV1(word1, word2):
    cnt = getFreq(word1)
    cnt2 = getFreq(word2)
    
    for w in word2:
        if w in cnt and cnt[w] > 0:
            cnt[w] -= 1
            cnt2[w] -= 1

    res1 = constructRes(word1, cnt)
    res2 = constructRes(word2, cnt2)

    length1 = len(res1)
    length2 = len(res2)
    if length1 == length2:
        # print("word 1 and 2 have same lenght after cancel: ", res1, res2)
        print("They're the same length.")
    elif length1 > length2:
        # print("word 1 has longer length than word 2: ", res1, res2)
        print(res1 + " has more.")
    else:
        # print("word 2 has longer length than word 1: ", res1, res2)
        print(res2 + " has more.")


def sol(word1, word2):
    cnt = {}
    length1 = len(word1)
    for w in word1:
        if w in cnt:
            cnt[w] += 1
        else:
            cnt[w] = 1

    length2 = len(word2)
    cnt2 = {}
    for w in word2:
        if w in cnt2:
            cnt2[w] += 1
        else:
            cnt2[w] = 1
        if w in cnt and cnt[w] > 0:
            cnt[w] -= 1
            cnt2[w] -= 1
            length2 -= 1 # cancel
            length1 -= 1 # cancel

    res1, res2 = "", ""
    for w in word1:
        if cnt[w] > 0:
            res1 += w
            cnt[w] -= 1

    for w in word2:
        if cnt2[w] > 0:
            res2 += w
            cnt2[w] -= 1

    if length1 == length2:
        print("word 1 and 2 have same lenght after cancel: ", res1, res2)
    elif length1 > length2:
        print("word 1 has longer length than word 2: ", res1, res2)
    else:
        print("word 2 has longer length than word 1: ", res1, res2)

w1, w2 = "BLAMES", "NIMBLE" 
w3, w4 = "JUST", "CAUSE" 
w5, w6 = "HELLO", "HELP" 

# sol(w1, w2)
# sol(w3, w4)
# sol(w5, w6)

solV1(w1, w2)
solV1(w3, w4)
solV1(w5, w6)
