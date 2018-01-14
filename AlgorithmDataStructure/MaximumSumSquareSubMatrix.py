import sys


def kadane(a):
    """
    Maximum sum for rectangle sub-matrix
    :param a:
    :return:
    """
    print("array: %s" % a)
    # result[0] == maxSum, result[1] == start, result[2] == end;
    result = [-sys.maxsize - 1, 0, -1]
    current_sum = 0
    local_start = 0

    for i in range(len(a)):
        current_sum += a[i]
        if current_sum < 0:
            current_sum = 0
            local_start = i + 1
        elif current_sum > result[0]:
            result[0] = current_sum
            result[1] = local_start
            result[2] = i

        # all numbers in a are negative
        if result[2] == -1:
            result[0] = 0;
            for i in range(len(a)):
                if a[i] > result[0]:
                    result[0] = a[i]
                    result[1] = i
                    result[2] = i
    return result


def find_max_sub_rectangle_matrix(a):
    cols = len(a[0])
    rows = len(a)
    current_result = []
    max_sum = -sys.maxsize - 1
    left = 0
    top = 0
    right = 0
    bottom = 0

    for left_col in range(cols):
        tmp = [0] * rows

        for right_col in range(left_col, cols):

            for i in range(rows):
                tmp[i] += a[i][right_col]

            current_result = kadane(tmp)
            if current_result[0] > max_sum:
                max_sum = current_result[0]
                left = left_col
                top = current_result[1]
                right = right_col
                bottom = current_result[2]

    print("MaxSum: %d, range: [(%d, %d) (%d, %d)]" % (max_sum, left, top, bottom, right))


def find_max_sub_square_matrix(a):
    """
    Brute force to get max sum in square sub-matrix, O(n^5)
    :param a:
    :return:
    """
    cols = len(a[0])
    rows = len(a)
    max_sum = -sys.maxsize - 1
    for x in range(rows):
        for y in range(cols):
            for length in range(1, rows + 1 - max(x, y)):
                cur_sum = 0
                print("length: %d" % length)
                for i in range(x, x + length):
                    for j in range(y, y + length):
                        cur_sum += a[i][j]
                print("cur_sum: %d, max_sum: %d" % (cur_sum, max_sum))
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    print("max_sum: %d, x: %d, y: %d, len: %d" % (max_sum, x, y, length))

    return max_sum


def print_matrix(mat):
    n = len(mat)
    for x in range(n):
        for y in range(n):
            print("%d" % mat[x][y])


def print_square_sum(mat, k, max_sum):
    print("square side length: %d" % k)
    n = len(mat)
    # k must be smaller than or equal to n
    if k > n:
        return

    # 1: Pre-processing
    # To store sums of all strips of size k x 1
    # https://stackoverflow.com/questions/21036140/python-two-dimensional-array-changing-an-element
    strip_sum = [[0] * n for _ in range(n)]

    # Go column by column
    for j in range(n):
        # Calculate sum of first k x 1 rectangle in this column
        cur_sum = 0
        for i in range(k):
            cur_sum += mat[i][j]
        strip_sum[0][j] = cur_sum
        # Calculate sum of remaining rectangles (strip sum)
        for i in range(1, n - k + 1):
            cur_sum += (mat[i + k - 1][j] - mat[i - 1][j])
            strip_sum[i][j] = cur_sum

    # 2: CALCULATE SUM of Sub-Squares using strip_sum[][]
    for i in range(n - k + 1):
        # Calculate and print sum of first sub-square in this row
        cur_sum = 0
        for j in range(k):
            cur_sum += strip_sum[i][j]
        max_sum = max(max_sum, cur_sum)

        # Calculate sum of remaining squares in current row by
        # removing the leftmost strip of previous sub-square and
        # adding a new strip
        for j in range(1, n - k + 1):
            cur_sum += (strip_sum[i][j + k - 1] - strip_sum[i][j - 1])
            max_sum = max(max_sum, cur_sum)

    return max_sum


def find_max_sub_square_matrix1(a):
    """
    Get max sum in square sub-matrix with optimization, O(n^3)

    https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

    :param a:
    :return:
    """
    length = len(a)
    max_sum = -sys.maxsize - 1
    for i in range(length):
        max_sum = print_square_sum(a, i + 1, max_sum)

    return max_sum


# values = [[10, 20], [30, 40, 50, 60, 70]]
input_matrix = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1], [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]
input_matrix1 = [[3, -1, 4], [4, -2, 6], [3, 1, -21]]
# find_max_sub_matrix(input_matrix)
# find_max_sub_matrix([[3,-1,4],[4,-2,6],[3,1,-21]])
find_max_sub_square_matrix1(input_matrix1)
