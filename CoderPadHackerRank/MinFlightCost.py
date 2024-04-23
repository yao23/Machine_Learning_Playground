"""
Plan a round trip between two cities with minimum flight cost.
From departure city to destination city, the fees are stored in array D[].
From destination city to departure city, the fees are stored in array R[].
Both arrays should have equal length, and index corresponds to dates.

    0   1  2  3   4
D: [10, 8, 9, 11, 7]
R: [8,  8, 10, 7, 9]

S: [18, 16, 19, 18, 16]

minPriceAfterIndex: [7, 7, 7, 7, 9]
sum:[17, 15, 16, 18, 16]
"""

# T: O(n) - two rounds iteration
# S: O(n)
def getMinFlightCost(D, R):
    minPriceAtAfterIndex = [0] * len(R) # min price at or after this index for array R
    minPriceAtAfterIndex[len(R) - 1] = R[len(R) - 1]
    for i in range(len(R) - 2, -1, -1):
        minPriceAtAfterIndex[i] = min(R[i], minPriceAtAfterIndex[i + 1])
        # totalPrice and compare with res

    res = float("inf")
    for i in range(len(D)):
        totalPrice = D[i] + minPriceAtAfterIndex[i]
        res = min(res, totalPrice)

    return res

# T: O(n) - one round iteration
# S: O(n)
def getMinFlightCost(D, R):
    minPriceAtAfterIndex = [0] * len(R) # min price at or after this index for array R
    minPriceAtAfterIndex[len(R) - 1] = R[len(R) - 1]
    res = D[-1] + minPriceAtAfterIndex[-1]
    totalPrice = 0
    for i in range(len(R) - 2, -1, -1):
        minPriceAtAfterIndex[i] = min(R[i], minPriceAtAfterIndex[i + 1])
        totalPrice = D[i] + minPriceAtAfterIndex[i]
        res = min(res, totalPrice)
        
    return res
