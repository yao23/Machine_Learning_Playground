def knows(a, b):
    """
    The knows API is already defined for you.
    @param a, person a
    @param b, person b
    @return a boolean, whether a knows b
    """
    pass


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int

        Explanation

        The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
        After the first loop, x is the only candidate.
        The second and third loop is to verify x is actually a celebrity by definition.

        The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison,
        if a knows b then a < b, if a does not know b, a > b. Then if there is a celebrity,
        he/she must be the "maximum" of the n people.

        However, the "maximum" may not be the celebrity in the case of no celebrity at all.
        Thus we need the second and third loop to check if x is actually celebrity by definition.

        The total calls of knows is thus 3n at most. One small improvement is that in the second loop
        we only need to check i in the range [0, x). You can figure that out yourself easily.

        beats 55.71%
        """
        x = 0
        for i in range(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in range(x)):
            return -1
        if any(not knows(i, x) for i in range(n)):
            return -1
        return x
